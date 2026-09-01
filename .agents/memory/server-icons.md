---
name: Transparent Android server icons
description: Rasterization constraint for custom PNG assets used in the recovered Android APK.
---

Custom SVG assets must pass `-background none` before the SVG input when rasterized with ImageMagick; placing it after the input can produce an opaque white canvas that appears as a white square in Android ImageViews.

**Why:** The Android server cards display these assets at small sizes, so an opaque canvas is immediately visible and makes otherwise clean artwork look broken.

**How to apply:** Keep the icon generator's alpha check on a corner pixel, and verify the decoded APK assets after every rebuild.