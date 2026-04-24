---
title: "What's New in FlutterFlow | March 26, 2025"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/what-s-new-in-flutterflow-march-25-2025-RcodKuHRPOVGAUS"
slug: "what-s-new-in-flutterflow-march-25-2025"
author: "Inactive Member"
createdAt: "2025-03-26T17:44:06.393Z"
publishedAt: "2025-03-26T17:44:06.000Z"
updatedAt: "2025-05-20T13:26:54.444Z"
releaseDate: "\"2025-03-26T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:46.954292Z"
---

AI-Agent Builder
Build smarter apps effortlessly! Our new AI Agent Builder lets you quickly integrate powerful AI from Google, OpenAI, or Anthropic into your FlutterFlow apps—no complex setup required. Customize agents, automate interactions, and level-up your user experience instantly.
What's currently supported:
Creation of 1 AI Agent on Standard plans and unlimited AI Agents on Pro & Team Plans: You can create an AI Agent and configure its system instructions, preloaded messages, vendor, model, request type, response type, and model parameters.
3 Vendors: Google, OpenAI, and Anthropic [all of the latest models for those vendors]
How it works:
Create an AI Agent: choose your vendor+model & all the necessary parameters. If you're creating a Google agent, ensure you have Gemini API via Vertex AI turned on in your Firebase console. The Google interaction is done client side via Firebase and does not require an API key. If you're creating an OpenAI or Anthropic based agent, make sure you have a Firebase project connected with a Blaze plan that we can deploy cloud functions to call that agent with.
Use the new AI Agent action Send Message to interact with the agent: Choose the created agent and this action will allow you to pass all of the request options you specified in the cloud call or in the firebase_vertexai package call!
Use the AI Agent action Send Message response: Right now, we support text, markdown, or JSON.
Learn more in our documentation.
What's to come:
Data types as a response output
Tools & function calling
More vendors + models
Streaming
Deploy without firebase dependency
Image generation
Ability to edit platform configuration files
FlutterFlow now empowers you to customize your app’s platform configuration files for both Android and iOS—specifically AndroidManifest.xml, proguard-rules.pro, Info.plist, and Entitlements.plist. These files serve as the critical interface between your app and the operating system, declaring permissions, capabilities, and other essential settings. By editing them, you unlock new possibilities and extend FlutterFlow’s built‑in functionality.
You have two options when editing these files:
Adding “snippets”
Use Snippets to safely inject code (for example, XML entries) into predefined sections of each configuration file. This approach automatically preserves all FlutterFlow‑required settings while appending your custom code exactly where it belongs—minimizing risk and ensuring your project continues to build and run smoothly.
Editing the files manually
For advanced use cases that require altering or removing existing entries, you can unlock the file and edit it directly. While this grants full control over every line, exercise caution: modifying or deleting critical configuration elements can break your app.
For more details, see the documentation. 
Note that over the next few releases we will extend capabilities so that you can reference variables like Dev Environment Values and Library Values within these files. We’re also working on automatic imports of XML snippets from Library projects into the projects they’re imported into.
Other Improvements 🛠️
Ability to manually edit the main.dart
Fixed several issues related to Libraries
Performance enhancements for git merge
New Features We're Working On 🏗️
Support for variables in XML files
Support for XML hooks in Libraries
Supporting pages in Libraries
Custom code enhancements
UX improvements
AI enhancements

## Related documentation
- https://docs.flutterflow.io/integrations/ai-agents
- https://docs.flutterflow.io/concepts/custom-code/configuration-files

