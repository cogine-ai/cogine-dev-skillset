---
name: image2-with-codex
description: Route image generation to the local image2-with-codex HTTP service at http://127.0.0.1:4312, which delegates to the user's Codex CLI. Use only when the user explicitly asks for this route. Default behavior is raw prompt pass-through; do not substitute HTML layout, infographic tooling, or other image tools.
---

# image2-with-codex

You are the boundary guard for the local Codex CLI image-generation pipeline. Recognize the request, execute faithfully, deliver the image. Do not invent a smarter substitute.

## When to trigger

Trigger when the user explicitly asks for this pipeline. Typical phrases:

- "use image2 with codex" / "send this to image2 with codex"
- "use the local codex image service" / "don't use other tools, use local image service"
- "use GPT Image 2" when paired with *local*, *codex*, or *image2-with-codex*
- Chinese: "用本地 codex 画图"、"走 image2 with codex"、"调本地图像服务"
- or when the current conversation already established that this request goes through this service

Do **not** trigger on bare "Image 2" / "image2" / "图 2" without a *local* / *codex* / *service* qualifier. Those overlap with unrelated usage.

## How to execute

1. **Verify the service is up.** `GET http://127.0.0.1:4312/health`.
   - `ok: true` (HTTP 200) → continue.
   - `ok: false` (HTTP 503) → report which `checks[]` entry failed and stop. Do not silently fall back to another tool. See `references/api.md` for the checks → remediation table.
   - Connection refused / port closed → the local service isn't installed or isn't running. **Do not fall back to other tools.** Instead guide the user through the install (see "Installing the service" below), then retry.

2. **Submit the job.** `POST http://127.0.0.1:4312/v1/images/generations` with:
   ```json
   {
     "prompt": "<user prompt, unmodified>",
     "images": ["<absolute path to reference image>", "..."],
     "timeout_sec": 180
   }
   ```
   Returns HTTP 202 and `{ ok: true, job: { id, status: "queued", ... } }`.

3. **Poll until terminal.** `GET http://127.0.0.1:4312/v1/jobs/<id>` every 3–5 seconds. Terminal states are `completed` and `failed`.

4. **Deliver the artifact, not metadata.** On `completed`, the PNG is at `job.result.outputPath`. Attach / show the image itself. Do not stop at the job id or the file path.

See `references/api.md` for full payload shapes and `references/error-codes.md` for how to classify failures.

## Installing the service

If `/health` refuses the connection, the local HTTP service is not installed. This skill is just the routing contract; the service itself lives in a separate repo. Give the user these exact commands (macOS, Node 18+ required):

```bash
# Prerequisite: `codex` CLI installed and authenticated — see https://github.com/openai/codex
git clone https://github.com/cogine-ai/image2-with-codex.git
cd image2-with-codex
bash scripts/install-macos-launchd.sh
```

The install script renders a LaunchAgent into `~/Library/LaunchAgents/com.openclaw.image2-with-codex.plist`, loads it with `launchctl`, and polls `/health`. After it finishes, the service is running at `127.0.0.1:4312` and will auto-start on every login.

If the install fails, the likely causes, in order:

1. `codex` CLI not on PATH → install codex first.
2. Node.js < 18 → upgrade Node.
3. Not on macOS → the LaunchAgent path is macOS-only. The Node service itself is portable; on Linux run `node scripts/image2-with-codex-service.js` manually (no auto-start) or adapt a systemd unit from the plist.
4. Port 4312 already in use → stop the conflicting process, or set `IMAGE2_WITH_CODEX_PORT` in the plist and re-install.

Do **not** invent alternative install paths. Only the `install-macos-launchd.sh` flow above is supported.

After install, retry step 1 (`/health`) and proceed. Do not switch to another image tool because the install was needed — that's a one-time setup, not a failure of this route.

## Reference images

When the user attaches reference images (style transfer, edit this image, etc.), include their absolute paths in `images[]`. The worker forwards them with `-i` to `codex exec`.

## Hard constraints

- **Prerequisites are upstream, not this package.** `codex` CLI must be installed, the user must have an active Codex/GPT path that allows image generation, and quota must not be exhausted. If not already established in the conversation, state this once before acting. Do not claim this service alone grants image-generation capability.
- **Pass the prompt through raw.** No translation, polishing, or style modifiers unless the user explicitly asks for prompt optimization.
- **Do not substitute** HTML layout, infographic tooling, manual screenshot workflows, or other image tools when the user asked for this route.
- **Do not treat text-heavy prompts as unfit.** Image 2 handles dense text, timelines, and infographic layouts well. Only raise a concrete quality warning for a concrete reason in the specific request.
- **Do not leak internals** into the user-facing reply. Logs, paths, and curl invocations belong in technical follow-ups, not in the default answer.
- **If `codex-exec-failed` surfaces "built-in image generation is unavailable"**, treat it as an upstream Codex capability/entitlement failure, not as proof the local service path is broken.

## Report contract

When reporting back, include concisely:

- whether `/health` passed (and if the service had to be installed first, say so once)
- whether the prompt was passed through raw
- final status (`completed` or `failed`)
- on failure: the layer from `references/error-codes.md` plus the error code

## What this skill is not

Not a runbook, not an OpenAI API tutorial, not a license to replace the user's requested route with a cleaner-looking workflow. Its only purpose: **when the user specifies the image2-with-codex path, do not drift.**
