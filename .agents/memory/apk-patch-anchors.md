---
name: APK patch anchors
description: Reliable patching of smali recovered and rebuilt with apktool.
---

Recovered smali is reformatted by apktool during decode/build cycles, including blank lines and line-number markers. Exact multi-line replacement anchors can therefore fail on a later rebuild even when the feature is already present.

**Why:** The imported Android app is rebuilt from a decoded APK rather than maintained as source, so the injector is commonly run against both the original decode and a previously rebuilt APK.

**How to apply:** Detect an existing patch by a stable class or instruction reference, and insert new instructions relative to a unique stable call. Validate injector idempotency against the generated APK.