---
name: APK build tools
description: Environment-specific signing and verification constraints for recovered Android APK rebuilds.
---

The runner can include Apktool, keytool, and jarsigner without providing the Android SDK `apksigner` or `zipalign` binaries. A rebuilt APK can still be signed and checked with the available Java JAR-signing path, but device validation remains important because this does not provide the full modern APK Signature Scheme toolchain.

**Why:** The imported project is an APK reconstruction rather than a normal Gradle project, and the available Nix packages do not guarantee the Android build-tools binaries.

**How to apply:** Check for `apksigner` and `zipalign` before signing. If they are unavailable, use an ephemeral recovery keystore with `jarsigner`, verify the ZIP and JAR signature, and clearly flag physical-device installation as the remaining validation.