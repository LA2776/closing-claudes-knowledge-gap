---
title: "What's New in FlutterFlow | November 13, 2024"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow-november-13-2024-Vba3bZ8awZmgRTV"
slug: "what-s-new-in-flutterflow-november-13-2024"
author: "Inactive Member"
createdAt: "2024-11-13T22:59:14.955Z"
publishedAt: "2024-11-13T22:59:15.225Z"
updatedAt: "2026-03-17T07:42:21.053Z"
releaseDate: "\"2024-11-13T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:54.773745Z"
---

Supabase Package Upgrade
We've upgraded the Supabase package in FlutterFlow (supabase_flutter) from version 1.10.24 to 2.6.0. This update will make it easier for us to support the latest Supabase capabilities on the FlutterFlow platform and provides you the option to incorporate new features through custom code.
Please note, moving to Supabase v2 includes several breaking changes. To ease the transition, you can continue using the previous version of supabase_flutter for the next 4 weeks. If this applies to you, you’ll see an option to upgrade by toggling off “Use Supabase v1” in the Supabase settings page.
However, in 4 weeks from now, all FlutterFlow projects will use supabase_flutter 2.6.0. This means if you have custom code using Supabase v1, your project likely will have errors when this change goes into effect. 
Also note that you will not be able to use test mode while you stay on Supabase v1. Instead, we recommend using local run. You will also not have access to the new Supabase features until you toggle off “Use Supabase v1”.
You can see Supabase’s migration guide for help migrating your custom code.
Supabase Streaming Queries
You can now enable real-time streaming for your Supabase queries. 
Just switch off the "Single Time Query" toggle when setting up a Supabase Query to stream results in real-time.
 Apple Authentication for Supabase
You can now add Apple Authentication to your app when using Supabase, alongside Email Authentication and Google Sign-In. 
This not only enhances your app's sign-in options but also ensures compliance with Apple’s App Store guidelines, which require Apple Sign-In wherever Google Sign-In is offered.
See the setup instructions for details. 
Search in App Settings
We’ve added search to the App Settings page, a simple but useful way to make it easier to navigate through the various project-level settings within FlutterFlow.
Improved Dependency Page
In a recent update, we introduced the Project Dependencies page, enabling you to add FlutterFlow Library projects as dependencies and view Dart package dependencies. 
Now, we’ve expanded this functionality to make the page even more useful. With the latest FlutterFlow version, you can add custom pub dependencies (Dart packages) to your app or adjust the versions of existing dependencies. Plus, FlutterFlow now provides helpful error messages to prevent dependency conflicts.
The goal is to give you a centralized place to view all project dependencies and take any actions necessary to successfully build and run your project. 
You’ll also notice that when you add custom pub dependencies in this page or in the custom code editor, you’ll see the same dependencies shown on each custom code resource. 
For example, you may have added your dependency to use in a Custom Widget. However, it will still show as a dependency in your Custom Actions. This is because dependencies are added at the project level. 
Note that dependency errors and warnings are now also surfaced in the custom code editor. 
Team Library Migration Tool
We’ve released a migration tool to help you migrate Team Libraries (custom code libraries, API libraries and components within Team Design Systems) to Library projects. 
You can see the guide for how to migrate Team Libraries to Library projects here.
Note that it is advised to commit changes in your projects before doing the migration so it’s easy to revert any unexpected modifications. 
A Note on Firebase Store Changes
Last month, Firebase made some modifications to Cloud Storage for Firebase. You now need to be on a Blaze pay-as-you-go plan to use Cloud Storage. Note that no-cost usage is still available, even on the Blaze pan. 
This means that you may need to change your plan to continue using some FlutterFlow features that use Cloud Storage behind the scenes. For example, the File Upload action and the Upload Signature action.
Other Improvements 🛠️
Enhanced testing and QA process, aiming to reduce bugs and regressions
Ability to specify image file type in the image widget - allows you to more reliably support SVG images by selecting SVG type
Fixed issues with setting the cursor position 
Fixed some bugs related to Libraries
New Features We're Working On 🏗️
Incorporating Libraries into Marketplace
Making every widget property dynamic
Enhanced branch merging experience
Hooks for editing native code
Fine tuning magic cursor
In-product release notes
FlutterFlow versioning
Have a Technical Question or Issue?
If you need help building in FlutterFlow, you can sign up for office hours with one of our developer relations team members here.
