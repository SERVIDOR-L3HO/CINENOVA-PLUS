---
name: Android and TV football feeds
description: Durable distinction between the Android and TV home-fragment data paths for APK reconstruction.
---

Android and TV are separate home-fragment flows and cannot share an updater that assumes the TV fragment type. The Android path must insert its `CustomList` into its own list and rebuild its own adapter.

**Why:** The TV feed can appear correctly while Android remains unchanged when the injection is attached only to the TV fragment.

**How to apply:** When changing the football feature, validate both fragment paths independently and keep the TV behavior intact while adding the Android update.