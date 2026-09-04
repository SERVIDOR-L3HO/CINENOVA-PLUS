---
name: Android football adapter
description: Constraint for routing football carousel cards to the recovered player on Android.
---

The TV and Android football carousels use different click-handler classes. The Android home-screen carousel has its own handler in addition to the secondary list adapters; each handler needs its own direct `MediaActivity` branch for the football media type.

**Why:** Android home-screen cards were being sent to the generic information activity even though their feed objects carried the correct football type and stream URL. Patching only a secondary Android adapter did not affect that screen.

**How to apply:** When changing football navigation, inspect the home-screen carousel path and the secondary list path, then pass the same playback extras (`video`, video flag, local flag, title, referer, and origin) in each direct-player branch.