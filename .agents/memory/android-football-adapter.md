---
name: Android football adapter
description: Constraint for routing football carousel cards to the recovered player on Android.
---

The TV and Android football carousels use different click-handler classes. Matching the football media type in the TV handler does not route Android cards to playback; the Android handler needs its own direct `MediaActivity` branch.

**Why:** Android cards were being sent to the generic information activity even though their feed objects carried the correct football type and stream URL.

**How to apply:** When changing football navigation, inspect both adapter click paths and pass the same playback extras (`video`, video flag, local flag, title, referer, and origin) in each direct-player branch.