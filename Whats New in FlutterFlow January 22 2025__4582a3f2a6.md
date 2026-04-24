---
title: "What's New in FlutterFlow | January 22, 2025"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow-january-22-2025-D4kO2VnKByIsOJd"
slug: "what-s-new-in-flutterflow-january-22-2025"
author: "Inactive Member"
createdAt: "2025-01-22T20:41:15.032Z"
publishedAt: "2025-01-22T20:41:15.000Z"
updatedAt: "2025-02-24T10:18:08.452Z"
releaseDate: "\"2025-01-22T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:49.748381Z"
---

Git Merge (Beta)
We’re excited to introduce Git Merge, a new (beta) way to combine changes between branches in FlutterFlow. Previously, we used a custom tool that directly compared branches within FlutterFlow to merge, but it sometimes caused unexpected results when merging. This new approach uses YAML files (a format that describes your project’s configuration) and Git to compare and merge changes more reliably.
Because this is an early release, you may run into a few challenges—especially with performance, the wording of YAML errors, and making the YAML format clearer for everyone. We’re actively working to improve all these areas and will release updates in each release.
To learn how to start a merge and navigate the new merge view, check out our documentation, and see how to resolve merge conflicts. Stay tuned for more resources and improvements soon!
Current Route Global Variable
We’ve introduced a new global variable that provides the route name of the currently active page, allowing you to differentiate between a truly active page and one running in the background (e.g., when launching the app via push notification). It enables you to conditionally block or allow actions based on whether the user is on the expected page, helping resolve issues like this one, by preventing unwanted behavior when background pages are still running.
Other Improvements 🛠️
Performance enhancements
Updated canvas settings user experience
New Features We're Working On 🏗️
Improved performance for CLI, test mode and local run
Continuing to refine new branching experience
Hooks for editing native code
Supporting pages in Libraries
Custom code enhancements
UX improvements

## Related documentation
- https://docs.flutterflow.io/collaboration/branching/#git-merge-new
- https://docs.flutterflow.io/collaboration/branching/#git-merge-new-1

