---
name: Football playback error path
description: Constraint for the recovered ExoPlayer error callback used by football streams.
---

The football launch path supplies a direct stream URL and does not populate the generic movie `WebResult` object. A shared ExoPlayer error handler must not assume that object exists when attempting alternate-server recovery.

**Why:** A failed football stream reached the generic retry branch, which dereferenced the absent movie metadata and caused the player activity to crash instead of showing an error.

**How to apply:** Null-check the movie metadata before generic retry logic; for direct football streams, keep the activity alive and show the playback error state rather than attempting movie-specific recovery.