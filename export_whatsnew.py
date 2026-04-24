"""
FlutterFlow "What's New" Exporter
==================================
Exports posts from FlutterFlow's Community "What's New" section
(powered by Bettermode) into individual Markdown files.

Includes diff mode: re-runs only export new or updated posts.
Set FULL_REFRESH = True to re-export everything from scratch.

Environment: Windows (tested on Windows 11)
Auth: Netscape/Mozilla cookies.txt exported from browser

Usage:
    python export_whatsnew.py
    python export_whatsnew.py --full-refresh
"""

import requests
import pathlib
import datetime as dt
import re
import json
import hashlib
import time
import sys
import html as html_lib
from http.cookiejar import MozillaCookieJar
from dateutil import parser as dateparser
from markdownify import markdownify as md
from html.parser import HTMLParser
from urllib.parse import urljoin

# ============================================================
# CONFIGURATION
# ============================================================

WORKDIR = pathlib.Path(__file__).parent
COOKIES_TXT = WORKDIR / "cookies.txt"

TOPICS_DIR = WORKDIR / "topics"
MANUAL_DIR = WORKDIR / "needs_manual"
TOPICS_DIR.mkdir(exist_ok=True)
MANUAL_DIR.mkdir(exist_ok=True)

INDEX_MD = WORKDIR / "index.md"
CACHE_JSON = WORKDIR / "export_cache.json"

# Export posts with releaseDate/createdAt >= this date, stop once older
CUTOFF = dt.datetime(2024, 1, 1, tzinfo=dt.timezone.utc)

API_URL = "https://api.bettermode.com/"
SPACE_ID = "efisN1RDE6hn"
POST_TYPE_ID = "CLDhuwrITiTyBAI"

PAGE_LIMIT = 20
TIMEOUT = 45

# Set True to re-export everything (ignores cache)
FULL_REFRESH = "--full-refresh" in sys.argv

# Set True for diagnosing API issues
DEBUG = False

# ============================================================
# GRAPHQL QUERIES
# ============================================================

# SAFE LIST QUERY: do not request any "rich body" fields here.
QUERY_LIST = """
query GetPosts($after: String, $limit: Int!, $spaceIds: [ID!], $postTypeIds: [String!], $orderByString: String, $reverse: Boolean, $filterBy: [PostListFilterByInput!]) {
  posts(
    after: $after
    limit: $limit
    spaceIds: $spaceIds
    postTypeIds: $postTypeIds
    orderByString: $orderByString
    reverse: $reverse
    filterBy: $filterBy
  ) {
    totalCount
    pageInfo { endCursor hasNextPage }
    nodes {
      id
      title
      slug
      createdAt
      publishedAt
      updatedAt
      hasMoreContent
      shortContent
      textContent
      relativeUrl
      url
      fields { key value }
      owner { member { id name username displayName } }
    }
  }
}
"""

# Single post fetch
QUERY_ONE = """
query GetPost($id: ID!) {
  post(id: $id) {
    id
    title
    slug
    createdAt
    publishedAt
    updatedAt
    hasMoreContent
    shortContent
    textContent
    relativeUrl
    url
    fields { key value }
    owner { member { id name username displayName } }
  }
}
"""

# ============================================================
# HELPERS
# ============================================================

def cookie_value_latest(jar: MozillaCookieJar, name: str) -> str:
    matches = [c for c in jar if c.name == name and (c.value or "").strip()]
    if not matches:
        return ""
    best = max(matches, key=lambda c: (c.expires or 0))
    return best.value


def apply_auth(session: requests.Session) -> None:
    """
    Reload cookies.txt and set Authorization header from freshest c_access_token.
    This handles Bettermode's intermittent 'Forbidden resource' behavior.
    """
    jar = MozillaCookieJar()
    jar.load(str(COOKIES_TXT), ignore_discard=True, ignore_expires=True)
    session.cookies = jar

    token = cookie_value_latest(jar, "c_access_token")
    if not token:
        raise SystemExit(
            "ERROR: c_access_token not found in cookies.txt.\n"
            "Re-export cookies from the Community tab while logged in."
        )
    token = token.strip().strip('"').strip("'")

    session.headers.update({
        "Content-Type": "application/json",
        "Origin": "https://community.flutterflow.io",
        "Referer": "https://community.flutterflow.io/",
        "User-Agent": "Mozilla/5.0",
        "x-request-source": "neo-csr",
        "Authorization": f"Bearer {token}",
    })


def parse_dt(value: str) -> dt.datetime:
    if not value:
        raise ValueError("Empty date value")
    value = value.strip().strip('"').strip("'")
    d = dateparser.parse(value)
    if not d:
        raise ValueError(f"Could not parse date: {value}")
    if not d.tzinfo:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d.astimezone(dt.timezone.utc)


def safe_filename(s: str, max_len: int = 120) -> str:
    s = re.sub(r"[^\w\-\.\(\) ]+", "", (s or "")).strip()
    s = re.sub(r"\s+", " ", s)
    return (s[:max_len].rstrip() or "post")


def sha10(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]


def field_value(fields, key: str):
    for f in fields or []:
        if f.get("key") == key:
            return f.get("value")
    return None


def needs_manual_stub(url: str, reason: str) -> str:
    return (
        "# NEEDS_MANUAL_CAPTURE\n\n"
        f"- url: {url}\n"
        f"- reason: {reason}\n"
        f"- captured_at_utc: {dt.datetime.utcnow().isoformat()}Z\n"
    )


def looks_like_html(s: str) -> bool:
    if not s:
        return False
    s = s.strip()
    return ("<a " in s) or ("</" in s) or ("<p" in s) or ("<div" in s) or ("<span" in s)


def normalize_to_markdown(text_content: str, short_content: str) -> str:
    """
    If content looks like HTML, convert to Markdown (keeps <a href> if present).
    Otherwise keep as plain text.
    """
    raw = (text_content or short_content or "").strip()
    if not raw:
        return ""
    if looks_like_html(raw):
        return md(raw, heading_style="ATX").strip()
    return raw


# ============================================================
# CACHE (diff mode)
# ============================================================

def load_cache() -> dict:
    """
    Cache format:
    {
      "version": 1,
      "posts": {
        "<url>": {
          "updatedAt": "<iso string>",
          "path": "topics/<filename>.md"
        }
      }
    }
    """
    if not CACHE_JSON.exists():
        return {"version": 1, "posts": {}}
    try:
        return json.loads(CACHE_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {"version": 1, "posts": {}}


def save_cache(cache: dict) -> None:
    CACHE_JSON.write_text(
        json.dumps(cache, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ============================================================
# GRAPHQL CLIENT
# ============================================================

def graphql(session: requests.Session, query: str, variables: dict, op_name: str) -> dict:
    payload = {"operationName": op_name, "query": query, "variables": variables}
    r = session.post(API_URL, json=payload, timeout=TIMEOUT)

    if DEBUG:
        print("\n=== GRAPHQL DEBUG ===")
        print("op_name:", op_name)
        print("HTTP:", r.status_code)
        print("resp_content_type:", r.headers.get("Content-Type"))
        print("resp_text_first_600:", r.text[:600])
        print("variables:", json.dumps(variables, indent=2)[:1200])
        print("=== END DEBUG ===\n")

    r.raise_for_status()
    j = r.json()
    if j.get("errors"):
        msgs = "; ".join([e.get("message", "(no message)") for e in j["errors"][:3]])
        raise RuntimeError(f"GraphQL errors: {msgs}")
    return j.get("data") or {}


def get_posts_with_retry(session: requests.Session, after):
    """
    If Bettermode returns Forbidden resource, reload cookies+token and retry.
    """
    attempts = 3
    last_err = None
    for _ in range(attempts):
        try:
            return graphql(
                session,
                QUERY_LIST,
                variables={
                    "after": after,
                    "limit": PAGE_LIMIT,
                    "spaceIds": [SPACE_ID],
                    "postTypeIds": [POST_TYPE_ID],
                    "orderByString": "fields.releaseDate",
                    "reverse": True,
                    "filterBy": [],
                },
                op_name="GetPosts",
            )
        except Exception as e:
            last_err = e
            if "Forbidden resource" in str(e):
                apply_auth(session)
                time.sleep(0.8)
                continue
            raise
    raise RuntimeError(
        "Your Community cookie token expired. "
        "Re-export cookies.txt from the Community tab and re-run immediately.\n"
        f"Last error: {last_err}"
    )


# ============================================================
# HTML FALLBACK: extract docs links from post page
# ============================================================

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self._in_a = False
        self._href = None
        self._text_chunks = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            self._in_a = True
            self._href = dict(attrs).get("href")
            self._text_chunks = []

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self._in_a:
            text = "".join(self._text_chunks).strip()
            href = (self._href or "").strip()
            if href:
                self.links.append((href, text))
            self._in_a = False
            self._href = None
            self._text_chunks = []

    def handle_data(self, data):
        if self._in_a and data:
            self._text_chunks.append(data)


def extract_doc_links_from_page(session: requests.Session, post_url: str) -> list:
    """
    Fetch the post HTML and find docs.flutterflow.io links.
    Works even if the page is JS-rendered by regex-scanning the HTML/JS payload.
    """
    r = session.get(post_url, timeout=TIMEOUT)
    r.raise_for_status()
    html = r.text or ""
    hay = html_lib.unescape(html)

    urls = []

    # 1) Parse anchors, if present in server HTML
    p = LinkExtractor()
    p.feed(html)
    for href, _text in p.links:
        urls.append(urljoin(post_url, href))

    # 2) Regex scan for docs URLs anywhere in HTML/JS
    urls += re.findall(r"https?://docs\.flutterflow\.io[^\s\"'<>)]*", hay)

    # Filter + clean + de-dupe
    filtered = []
    for u in urls:
        if "docs.flutterflow.io" in (u or "").lower():
            filtered.append(u)

    seen = set()
    out = []
    for u in filtered:
        u = u.rstrip('",.)]>}')
        # Remove generic homepage (with or without trailing slash)
        if u.rstrip("/") == "https://docs.flutterflow.io":
            continue
        if u and u not in seen:
            out.append(u)
            seen.add(u)
    return out


# ============================================================
# MAIN
# ============================================================

def run():
    session = requests.Session()
    apply_auth(session)

    # Load diff cache
    cache = load_cache()
    cache_posts = cache.get("posts", {})
    if FULL_REFRESH:
        print("FULL REFRESH mode: re-exporting all posts.")
    else:
        print(f"Diff mode: {len(cache_posts)} posts in cache.")

    index_lines = ["# FlutterFlow — What's New (export)\n"]
    after = None
    exported = 0
    skipped = 0
    manual = 0

    while True:
        try:
            data = get_posts_with_retry(session, after)
        except Exception as e:
            (MANUAL_DIR / f"LISTING_FAILED_{sha10(str(after))}.md").write_text(
                needs_manual_stub(
                    "https://community.flutterflow.io/c/whats-new-in-flutterflow",
                    str(e),
                ),
                encoding="utf-8",
            )
            manual += 1
            break

        posts_block = (data.get("posts") or {})
        pageinfo = (posts_block.get("pageInfo") or {})
        nodes = posts_block.get("nodes") or []

        if not nodes:
            break

        for node in nodes:
            try:
                post_id = node.get("id")
                if not post_id:
                    raise ValueError("Missing post id")

                title = node.get("title") or "Untitled"
                slug = node.get("slug") or post_id or sha10(title)
                url = node.get("url") or (
                    "https://community.flutterflow.io" + node.get("relativeUrl", "")
                )

                # Cutoff based on releaseDate (preferred) else createdAt
                release = field_value(node.get("fields"), "releaseDate")
                cutoff_dt = parse_dt(release) if release else parse_dt(node["createdAt"])
                if cutoff_dt < CUTOFF:
                    # Save cache and index before exiting
                    cache["posts"] = cache_posts
                    save_cache(cache)
                    INDEX_MD.write_text("\n".join(index_lines) + "\n", encoding="utf-8")
                    print("Reached posts older than Jan 1, 2024. Stopping.")
                    print(f"Done. Exported {exported}, skipped {skipped}, {manual} needs_manual stubs.")
                    return

                # Fetch full post (textContent/shortContent)
                one = graphql(session, QUERY_ONE, {"id": post_id}, "GetPost").get("post") or {}

                text_content = one.get("textContent") or node.get("textContent")
                short_content = one.get("shortContent") or node.get("shortContent")

                # Update url/slug/title if present
                url = one.get("url") or url
                slug = one.get("slug") or slug
                title = one.get("title") or title

                body_md = normalize_to_markdown(text_content, short_content)
                if not body_md.strip():
                    raise ValueError("Empty content after extraction")

                # DOCS FALLBACK:
                # If text mentions documentation but no docs.flutterflow.io URL present,
                # scrape the page and append found docs links.
                doc_trigger = "documentation" in body_md.lower()
                already_has_docs_url = "docs.flutterflow.io" in body_md.lower()

                if doc_trigger and not already_has_docs_url:
                    try:
                        doc_links = extract_doc_links_from_page(session, url)
                        if doc_links:
                            body_md += "\n\n## Related documentation\n"
                            for u in doc_links:
                                body_md += f"- {u}\n"
                    except Exception:
                        pass  # do not fail export because scraping failed

                author = (
                    ((one.get("owner") or {}).get("member") or {}).get("displayName")
                    or ((one.get("owner") or {}).get("member") or {}).get("name")
                    or ""
                )

                created_at = one.get("createdAt") or node.get("createdAt") or ""
                updated_at = one.get("updatedAt") or node.get("updatedAt") or ""
                published_at = one.get("publishedAt") or node.get("publishedAt") or ""

                # Stable filename by URL hash (prevents duplicates on title change)
                h = sha10(url or (slug + created_at))
                fname = f"{safe_filename(title)}__{h}.md"

                front = (
                    "---\n"
                    f"title: {json.dumps(title)}\n"
                    f"url: {json.dumps(url)}\n"
                    f"slug: {json.dumps(slug)}\n"
                    f"author: {json.dumps(author)}\n"
                    f"createdAt: {json.dumps(created_at)}\n"
                    f"publishedAt: {json.dumps(published_at)}\n"
                    f"updatedAt: {json.dumps(updated_at)}\n"
                    f"releaseDate: {json.dumps(release or '')}\n"
                    f"capturedAtUtc: {json.dumps(dt.datetime.utcnow().isoformat() + 'Z')}\n"
                    "---\n\n"
                )

                # ---- DIFF LOGIC ----
                remote_updated = updated_at or ""
                cache_key = url
                should_export = FULL_REFRESH

                if not should_export:
                    if cache_key not in cache_posts:
                        should_export = True
                        reason = "NEW"
                    else:
                        local_updated = cache_posts[cache_key].get("updatedAt") or ""
                        if remote_updated and remote_updated > local_updated:
                            should_export = True
                            reason = "UPDATED"
                        else:
                            reason = "UNCHANGED"

                if should_export:
                    # If an old file exists under a different name (title changed), remove it
                    if cache_key in cache_posts:
                        old_path = TOPICS_DIR / pathlib.Path(cache_posts[cache_key].get("path", "")).name
                        if old_path.exists() and old_path.name != fname:
                            old_path.unlink()

                    (TOPICS_DIR / fname).write_text(front + body_md + "\n", encoding="utf-8")
                    exported += 1
                    label = "REFRESH" if FULL_REFRESH else reason
                    print(f"{label}: {title}")

                    cache_posts[cache_key] = {
                        "updatedAt": remote_updated,
                        "path": f"topics/{fname}",
                    }
                else:
                    skipped += 1
                    print(f"SKIPPED: {title}")

                index_lines.append(f"- [{title}](topics/{fname})")

            except Exception as e:
                url2 = node.get("url") or (
                    "https://community.flutterflow.io" + node.get("relativeUrl", "")
                )
                title2 = node.get("title") or "Untitled"
                h = sha10(url2 or title2)
                (MANUAL_DIR / f"{safe_filename(title2)}__{h}.md").write_text(
                    needs_manual_stub(url2, str(e)),
                    encoding="utf-8",
                )
                index_lines.append(f"- [NEEDS_MANUAL] {title2} ({url2})")
                manual += 1
                print(f"NEEDS_MANUAL: {title2} -> {e}")

        if not pageinfo.get("hasNextPage"):
            break
        after = pageinfo.get("endCursor")
        if not after:
            break

    # Save cache and index
    cache["posts"] = cache_posts
    save_cache(cache)
    INDEX_MD.write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"\nDone. Exported {exported}, skipped {skipped}, {manual} needs_manual stubs.")


if __name__ == "__main__":
    run()
