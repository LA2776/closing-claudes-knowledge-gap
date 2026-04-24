---
title: "What's New in FlutterFlow | July 8, 2025"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow-july-8-2025-PUQpPy0e4ihwEbb"
slug: "what-s-new-in-flutterflow-july-8-2025"
author: "Inactive Member"
createdAt: "2025-07-08T19:45:00.181Z"
publishedAt: "2025-07-08T19:45:00.341Z"
updatedAt: "2025-09-12T09:55:23.447Z"
releaseDate: "\"2025-07-08T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:43.082367Z"
---

⬆️ Flutter 3.32.4 Upgrade
We’ve upgraded the underlying Flutter version to 3.32.4. This release includes some significant updates to Flutter itself, plus updates to dozens of third-party packages used across FlutterFlow. You’ll find the full list (plus additional packages that may require action) in our migration guide.
Most projects will continue to work as expected, but you may need to make changes to custom code or dependencies—especially if you rely on web rendering or older Android embedding. If you run into issues with custom dependencies, check out our video on How to Resolve Dependency Issues.
We’ve also added an experimental toggle in Web Deploy settings to use --wasm when building and deploying web apps, which can result in better performance.
🏗️Edit AppDelegate.swift and build.gradle
You can now directly modify build.gradle (Android) and AppDelegate.swift (iOS) files inside FlutterFlow! This unlocks powerful integrations that require native configuration—like manually registering custom plugins, tweaking SDK versions, or adding build-time dependencies. These files join other configuration files FlutterFlow exposes directly, including main.dart and AndroidManifest.xml.
Whether you're adding an SDK initialization call in AppDelegate.swift or enabling MultiDex in build.gradle, you can do it all without leaving FlutterFlow. Learn more by checking out the docs. 
📚Custom Classes in Libraries
Your custom classes can now be shared across multiple projects through Libraries! Create reusable data models, business logic, and enums in a library project and import them anywhere. Whether you're building a UserProfile class for your authentication library or a Product class for your e-commerce components, these classes and their methods will automatically become available in any project that imports your library.
This is a game-changer for teams working on multiple apps—no more recreating the same data structures across different projects. Your custom classes are now as shareable and version-controlled as your components and API calls, making it easier than ever to build scalable, maintainable Flutter applications.
 🛠️Other Improvements
Double clicking on a text element (Text, RichText) now focuses the value input box
Refreshed available devices in the canvas (includes iPhone 16, Pixel 9, + more)
Added the ability to search, sort, and filter project members in Collaboration settings
Updated Project API documentation, including support for new /listProjects endpoint
Custom Code Expressions now support AI prompts with full access to your project variables
Added Show Border on Focus toggle in Accessibility options for widgets to enable visual highlights when widgets are focused via keyboard
Updated AI Agents to use OpenAI’s Responses API and upgraded Google models to stable versions of Gemini 2.5 Pro and Gemini 2.5 Flash
Improved the rename branch flow to make the operation more intentional
Improved the loading time for listing projects in the dashboard
Improved the accuracy and reliability of AI generated components from images
When importing pages from libraries, we now auto-resolve route conflicts like homePage_${dependencyProjectId}
Improved the loading UX for generating and loading FlutterFlow CLI commands
It’s no longer possible create new TEMPLATE types on Marketplace (prefer LIBRARY)
 🐞Bug Fixes
Fixed some pixel overflow issues in the property panel
Fixed an issue where Loop through list would not work as expected in Action Blocks
Fixed an issue where selecting actions of different loop types (e.g. a Loop over List…and then a While Loop) would not update the type toggle in the action editor
Fixed an issue where loop values could not be used in a conditional action
Fixed an issue where commits list showed a grey screen when creating a new branch
Fixed an issue where custom code expressions did not display emojis correctly
Fixed an issue where builds failed for projects with dependencies
Fixed an issue where API variables did not correctly reference default values
Fixed an issue where analyzer would load infinitely when toggling back and forth between viewing code and the builder. Viewing code now opens a new tab
Fixed an issue where “Custom Functions need to be checked for errors” shows up too frequently
Fixed an issue where library page route overrides could be empty / non-editable when viewing library details
Fixed an issue where FlutterFlow Windows desktop app could crash when loading custom code (or other webviews)
Fixed an issue where unpaginated data tables would not refresh when new data was added
Fixed an issue where deleted action library values might show a duplicate value error
Fixed an issue where opening the library details for one dependency reset the library values of all other dependencies
Fixed an issue where auth actions were not checked for errors in action blocks or callback actions
Fixed an issue that prevented projects from being deleted in some cases from the dashboard
Fixed an issue where existing branches were not visible under the Branch Level Access section in the Collaboration tab
 🏗️New Features We're Working On
Finalizing MCP support!
Bulk import pages and components from Figma
Performance improvements
Have a Technical Question or Issue?
If you need help building in FlutterFlow, you can sign up for office hours with one of our Developer Relations Team members here.

## Related documentation
- https://docs.flutterflow.io/concepts/custom-code/configuration-files/
- https://docs.flutterflow.io/concepts/custom-code/code-file/
- https://docs.flutterflow.io/resources/projects/settings/project-apis/

