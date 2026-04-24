---
title: "What's New in FlutterFlow | April 23, 2025"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow-april-23-2025-uoCpFa26fbKkJks"
slug: "what-s-new-in-flutterflow-april-23-2025"
author: "Inactive Member"
createdAt: "2025-04-23T16:00:23.829Z"
publishedAt: "2025-04-23T16:00:23.933Z"
updatedAt: "2025-07-11T15:11:44.552Z"
releaseDate: "\"2025-04-23T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:44.859787Z"
---

✨Improved AI-Generated Pages
Check out our improved AI page generation! It now creates multiple design versions simultaneously and intelligently selects the best result—giving you higher quality outputs with significantly fewer errors. We've already seen impressive improvements in page quality and reliability. Check out a before and after:
Try it out by opening the FlutterFlow AI Tools Panel and selecting New Page Creation.
🔁 Loop Over List Action
The new Loop Over List action lets you iterate through any list without manually tracking index variables 🙌 Plus you can set start/end indices, step size, and even looping in reverse 🙃.
To use it, click + Add Loop when defining a new action and set Loop Type to Over List. Then, you can access both the current item and its index in each iteration–perfect for cycling through products, users, or any list type that needs batch processing.
🧑‍💻 Config Snippets in Libraries
Now when you import a library that contains configuration file snippets for AndroidManifest.xml, Info.plist, or Entitlements.plist, these snippets are automatically added to your project's configuration files. Plus your project can supply its own variables (such as API keys) to include in those snippets via Library Values.
This makes libraries way more powerful and unlocks dozens of new integrations in Marketplace, such as PostHog analytics, Sentry crash reporting, CleverTap, flutter_local_notifications, flutter_nfc_kit, and much more!
🤖New Models in AI Agent Builder
We’ve added support for two cutting-edge models to the AI Agent Builder—GPT-4.1 from OpenAI and Gemini 2.5 Flash (Preview) from Google. These new additions bring faster, smarter, and more cost-effective capabilities to your AI-powered FlutterFlow apps.
⚠️ Note: AI Agent Builder currently uses OpenAI’s Assistants API, which limits access to some other new models like o4-mini and o3. We plan to support those models soon after migrating to the Responses API.
 🛠️Other Improvements
Snapshots now live under Branching, and Versions have been replaced by Commits for richer, Git‑style history. Versions can still be accessed but not created. Read more.
New “Update Text Scaling Factor” action to change global text size
Added tooltips to functions and actions that use descriptions.
Added an “On Tab Change” trigger for TabBar widgets.
Added support for optional (nullable) widget builder values
Color picker search works with hex codes as well as color names.
 🐞Bug Fixes
Library resources display the library’s name instead of its ID.
Stray tab characters in pubspec.yaml have been removed to prevent build failures.
Bumped purchases_flutter to v8.7.0, fixing an iOS 18.4+ compile‑time error.
Fixed custom action code analysis error related to streaming APIs.
Corrected CORS‑proxy detection to stop false Firebase deployment errors.
You can now delete any asset in Media Assets—the delete button always shows up.
Patched the video player by pinning wakelock_plus to a stable version.
 🏗️New Features We're Working On
A little celebration for FlutterFlow’s 4th birthday 🎂
Firebase Dynamic Links replacement
PDF support in AI Agents
Support for Pages in Libraries
Have a Technical Question or Issue?
If you need help building in FlutterFlow, you can sign up for office hours with one of our Developer Relations Team members here.
