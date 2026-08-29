---
name: APK signing continuity
description: Imported APKs may contain only the public certificate, not the private keystore needed for update-compatible rebuilds.
---

The imported CINENOVA APK includes a self-signed recovery certificate but no private signing keystore in the project or runner. Any rebuilt APK must be signed with a new key unless the owner supplies the original private key, so Android will treat it as a fresh installation rather than an update.

**Why:** APK signatures cannot be reproduced from the embedded public certificate; reusing the certificate name does not preserve installation compatibility.

**How to apply:** Before future APK edits, look for the original private keystore and compare certificate fingerprints. If it is unavailable, warn that the rebuilt APK cannot overwrite the currently installed one.