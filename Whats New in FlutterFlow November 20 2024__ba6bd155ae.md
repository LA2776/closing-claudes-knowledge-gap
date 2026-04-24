---
title: "What's New in FlutterFlow | November 20, 2024"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow-november-20-2024-4P2kaAI1UZcJ0qP"
slug: "what-s-new-in-flutterflow-november-20-2024"
author: "Inactive Member"
createdAt: "2024-11-21T00:49:56.535Z"
publishedAt: "2024-11-21T00:49:56.669Z"
updatedAt: "2025-02-21T14:13:37.326Z"
releaseDate: "\"2024-11-20T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:54.619548Z"
---

File Download Action 
It’s easier than ever to give users the ability to download files within your app! The new File Download action allows you to specify the URL or bytes variable that should be downloaded, and gives you the ability to name the file.
You can learn more about how to use this action, and other file related actions, in the FlutterFlow documentation.
Updates to Reset Password Flow (Firebase & Supabase)
"Reset Password" action has been renamed to "Send Reset Password Email" - to better reflect its intended usage which is to send the reset password email to a user. 
In Supabase, this sends a magic link that will authenticate the current user into your app. In Firebase, this sends an email that goes to a change-password webpage hosted by Firebase.
We’ve also added a new "Update Password" action, that takes the new password as input, and updates the current authenticated user's password in either Firebase or Supabase. 
For Supabase projects, you must create a page in your app to actually handle the new password logic using this action.
For Firebase projects, you can rely on the change-password page provided by Firebase, or create your own page in your app. 
You can see details in our documentation.
onDragStarted + onDragCancel
Two new action triggers have been added for the Draggable widget - onDragStarted and onDragCancel, which are called when the draggable widget has begun to be dragged, and when a drag is interrupted. 
This allows you to build more complex draggable experiences within your app. 
Other Improvements 🛠️
Fixed some issues related to Supabase work
Fixed a few bugs related to code generation
Made some improvements to the user experience in the collaboration page
New Features We're Working On 🏗️
Improved performance for CLI, test mode and local run
Incorporating Libraries into Marketplace + Firebase into Libraries
Making every widget property dynamic
Enhanced branch merging experience
Hooks for editing native code
Fine tuning magic cursor
In-product release notes
FlutterFlow versioning
Have a Technical Question or Issue?
If you need help building in FlutterFlow, you can sign up for office hours with one of our developer relations team members here.

## Related documentation
- https://docs.flutterflow.io/concepts/file-handling/download-file
- https://docs.flutterflow.io/integrations/authentication/supabase/auth-actions/#reset-password-action
- https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/draggable/

