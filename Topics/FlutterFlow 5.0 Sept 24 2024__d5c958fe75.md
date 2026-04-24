---
title: "FlutterFlow 5.0 | Sept 24, 2024"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/flutterflow-5-0-sept-24-2024-2yab7mYWtddLIwh"
slug: "flutterflow-5-0-sept-24-2024"
author: "Inactive Member"
createdAt: "2024-09-24T21:41:10.729Z"
publishedAt: "2024-09-24T21:41:10.000Z"
updatedAt: "2024-11-06T23:00:57.221Z"
releaseDate: "\"2024-09-24T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:59.203493Z"
---

Last week at FFDC we showed some of the new features we’ve been working on, including many of the new features we’re launching today as part of FlutterFlow 5.0. 
We’re super excited about these new capabilities and look forward to hearing your feedback! 
Development Environments
You can now set up multiple “environments” for your app, such as development, staging, and production. 
In each development environment, you can specify different Environment Values for setting things like API URLs, keys, and more. This way, you can test out new features in your app without affecting production data.
For more details on how to use Development Environments, see the documentation.
New Gesture Detector Action Triggers
We’ve added support for 50+ new action triggers, to allow you to make more interactive and responsive user interfaces. These triggers allow you to respond to things like drag, pan, and scale interactions in your app. 
You’ll notice these triggers when you add a new action to a container widget. Additionally, you’ll be able to leverage the Gesture Detector data - like the coordinates of the drag interaction – within your action flows. 
This opens the door to so many possibilities. For some inspiration, check out the FFDC keynote where we featured some great examples - including the custom sliders shown below.
Listen for Keyboard Press Events
Many of you are building web apps in FlutterFlow, which means pointer gestures aren’t the only way users can interact with your screens. So, we’re also excited to launch keyboard shortcuts.
Now, you can create action triggers that listen for key presses at the Page and Component levels.
Widget Builder as Parameter
As you may have noticed over our last few releases, we’ve been on a mission to make Components more powerful. In FlutterFlow 5.0 we’ve taken this even further. Now, when you create a Component, you can add a parameter that’s of type Widget Builder. 
This allows you to dynamically substitute in widgets on your Component’s widget tree. For example, specifying custom input fields in the design shown below:
You can see some examples of just how powerful this feature is by looking at our documentation and watching the FFDC talks.
Libraries
You can now create and publish libraries in FlutterFlow with resources that you can then import into multiple other FlutterFlow projects. This allows you to reuse components, API calls, custom code, and more - all with version control. By using libraries, development becomes more efficient and scalable.
You can now create and publish libraries in FlutterFlow with resources that you can then import into multiple other FlutterFlow projects. This allows you to reuse components, API calls, custom code, and more - all with version control. By using libraries, development becomes more efficient and scalable.
To create a Library, build resources as you normally would, then head to your App Settings and check out the new Publish as a Library page. 
To import resources from a Library, add the Library Project as a dependency in the Project Dependencies page in your App Settings. 
Beyond sharing resources with your team, Libraries let you share UI Kits and integrations with the broader FlutterFlow community. Check out Adapty, who built a FlutterFlow plugin, as an example. We’ll be sharing more details soon!
To learn more about how to publish and import libraries, see the documentation. 
Branch Commits
A commit is essentially a named snapshot of your project at a particular point in time. When you make changes to your project (such as adding new widgets, modifying actions, or configuring integrations), you can create a commit to save these changes. Each commit stores a record of what has been modified and serves as the version history for your branch, making it easy to see what has changed and roll back to previous versions if needed.
Other Improvements 🛠️
Fixed issue with Xcode 16
Fixed issue with Google Sign In on Windows
Fixed issue with animation delay & duration
API variables can be set from App State variables and Constants
Improved UI for seeing the Component definition from the Widget Property Panel
Added ability to search for data types and enums throughout the product
New Features We're Working On 🏗️
AI tooling 
At FFDC we demoed some of the exciting new AI features we’ve been working on. We’ll be rolling out Page Autocomplete, Sketch to Component, and Enhanced Page Gen as soon as possible. We’re still putting the finishing touches on Magic Cursor, so join the wait list if you want to be a part of our early access group.
Other features we’re working on
VSCode Extension
Enhanced Supabase integration
Incorporating Libraries into Marketplace
Supporting Development Environments in integrations
Making every widget property dynamic
Improved performance
Enhanced branch merging experience

## Related documentation
- https://docs.flutterflow.io/testing/dev-environments
- https://docs.flutterflow.io/resources/functions/action-triggers#gesture-detector-triggers
- https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#on-shortcut-press-action-trigger
- https://docs.flutterflow.io/resources/ui/components/widget-builder
- https://docs.flutterflow.io/resources/projects/libraries

