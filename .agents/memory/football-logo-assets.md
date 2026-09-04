---
name: Football logo assets
description: Recovered APKs may need bundled football competition or country logos for TV image reliability.
---

The TV carousel can fall back to its generic placeholder even when the same remote football logo loads on Android. Bundling transparent, normalized copies of the known API logos gives both modes consistent rendering.

**Why:** The recovered app uses an asynchronous image loader whose TV path did not reliably display the remote `logoUrl`, while the feed only provides one country or competition logo rather than individual team crests.

**How to apply:** Keep local-logo selection keyed to the API URL with a remote fallback for new URLs, and preserve transparent assets at a sufficiently large intrinsic size for `CENTER_INSIDE`.