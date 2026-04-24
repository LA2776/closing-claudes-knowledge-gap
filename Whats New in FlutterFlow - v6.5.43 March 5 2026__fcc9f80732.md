---
title: "What's New in FlutterFlow - v6.5.43 | March 5, 2026"
url: "https://community.flutterflow.io/c/whats-new-in-flutterflow/post/flutterflow-update-shader-widgets-faster-local-run-5yYATzlQzcTQVEv"
slug: "flutterflow-update-shader-widgets-faster-local-run"
author: "Manoranjan Padhy"
createdAt: "2026-03-06T08:12:41.885Z"
publishedAt: "2026-03-06T08:12:41.881Z"
updatedAt: "2026-04-16T09:21:58.326Z"
releaseDate: "\"2026-03-05T00:00:00\""
capturedAtUtc: "2026-04-24T01:05:39.013763Z"
---

Shader Widgets
Fragment shaders are the technology behind high-end visual effects in games and motion graphics. Until now, using them in a Flutter app meant writing GLSL code by hand.
Today, FlutterFlow changes that.
Two new widgets: ShaderWrapper applies an effect to any existing widget, and ShaderFill uses a shader as the fill for a widget's background. Both support implicit animations out of the box.
We shipped 26+ built-in presets, including ripple, marble, smoke, pixel, gradient noise, burn, and more, so you can get results immediately.
For full control, you can load your own custom fragment shaders.
Faster Local Run (Experimental)
We've introduced an experimental local code generation mode that runs a long-lived daemon process on your machine, cutting typical hot reload times from around 14 seconds down to 5 seconds.
This is opt-in for now. Give it a try and let us know what you think.
🏗️ Improvements
New Project Dialog redesign — Cleaner layout, better text styling, and an improved template browsing experience.
Button styling overhaul — Buttons are now consistent and polished across the entire application.
🐞 Bug Fixes
Fixed palette color code generation, outputting hardcoded hex values instead of theme references
Fixed action dialog crash caused by ProjectErrorsNotifier
Fixed enum dependency checking to include all project dependencies during code generation
Fixed asset storage rules to keep project assets publicly accessible
