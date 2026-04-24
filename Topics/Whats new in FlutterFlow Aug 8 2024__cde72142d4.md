---
title: "What's new in FlutterFlow | Aug 8, 2024"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow-aug-8-2024-DswYx4kOD9LlUYI"
slug: "what-s-new-in-flutterflow-aug-8-2024"
author: "Inactive Member"
createdAt: "2024-08-08T16:48:53.873Z"
publishedAt: "2024-08-08T16:48:54.000Z"
updatedAt: "2024-09-18T08:45:56.464Z"
releaseDate: "\"2024-08-08T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:59.352395Z"
---

We're happy to share the latest feature updates! Explore more powerful live previews, renaming data types, and other improvements!
More Powerful Live Previews
Having live previews directly in the builder is one of the things that makes FlutterFlow so powerful. So, we’re continuing to make the preview more powerful by rendering constant values for some widget properties. 
If you use constants for padding or your border radius, you can now see how those values will look directly in the preview. This allows you to consistent values across your app - simply create the padding constants, and leverage those constants within padding properties.
The same goes for leveraging responsive values in size and width properties. You can set the size and width for containers to respond to your screen size and width, and see those changes directly in the preview builder. We’re working on item spacing next!
Renaming Custom Data Types & Enums
Want to change the name of your Custom Data Type or Enum? Well, now you can! Simply edit the name and you’re good to go! No more manual refactoring 🙂
And in case you didn’t know, you could already rename the fields in Custom Data Types by double clicking!
Ability to Toggle Debug Mode off for Local Run & Test Mode
We recently made the Debug Panel available both in Test Mode and for Local Run. While this is great for debugging, it can have some performance implications. 
So, over the past week we’ve added toggles to turn off the debug logging to get a better sense for your app’s performance when it will be released to your customers. 
To turn off debug logging for test mode sessions you can click the three dots menu next to Debug Panel while in a test mode session.
To turn it off for local run, you can edit the Code Export settings in the Local Run Configuration Menu.
Comparing Entire Branch History in Merge
We’ve made some changes to our merging logic so that the entire branch history is considered during merges. This means that you may need to resolve the same conflict more than once. We did this to better ensure that you can understand and trust what changes are applied during a merge. We recommend that you keep branch histories short - so create a branch, make your change, merge it back into main and then delete it - for increased stability.
We know there have been ongoing issues with branching and we’re committed to making this a great experience for all users. We’ll be investing more in the coming weeks.
Other Improvements 🛠️
Debug panel performance enhancements
Fixed some syncing issues
Focused on over product health and stability
Fixed several issues related to branching
New Features We're Working On 🏗️
Branching & version control
Support for more action triggers
Overall user experience
Sharing resources across FlutterFlow projects
