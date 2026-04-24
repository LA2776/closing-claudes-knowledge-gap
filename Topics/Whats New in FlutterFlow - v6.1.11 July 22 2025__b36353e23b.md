---
title: "What's New in FlutterFlow - v6.1.11 | July 22, 2025"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow---v6-1-11-july-22-2025-IVGybEaJbWXyft5"
slug: "what-s-new-in-flutterflow---v6-1-11-july-22-2025"
author: "Inactive Member"
createdAt: "2025-07-23T01:50:55.048Z"
publishedAt: "2025-07-23T01:50:55.073Z"
updatedAt: "2025-09-12T09:55:11.559Z"
releaseDate: "\"2025-07-22T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:42.244907Z"
---

🌳 Branching Improvements
We know branching can be tricky—especially for big projects with lots of contributors. We’re actively working to make it faster and smoother.
While there’s still more to do (performance is a key focus), here are some recent improvements:
Better Navigation: Filter by category in the merge sidebar and use advanced search (Match Case, Match Whole Word, or top-level only).
Smarter Merging: We’ve improved merge speed, especially for projects with lots of translations. We also use Git to better detect unchanged files.
Less Stale Branches: You’ll now see a stale branch dialog when trying to merge a branch that’s been hanging around for longer than a week.
Safer Conflict Resolution: When resolving a conflict, you can now Copy Nested Files, which helps keep your components intact and prevents broken dependencies.
Heads Up: We removed the option to duplicate a project with branches since that flow led to unexpected behavior for some users.
✅ Bulk User Management
You can now bulk invite team members to a project and update their roles all at once—no more one-by-one clicks.
Paste a list of emails (comma-separated or line-separated), and FlutterFlow will automatically detect and format them for you to make it easy to invite them.
Use checkboxes to select multiple users and adjust their access levels in bulk. If the selected users have different access levels, we’ll show the options that are available to everyone (for example, you can remove access from all selected users or downgrade them to Read-only if that’s valid).
This works with search, filters, and sorting too—so you can easily find just the group you want to update.
♿ Focus Borders
We’ve added focus borders to make your apps easier to navigate with keyboards or assistive technologies.
How to use it:
Add an action to a widget
Go to the widget’s Accessibility options
Toggle Show Border on Focus
Customize the Border Width, Color, and Radius to match your design
 🛠️ Other Improvements
Wait (Delay) action now accepts variable duration. 
Added /listPartitionedFileFields endpoint to Project API to list all possible fields (not nested) for a given filename.
Updated AI Agent models to stable versions of Gemini 2.5 Pro and Flash.
Disabled WASM in Test Mode to improve reload performance.
Enhanced text scaling to automatically respect device accessibility settings when app-level scaling is at default, while maintaining priority for explicit in-app text scaling controls.
🐞 Bug Fixes
Fixed an issue where Test Mode would not display error messages on build failures.
Fixed iOS Local Run issues with Firebase App Check enforcement by enabling iOS App Check debug tokens.
Fixed an issue when deploying CORS proxy functions via Firebase.
Fixed an issue where loops within action callback parameters did not function correctly.
Fixed an issue where accessing parent loop values from a nested loop failed.
Fixed an issue where Loop over List operations failed in Action Blocks.
Fixed JSON path operations incorrectly converting Map objects to strings, which was causing crashes when trying to parse nested JSON data into custom data types.
Fixed an issue that blocked renaming of DataTables.
Fixed an issue where library page routes would not be updated correctly if the route was never overridden.
Fixed an issue with Supabase streaming where query results were not accessible in On Data Change actions.
Fixed the visibility of the 'Generate with AI' button in the page selection panel.
Fixed an issue where the first element of a RichText could not be edited.
Fixed an issue where projects would be updated even if custom files hadn’t changed.
Fixed an issue with playing asset audio on Android.
Fixed an issue with build.gradle not consistently updating when unlocked.
Fixed an issue where invalid variables could be inappropriately set.
Fixed an issue where package.json could not be edited in the Cloud Functions tab.
Fixed an issue where AppDelegate.swift changes would not reflect in exported code.
🚀ICYMI: DreamFlow
The next evolution of DreamFlow is here and available at www.dreamflow.app . DreamFlow now gives you the power to edit visually, write code, or let the agent handle changes for you. You’ll see a sharper experience that lets you:
• Start with a prompt to break the blank page
• Build visually with intuitive controls
• Refine with precision in real code
This is tri-surface development - agentic, visual, and code - built for speed, flexibility, and full control. Watch Dreamflow in action.
 🏗️ New Features We're Working On
An AI chatbot that uses context from our internal Technical Support Team to provide answers to you instantly.
MCP support
Building some exciting product updates for FFDC 2025!
Have a Technical Question or Issue?
If you need help building in FlutterFlow, you can sign up for office hours with one of our Developer Relations Team members here.
Follow-up Releases:
July 24 v6.1.12 - we have released a new version that slightly improves the speed of test mode and addresses lag in the editor. The team is still working on a long-term fix for test mode stability.
