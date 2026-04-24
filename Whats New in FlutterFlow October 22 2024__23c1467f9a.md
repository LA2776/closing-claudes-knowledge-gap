---
title: "What's New in FlutterFlow | October 22, 2024"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow-october-22-2024-SwPJhrzf93cjCkp"
slug: "what-s-new-in-flutterflow-october-22-2024"
author: "Inactive Member"
createdAt: "2024-10-22T16:11:58.219Z"
publishedAt: "2024-10-22T16:11:58.000Z"
updatedAt: "2024-12-06T13:51:03.001Z"
releaseDate: "\"2024-10-22T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:55.972623Z"
---

Flutter 3.24 + Packages Upgrade
Today’s release of FlutterFlow includes upgrading the underlying Flutter version from 3.22.2 to 3.24.2. We also upgraded the version of several third party packages we depend on. 
When we upgrade underlying dependencies, you may need to modify your custom code to ensure you’re using the most up-to-date pieces of the underlying Flutter framework or packages. 
We’ve compiled a list of breaking changes that might affect your custom code, as well as a list of the exact packages and version upgrades, in this migration guide here. 
We also recommend that you watch our video on How to Resolve Dependency Errors in case you run into conflicts with these upgrades.
Flex Widget
The new Flex widget can be used as an alternative to Row and Column. It allows you to dynamically set the layout axis (horizontal or vertical) based on specific conditions or logic. 
This is especially useful for creative responsive layouts - where child elements should be horizontal when the screen is wide, and vertical when the screen is narrow. 
Trailing Icons for Button
Now when adding an icon to the Button widget, you can select if it should be Leading or Trailing the label. 
Environment Tag in CLI
You can now pull the code for a specific environment using the --project-environment tag in the CLI. This is particularly useful when you need to retrieve code for a specific environment, apply local changes, and deploy to distinct testing or production hosting environments. For further details, check the CLI documentation.
Library Values
Library Values allow library users to pass in certain values to be used within the Library project. For example, a Library developer may create a Library Value that will hold an API key. The developer can reference this value just like any other variable within FlutterFlow. When a user of the Library imports it into their project, they are prompted to set a string value. See the documentation on libraries for more details.
Deprecation of Team Libraries 
Team code and API libraries are now deprecated, meaning you cannot create new team libraries or add import resources from existing team libraries within projects. Instead, we recommend using Libraries to centralize custom code, API calls, components, data types, and more in a place where they can easily be version controlled and reused by your team. 
In the next few releases we will work on tooling to help migrate existing team libraries to Libraries.
Other Improvements 🛠️
Added a new setting to VSCode extension that makes available for different FlutterFlow instances (i.e. beta, enterprise)
Made error messages more clear for VSCode extension
Fixed various issues related to Action Flow Editor
Fixed some issues related to Libraries
Resolved various bugs from GitHub tracker 
New Features We're Working On 🏗️
Enhanced Supabase integration
Incorporating Libraries into Marketplace
Making every widget property dynamic
Enhanced branch merging experience
Hooks for editing native code
Fine tuning magic cursor
Have a Technical Question or Issue?
If you need help building in FlutterFlow, can sign up for office hours with one of our developer relations team members here.

## Related documentation
- https://docs.flutterflow.io/testing/dev-environments/#:~:text=Development%20Environments%20in%20FlutterFlow%20allow,environment%2Dspecific%20values%20and%20databases
- https://docs.flutterflow.io/exporting/ff-cli/
- https://docs.flutterflow.io/resources/projects/libraries/

