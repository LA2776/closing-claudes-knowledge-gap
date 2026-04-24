# FlutterFlow "What's New" Exporter

Exports posts from [FlutterFlow's Community "What's New" section](https://community.flutterflow.io/c/whats-new-in-flutterflow) into individual Markdown files that can be loaded into AI project context (Claude, ChatGPT, Gemini, Copilot).

## Why This Exists

AI models (Claude, ChatGPT, Gemini) struggle with FlutterFlow instructions because their training data is typically 1-2 major versions behind. When an AI says "drag a Form widget from the palette," and FlutterFlow renamed it to "Form Validation" two versions ago, a non-technical builder has no way to know whether they're looking in the wrong place or following wrong instructions.

FlutterFlow publishes release notes on their community forum. But the format (embedded links, videos, nested discussions) is not something an AI can consume directly. This script exports those release notes into clean Markdown files with YAML frontmatter that any AI platform can read as project context.

The result: you load these files into your AI's project, and it knows what changed between versions. The error rate drops significantly.

## What It Does

- Exports all "What's New" posts from January 1, 2024 onward
- Converts content to clean Markdown with YAML frontmatter (title, URL, dates, author)
- Captures documentation links via HTML fallback when the API strips them
- **Diff mode** (default): re-runs only export new or updated posts
- **Full refresh mode**: re-exports everything from scratch
- Generates an `index.md` linking to all exported files

## Output Structure

```
ff-whatsnew-md/
  topics/           <- one .md file per release note
  needs_manual/     <- stubs for any posts that failed to export
  index.md          <- clickable index of all exported posts
  export_cache.json <- tracks what's been exported (for diff mode)
```

## Requirements

- **Windows 10/11** (tested on Windows 11; macOS/Linux users: adapt the batch files to shell scripts)
- **Python 3.11 or 3.12** (tested with 3.12; 3.13/3.14 should also work)
- **A FlutterFlow Community account** (free with any FlutterFlow plan)
- **A browser cookie exporter extension** (any extension that exports in Netscape/Mozilla `cookies.txt` format)

## Setup (One Time)

### Step 1: Install Python

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.12 (64-bit) for your OS
3. Run the installer
4. **CRITICAL:** Check "Add python.exe to PATH" on the first screen
5. Click Install Now

Verify it works:
```
python --version
```
You should see `Python 3.12.x`.

### Step 2: Clone or Download This Repo

**Option A** (if you have Git):
```
cd C:\
git clone https://github.com/YOUR_USERNAME/ff-whatsnew-md.git
cd ff-whatsnew-md
```

**Option B** (no Git):
1. Click the green "Code" button on GitHub, then "Download ZIP"
2. Extract to `C:\ff-whatsnew-md\`

### Step 3: Create Virtual Environment

Open Command Prompt:
```
cd C:\ff-whatsnew-md
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the start of your command line.

### Step 4: Install Dependencies

With `(venv)` active:
```
python -m pip install --upgrade pip
pip install requests python-dateutil markdownify
```

That's all you need. You only do this once.

## Running the Exporter

### The Cookie Flow (Must Be Done Every Time)

The FlutterFlow Community uses short-lived authentication tokens (~2-3 minutes). You must export cookies and run the script quickly.

1. Open [community.flutterflow.io](https://community.flutterflow.io/)
2. Click **Login with Google**
3. You'll land on your FlutterFlow project dashboard (this is normal)
4. Click **Community** in the left menu
5. A new browser tab opens: `community.flutterflow.io`
6. **In THAT tab**, use your cookie exporter extension to export cookies for `community.flutterflow.io`
7. Save as `C:\ff-whatsnew-md\cookies.txt`
8. **Immediately** double-click `run_export.bat`

**Important:** Export cookies from the Community tab only, not the dashboard tab. The token you need (`c_access_token`) only exists in the Community tab's cookies.

### Verify cookies.txt

Open `cookies.txt` in any text editor and search for `c_access_token`. If it's not there, re-export from the correct tab.

### Normal Run (Diff Mode)

Double-click `run_export.bat`. On first run, everything is NEW. On subsequent runs, only new or updated posts are exported.

### Full Refresh

Double-click `run_export_full_refresh.bat` to re-export all posts regardless of cache.

Or from the command line:
```
python export_whatsnew.py --full-refresh
```

## Expected Output

```
Diff mode: 46 posts in cache.
SKIPPED: Accessibility Improvements
SKIPPED: Component Updates
NEW: March 2026 Release Notes
...
Done. Exported 2, skipped 44, 0 needs_manual stubs.
```

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `GraphQL errors: Forbidden resource` | Cookie expired | Re-export cookies, run immediately |
| `c_access_token not found` | Wrong tab exported, or not logged in | Export from the Community tab only |
| `0 posts exported` | Token expired before script ran | Export cookies and run within 60 seconds |
| `IndentationError` | Spaces/tabs mixed in script file | Re-download the script from this repo |

## Loading Into Your AI

Once exported, you have a folder full of Markdown files. The next step is to bring them to your AI and let it figure out how to use them. Don't try to organize the files yourself — the AI knows where its own knowledge gaps are better than you do.

### Step 1: Zip the topics folder

Compress the `topics/` folder (and optionally `index.md`) into a single zip file for easy upload.

### Step 2: Upload and prompt

Upload the zip to a conversation in your AI platform of choice. Use a prompt like this:

> "Your knowledge of [platform] is outdated. I exported their release notes / changelog from [date range]. Attached are the files. Two questions: would having this help you give better answers? And if yes, what's the best way to organize it so you can actually use it?"

The key: **don't tell the AI how to organize it.** Ask it to figure that out. When I did this with Claude, it assessed the files, proposed consolidating 46 individual posts into a single structured reference document organized by topic (not by date), and I pointed out it had undervalued the documentation links — it went back, looked more carefully, and produced a better version. That back-and-forth is where the real value comes from. The AI curates its own supplemental knowledge better than you could, because it knows which categories matter for the work you're doing together.

### Step 3: Save the output as a project file

Whatever your AI produces (a consolidated reference, a structured changelog, a lookup table), save it and add it to your project's permanent context:

- **Claude**: Add to Project Knowledge files
- **ChatGPT**: Upload to a Project or Custom GPT knowledge
- **Gemini**: Attach as a reference file in a Gemini Project
- **Copilot**: Place in a OneDrive folder accessible to Copilot

### Step 4: Update your project instructions (this is the step people skip)

Having the file in your project is not enough. The AI will not consult it unless your project instructions explicitly tell it when and how.

In my experience, it took four separate changes before Claude actually started using the changelog consistently:

1. **The file had to exist in project context** — obvious, but not sufficient on its own.
2. **The instructions had to name the file and say when to check it** — something like: "Before giving FlutterFlow build instructions, check the Changelog Reference for any changes to the features you're referencing."
3. **The reading method had to be specified** — on Claude, reading the file directly (`view` tool) produced better results than searching it (`project_knowledge_search`), because search returns chunks and can miss the relevant entry in a long chronological document. If you're using Claude, tell it to read the file, not search it.
4. **Even after all three were in place, compliance still degraded** — the AI would check the changelog but then skip the next step (searching official docs for anything the changelog didn't cover) and fall back to its outdated training data. That required a separate instruction: "If the changelog doesn't explicitly cover the specific feature, search the official docs before writing instructions."

The pattern here is not specific to FlutterFlow. If you're using this approach for any platform where the AI's training data is behind, expect to iterate on your project instructions. The file alone is passive. The instructions are what make it active.

### Step 5: Re-run monthly

When FlutterFlow releases updates, re-run the exporter (diff mode will only grab what's new), then repeat Step 2 with just the new files. Ask the AI to update its reference.

## How It Works (Technical)

The FlutterFlow Community runs on [Bettermode](https://bettermode.com/). The script:

1. Authenticates via cookies exported from your browser session
2. Queries Bettermode's GraphQL API (`GetPosts` for listing, `GetPost` for individual posts)
3. Converts content to Markdown (handling both HTML and plain text formats)
4. When a post mentions "documentation" but the API doesn't return the link (GraphQL strips rich HTML), falls back to scraping the public post page for `docs.flutterflow.io` URLs
5. Uses a JSON cache file to track what's been exported, enabling efficient re-runs

**Known quirk:** Bettermode returns HTTP 200 even on authentication failures. The actual error is inside the JSON response body. The script detects this and retries with refreshed cookies.

## Background

This tool was built as part of a documented process of using three AI models (Claude, ChatGPT, Gemini) to build a FlutterFlow application with zero coding experience. The full story of why this exists and how it reduced AI instruction errors is documented in the accompanying article.

## License

MIT
