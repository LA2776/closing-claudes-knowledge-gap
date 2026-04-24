---
title: "What's New in FlutterFlow - v6.4.12 | October 31, 2025"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow---v6-4-12-october-31-2025-GoleNc2CTX2JTE7"
slug: "what-s-new-in-flutterflow---v6-4-12-october-31-2025"
author: "John Higgins"
createdAt: "2025-10-31T15:47:15.184Z"
publishedAt: "2025-10-31T15:55:42.526Z"
updatedAt: "2025-11-26T16:47:12.266Z"
releaseDate: "\"2025-10-28T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:39.487894Z"
---

New Action | Toggle Expandable Widget Action
New Action: We've added a Toggle Expandable Widget action to the Action Flow Editor, giving you programmatic control over expandable widgets.
What's New:
Expand or collapse one or multiple expandable widgets through your action flows
Trigger from any action flow: button taps, page load, API responses, or conditional logic
Control multiple expandable widgets simultaneously for coordinated UI updates
Use Cases:
Create "Expand All" / "Collapse All" buttons for FAQ sections
Auto-expand specific sections based on user actions or data
Close other expandables when opening a new one (accordion behavior)
Programmatically open relevant sections after search or filtering
Guide users through multi-step forms by auto-expanding the next section
This gives you fine-grained control over your expandable UI components without relying solely on manual user interaction.
Rebuild Type Control for Form Field Actions
New Option: Set/Reset Form Field actions now include a Rebuild Type setting, giving you control over when the UI rebuilds.
What's New:
Choose between Rebuild or No Rebuild when setting or resetting form fields
Optimize performance by preventing unnecessary UI updates
Batch multiple form field updates into a single rebuild operation
How It Works:
Rebuild - Updates the field value and immediately rebuilds the widget tree
Use for single field updates where users expect instant visual feedback
Use when other UI elements depend on the field value (conditional visibility, button states, etc.)
No Rebuild - Updates the field value directly without triggering a rebuild
Use when updating multiple fields at once (like loading profile data)
Use for hidden or off-screen fields
Improves performance for batch operations
Bug Fixes
Fixed: The "click to fix project error" feature now correctly executes for Set/Reset Form Field actions.
Fixed: File downloads no longer create duplicate extensions (like "image.png.png") on mobile and desktop platforms.
What We’re Working On
Monthly Collaborator Passes: We're working on the ability to purchase monthly collaborator passes, giving you more flexible options for team collaboration.
Ownership Transfer: Transferring ownership of a project will soon become much smoother
