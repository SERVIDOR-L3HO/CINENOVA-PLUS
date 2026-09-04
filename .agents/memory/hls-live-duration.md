---
name: HLS live duration guard
description: Why recovered playback code must not reject short sliding HLS windows as invalid videos.
---

Live HLS playlists commonly report only their current sliding segment window rather than a long fixed duration. A generic “short video” validation can therefore stop a healthy live stream and show the playback error dialog.

**Why:** The recovered player used a duration range below five minutes as an error condition, while the provider’s live playlist exposes a much shorter rolling window.

**How to apply:** Exclude known live HLS sources from fixed-duration sanity checks, while retaining the check for ordinary on-demand sources unless the product behavior explicitly changes.