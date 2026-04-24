---
title: "What's New in FlutterFlow | May 13, 2025"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow-may-13-2025-vDTjmMJA2cNiIlm"
slug: "what-s-new-in-flutterflow-may-13-2025"
author: "Inactive Member"
createdAt: "2025-05-13T21:07:17.039Z"
publishedAt: "2025-05-13T21:07:17.299Z"
updatedAt: "2025-07-11T15:11:07.283Z"
releaseDate: "\"2025-05-13T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:44.601399Z"
---

🎉 Heads up! The FlutterFlow team is hard at work preparing something big for our 4th birthday—and we’d love to show you! Join us live on May 28!
📚 Custom Code References
We’ve added a new feature to help keep your codebase clean and efficient. Now available on all projects (off by default), this tool highlights custom functions, actions, and widgets that aren’t being used — so you can safely remove them.
You’ll also see a full list of where each piece of custom code is being used in the right side panel. Just click to jump straight to the reference in the builder.
To get started, toggle the tool on in the Custom Code toolbar. You’ll see warnings for unused code and reference lists for everything else. Time to tidy up!
🔗 Introducing Branch Deeplinking Library
We're launching a complete replacement for Firebase Dynamic Links through our new Branch.io integration! Since Firebase is sunsetting Dynamic Links in 2025, we've created a new library that:
Automatically adds all required native code configs
Handles incoming deeplinks with custom navigation logic
Supports link generation right from your app
Includes helper functions to extract data from links
You'll find it in Marketplace completely free here and the documentation here.
🔥 Firebase and Supabase in DreamFlow
We're thrilled to announce integrations with both Firebase and Supabase in DreamFlow! Now you can build apps with powerful backend services in just a few clicks.
🔥Firebase: Connect your Google account to instantly provision a Firebase project with authentication, database setup, schema configuration, and security rules—all automatically deployed for you.
⚡Supabase: leverage PostgreSQL database capabilities with the same seamless experience.
To get started, select either Firebase or Supabase when starting a new project or in an existing project, authorize access, and DreamFlow will handle the rest—no manual configuration required! This is just one more way we're making it easier to turn your app ideas into reality. Try it out here.
🛠️ Other Improvements
Better search throughout the product with improved result ranking. You should notice a significant difference on widget search (added “Top Results”), custom code, or API call searches.
Improved variable validation messages to be more specific instead of "Current variable is invalid".
You can now pass PDF documents to your Google and Anthropic AI Agents.
You can include or drop pending changes when creating a new branch.
You can create Firestore queries with multiple IN conditions.
Importing a Figma theme now uses OAuth for simplified connecting.
Branching performance improvements (4x merge speedup in large projects).
Added support for internal application tags in the Android Manifest. This lets you add components like services, broadcast receivers, and additional activities without having to unlock the entire manifest file.
🐞 Bug Fixes
Fixed an issue where some icons were not appearing in Run and Test modes.
Improved date formatting in some places to show the year when it's not the current year.
Fixed an issue where snackbars in the builder would prevent interaction in the surrounding area.
You can now properly clear the Start, End, or Step values in Loop Over List actions and use the reverse option correctly.
Allow moving actions inside a loop action. 
Fixed some text encoding issues for non-English languages.
Fixed an issue with library version history selection.
Fixed AI Agent’s “Clear Chat History” in action blocks and better handling for empty multimodal input.
Fixed an issue where Theme values could disappear after a branch merge.
 🏗️New Features We're Working On
Join us live on May 28 to celebrate FlutterFlow’s 4th birthday with some powerful new features! 🎂
Have a Technical Question or Issue?
If you need help building in FlutterFlow, you can sign up for office hours with one of our Developer Relations Team members here.

## Related documentation
- https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking/#branch-deeplinking-library

