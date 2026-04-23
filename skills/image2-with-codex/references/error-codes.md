# Error codes → reporting layer

When a job fails, `job.error.code` (or the top-level `error.code` on HTTP 4xx/5xx) maps to one of five layers. Use the layer name when reporting back so the user immediately knows where the problem is.

| code                         | layer      | meaning                                                                          |
| ---------------------------- | ---------- | -------------------------------------------------------------------------------- |
| `prompt-required`            | submit     | prompt was missing or empty after trim                                           |
| `invalid-timeout-sec`        | submit     | `timeout_sec` was not a positive number                                          |
| `invalid-json`               | submit     | request body was not valid JSON                                                  |
| `request-body-too-large`     | submit     | request body exceeded 1 MiB                                                      |
| `image-not-found`            | submit     | a path in `images[]` does not exist on disk                                      |
| `service-restarted`          | queue      | the service restarted while this job was queued or running                       |
| `codex-exec-spawn-failed`    | generate   | failed to launch `codex` (binary missing, permission denied, PATH misconfigured) |
| `codex-exec-timeout`         | generate   | `codex exec` exceeded `timeout_sec` and was killed                               |
| `codex-exec-failed`          | generate   | `codex exec` exited non-zero — **usually upstream Codex capability / auth / quota**, not a local-service bug |
| `no-new-image-detected`      | generate   | `codex exec` returned zero but no new PNG appeared in `~/.codex/generated_images` |
| `artifact-copy-failed`       | persist    | generated image could not be copied to the job artifact path                     |
| `job-not-found`              | poll       | the given job id is unknown (expired, or never existed)                          |
| `internal-error`             | generate   | unclassified failure                                                             |

## How to read `codex-exec-failed`

`codex-exec-failed` is the most common confusing case. If the user sees messages like:

- `built-in image generation is unavailable`
- `image generation not enabled for this account`
- authentication / quota / rate-limit errors surfaced in `stderrPreview`

…then the **local service path is working correctly**. The failure is upstream in the user's Codex entitlement. Say so plainly instead of suggesting a retry or a different local setup.

Tell the user to check, in order:

1. Their Codex / GPT subscription and whether image generation is included
2. Remaining quota / credits
3. Whether `image_generation` is enabled for their account / environment

## How to read `no-new-image-detected`

Means `codex exec` exited cleanly but did not write a PNG to `~/.codex/generated_images`. Three usual causes:

1. Codex produced a non-PNG output (future codex version using `.webp` / `.jpg`). Worker currently only detects `.png`.
2. Codex wrote to a different path.
3. Codex "completed" without actually generating (e.g. policy refusal).

Look at `details.stdoutPreview` / `details.stderrPreview` in the error payload before guessing.
