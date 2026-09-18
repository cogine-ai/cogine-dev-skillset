---
name: ui-proof-video
description: "Record, review, or visibly play owner-facing UI proof videos for Codex tasks. Use when a worker wants to show a dynamic or multi-step browser flow, when a local WebM proof must be checked, or when the owner asks to play the video. Video is optional review media, separate from browser-verify and ui-proof-screenshot."
---

# UI Proof Video

Handle optional owner-facing video evidence. The assigned worker or Root invokes this skill directly; it is independent of `fresh-eyes` and is not a strict acceptance gate unless the owner explicitly makes it one.

## Modes

### Record

- Record the real UI flow with Playwright `recordVideo` or an available screencast API.
- Use practical boundaries: start shortly before the relevant action when the page is ready, and stop after the result is clearly visible.
- Setup, waits, cleanup, shortening, or split segments may be included or omitted as useful. State accurately what the recording covers.
- Do not record secrets or sensitive account data.
- Save as WebM under `/tmp`, an ignored `.tmp/proof`, or another owner-approved local evidence directory. Keep it out of Git.

### Review

- Confirm the file exists and can be decoded by a browser.
- Play it in the Codex in-app Browser in the background and inspect the relevant sequence/result.
- If direct WebM navigation is blocked, serve the file temporarily on `127.0.0.1` through a minimal local HTML video player. Stop the server and delete the temporary player after review.
- Compare the recording with the current candidate state. If code changed after recording and affects the shown behavior, mark the video `STALE`.

### Show

- Use the same local playback path as Review, but set the in-app Browser visibility to true so the owner can watch.
- Play from the beginning unless the owner asks for a specific segment.
- Keep playback controls visible when useful. Clean up the temporary server/player after playback unless the owner asks to keep it open.

## Return

Report:

- absolute video path;
- duration and resolution when available;
- what the video shows;
- whether it matches the current candidate;
- one media status: `PLAYABLE`, `STALE`, `INCOMPLETE`, or `UNPLAYABLE`.

Video does not replace required screenshots, browser functional checks, console/network evidence, runtime logs, or cleanup readback.
