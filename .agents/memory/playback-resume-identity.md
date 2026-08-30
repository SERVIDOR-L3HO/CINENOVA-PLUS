---
name: Playback resume identity
description: How the recovered player identifies saved playback positions for movies and episodic content.
---

Resume positions are keyed by the player-facing title string, not by the TMDB identifier. Series entries append the season/episode label to that title, so a home resume lookup must accept the exact title and the encoded title-plus-suffix form.

**Why:** The recovered playback flow receives the title as the `id` extra when it opens the player, while episode playback adds its episode description to that same value.

**How to apply:** When adding resume-aware UI, match saved positions against the title prefix and keep the original media object so the normal stream-selection flow remains intact.