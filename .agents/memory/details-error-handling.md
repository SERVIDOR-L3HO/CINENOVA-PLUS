---
name: Details error handling
description: Runtime behavior to preserve when movie metadata requests fail in the recovered Android app.
---

Metadata requests can fail because the API is unavailable or returns incomplete JSON. Treat that as an in-screen error state: show the existing connection warning and keep the movie details activity open.

**Why:** The recovered app explicitly finished both details activities from their metadata error callbacks, so a normal network/API failure looked like a navigation bug and returned the user to the home screen.

**How to apply:** When patching or regenerating the smali overlay, preserve the details activity on both request failure and metadata parsing failure paths; use stable smali instructions and labels as anchors.