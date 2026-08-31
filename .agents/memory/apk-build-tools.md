---
name: APK build tools
description: Environment-specific signing and verification constraints for recovered Android APK rebuilds.
---

The runner can lack the Android SDK `apksigner` and `zipalign` binaries. Adding the `jdk` system dependency provides `keytool` and `jarsigner`, allowing a rebuilt APK to be signed and checked with the available Java JAR-signing path; device validation remains important because this is not the full modern APK Signature Scheme toolchain.

**Why:** The imported project is an APK reconstruction rather than a normal Gradle project, and the available Nix packages do not guarantee the Android build-tools binaries.

**How to apply:** Check for `apksigner` and `zipalign` before signing. If they are unavailable, use an ephemeral recovery keystore with `jarsigner`, verify the ZIP and JAR signature, and clearly flag physical-device installation as the remaining validation.