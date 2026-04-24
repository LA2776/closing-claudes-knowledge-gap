---
title: "What's New in FlutterFlow | December 11, 2024"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow-december-10-2024-jFjxNUBK6AvoEHL"
slug: "what-s-new-in-flutterflow-december-10-2024"
author: "Inactive Member"
createdAt: "2024-12-12T04:40:17.980Z"
publishedAt: "2024-12-12T04:40:18.000Z"
updatedAt: "2024-12-27T04:54:21.751Z"
releaseDate: "\"2024-12-11T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:53.782439Z"
---

Environment Specific Deployment Settings
You can now customize your deployment settings for both mobile and web based on your development environment. This allows you to deploy your web app to a unique URL (e.g., ecommerceflow-beta.flutter-flow.app) when working in your beta environment, ensuring better management of different stages of development.
Note that we plan to support setting the package name based on the environment in the next 1-2 releases.
Ability to Submit Libraries to Marketplace 🚀
You can now submit your Library Projects to FlutterFlow Marketplace! FlutterFlow Libraries allow you to share reusable resources—such as components, API calls, custom code, data types/enums, action blocks, and more—across FlutterFlow projects, with full version control.
This feature also enables you to monetize your Libraries through FlutterFlow Marketplace. With Libraries, you can create integrations with other API-driven tools, wrappers for packages on pub.dev, UI kits, and much more.
See the documentation for details on submitting to Marketplace and the criteria for getting approved.
Updates to VSCode Extension
The latest version of the FlutterFlow Visual Studio Code (VSCode) extension introduces several updates to improve your development experience. A new panel has been added to make it easier to see modified files tracked by FlutterFlow and any warnings related to syncing changes. The extension now uses Flutter Version Management (FVM) under the hood, simplifying Flutter version management across projects. We’ve also fixed several issues to enhance reliability, making the extension more stable and consistent. Additionally, the source code for the extension is now open-source, enabling the FlutterFlow community to explore, contribute, and build new IDE extensions that further improve custom code development.
The extension is available to install or update from the VSCode marketplace.
Support Like Filter in Supabase Queries
When creating a Supabase Query you can now filter data using the Like (case-insensitive) or Like (iLike) relations. This leverages the Postgres LIKE capabilities under the hood. - which allows you to match strings using wildcard patterns, where % matches any sequence of characters, and _ matches a single character. See the Supabase documentation for details.
onDataChange Action Trigger for Supabase
You can now use the OnDataChange action trigger with streaming queries in Supabase, allowing you to control app components whenever the streamed data changes. This functionality, which was already available for Firebase, has now been expanded to support Supabase.
Custom redirect URL in Supabase reset password 
When using the Send Reset Password Email action, you can now set a custom redirect URL. This allows you to specify the page the magic link will direct users to, with the flexibility to have different destinations (e.g. based on user types).
See documentation for details.
Ability to Customize When Permission Notification Shows Up
Previously, FlutterFlow would prompt users to request permission for push notifications as soon as they authenticated into your app. Now, we've added a new setting in the Push Notifications settings, giving you control over when the permission request dialog appears.
When this setting is toggled off, the permission request will be triggered only when the specific action that requires permissions is initiated, providing a more streamlined user experience.
Ability to Control Costs for Private API Cloud Functions
When deploying private APIs in FlutterFlow, cloud functions are deployed to your connected Firebase project. You can now configure the minimum and maximum number of instances used for these cloud functions.
By default, the minimum instance is set to 1, reducing latency in your app. However, you can set the minimum to 0 to better control costs while still optimizing performance.
OnDispose Action Trigger for Pages & Components
The new onDispose action trigger allows you to execute logic when a page or component is disposed of. This is particularly useful for tasks such as cancelling active streams or closing clients for SDKs, ensuring resources are properly cleaned up.
Bulk Acceptance for Merge Conflict Resolution
You can now accept all changes from either branch when resolving merge conflicts. This makes it faster and easier to resolve conflicts if, for example, you want to take all the changes from the main branch.
Other Improvements 🛠️
Fixed issue with wrong screenshot
Fixed several issues with Libraries
Fixed issues with audio recording
New Features We're Working On 🏗️
Supabase OR filter
Improved performance for CLI, test mode and local run
Incorporating Firebase into Libraries
Making every widget property dynamic
Enhanced branch merging experience
Hooks for editing native code
Fine tuning magic cursor
FlutterFlow versioning
Have a Technical Question or Issue?
If you need help building in FlutterFlow, you can sign up for office hours with one of our developer relations team members here.

## Related documentation
- https://docs.flutterflow.io/testing/dev-environments/
- https://docs.flutterflow.io/marketplace/creators-hub/submit-item-for-reivew
- https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria
- https://docs.flutterflow.io/concepts/custom-code/vscode-extension/#:~:text=The%20Visual%20Studio%20Code%20(VSCode,and%20your%20local%20development%20environment
- https://docs.flutterflow.io/integrations/authentication/supabase/auth-actions#send-reset-password-email-action
- https://docs.flutterflow.io/resources/backend-logic/rest-api/#making-an-api-call-private

