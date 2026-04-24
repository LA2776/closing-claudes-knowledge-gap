---
title: "An Apology & Update on Test Mode"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/an-apology-update-on-test-mode-9L4EgvDTuzpI6VK"
slug: "an-apology-update-on-test-mode"
author: "Alex Greaves"
createdAt: "2025-07-30T22:51:41.854Z"
publishedAt: "2025-07-30T22:51:41.882Z"
updatedAt: "2025-09-12T09:55:02.266Z"
releaseDate: "\"2025-07-30T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:42.096940Z"
---

Hey everyone,
We owe you an update and an apology. Over the past few weeks, Test Mode has been unstable for many of you. Sometimes it works. Sometimes it hangs… sometimes it fails completely. We’ve heard a lot of you who have been blocked. That’s not okay.
We know Test Mode is core to how you build. It’s meant to be fast, seamless, and reliable. When it breaks, it slows you down and defeats the whole premise of using FlutterFlow in the first place. And we took far too long to fix this issue.
We’re sorry.
What happened?
Flutter version 3.32 quietly broke an assumption we’ve relied on for years: that certain debug assets could be shared and cached across projects. Since Flutter 3.32 that assumption no longer holds true and Test Mode suddenly needs to fetch many more unique files per session.
We caught this in internal testing and shipped what we thought was a fix, which worked in dev and passed existing tests. But once in production at scale, it caused unexpected network overloads — which led to the sporadic failures many of you saw. We tried to patch that too (more servers, longer timeouts), but the root problem needed more investigation.
We’ve rolled out a fix to all users and are monitoring potential edge cases. Please reach out with a bug report code if this issue is not resolved for you. You may need to force refresh your browser to see the changes take effect.
Once again, we want to apologize deeply for the pain this has caused. We appreciate your patience, and your pressure, and will do everything we can to make sure this doesn’t happen again.
Alex, Abel, & The FlutterFlow Team
