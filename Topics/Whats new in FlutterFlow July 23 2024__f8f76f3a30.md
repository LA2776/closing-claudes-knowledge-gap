---
title: "What's new in FlutterFlow | July 23, 2024"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow-july-23-2024-7HGIjexBaWdwKQQ"
slug: "what-s-new-in-flutterflow-july-23-2024"
author: "Inactive Member"
createdAt: "2024-07-25T20:13:37.144Z"
publishedAt: "2024-07-25T20:13:37.000Z"
updatedAt: "2024-08-31T11:51:20.970Z"
releaseDate: "\"2024-07-23T00:00:00\""
capturedAtUtc: "2026-04-24T01:06:00.281207Z"
---

We're happy to share a host of new features this update! Explore page and component descriptions, control minimum version for iOS and minSDK for Android, scrolling lists in descending order, and more. 
Page and Component Descriptions 
We're on a mission to add metadata that brings clarity and context to your projects. We already support documentation at the widget or action level. Now, we’re excited to launch Page and Component descriptions.
You can add a description to a new or existing Page or Component that describes what the element does and how it can be used. 
You'll see the descriptions added as Dart documentation comments in the generated code, which means that if you’re leveraging these classes in a Flutter-supported IDE then you can hover over the class name and see your description in the tooltip.
Over the next few months we’ll continue to add metadata that will not only make it easier for collaborators to leverage what you’ve built, but also make it easier to search and find what you’re looking for.
Control Minimum Version for iOS and minSDK for Android 
Sometimes you want to use a package that leverages newer Android or iOS APIs. Many times, these packages require a minimum iOS version, or minimum Android SDK version.
Previously, you would see an error like
“The plugin …. requires a higher Android SDK version” - and you would need to modify the native code after building the app.
But now, we’ve added the ability to control both the minimum iOS version and minimum Android SDK version from the Platform page in App Settings.
Sorting Lists in Descending Order 
Not everyone wants to sort a list in ascending order, so now you can sort lists descending as well!
Leverage Debug Panel (Flutter Devtools Extension) outside of FlutterFlow 
As mentioned above, we’ve added support for the Debug Panel to local run through a Devtools Extension. But, sometimes you want to run your app totally outside of FlutterFlow. Most of the time, you’ll use the FlutterFlow CLI to download the code and run as you please using Flutter and Dart tooling. So, we’ve added a flag to the CLI that allows you to pull down debugging code. This debugging code adds logging in the generated code that supports the debug panel, and 
Simply run the CLI command below and run as you normally would. 
flutterflow export-code --as-debug …
You can access the debug panel by opening Flutter Devtools.
Other Improvements 
Fixed issues with network connection
Localization fixes
Please visit the Official FlutterFlow Issue Tracker for the most up to date status of all reported bugs and fixes.
New Features We're Working On
Making the builder UI more powerful
Branching improvements
Performance improvements
Support for more action triggers
