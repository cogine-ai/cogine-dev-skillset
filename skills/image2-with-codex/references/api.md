# API reference

Base URL (default): `http://127.0.0.1:4312`. All endpoints are local-only (bound to 127.0.0.1).

## `GET /health`

Service readiness report. Returns HTTP 200 when `ok: true`, HTTP 503 otherwise.

```json
{
  "ok": true,
  "queue": { "queued": 0, "running": 0, "completed": 3, "failed": 0, "total": 3 },
  "config": {
    "host": "127.0.0.1",
    "port": 4312,
    "artifactRoot": "/tmp/image2-with-codex-service",
    "jobTtlMs": 3600000,
    "jobStateFile": "/tmp/image2-with-codex-service/jobs-state.json",
    "generatedImagesRoot": "/Users/<you>/.codex/generated_images",
    "workerWorkdir": "/path/to/image2withcodex"
  },
  "checks": [
    { "name": "codex-command", "ok": true, "details": { "path": "/opt/homebrew/bin/codex" } },
    { "name": "codex-cli-runnable", "ok": true, "details": { "version": "codex 0.x.y", "error": null } },
    { "name": "artifact-root-writable", "ok": true, "details": { "path": "/tmp/image2-with-codex-service", "error": null } },
    { "name": "generated-images-root", "ok": true, "details": { "path": "/Users/<you>/.codex/generated_images", "error": null } },
    { "name": "worker-workdir", "ok": true, "details": { "path": "/path/to/image2withcodex", "error": null } },
    { "name": "job-state-path-writable", "ok": true, "details": { "path": "/tmp/image2-with-codex-service/jobs-state.json", "error": null } }
  ]
}
```

If `ok: false`, the first failing entry in `checks[]` tells you what to tell the user:

| check name                 | how to resolve                                                   |
| -------------------------- | ---------------------------------------------------------------- |
| `codex-command`            | `codex` CLI is not on PATH. User must install it.                |
| `codex-cli-runnable`       | `codex` is on PATH but `codex --version` failed. Auth / broken install. |
| `artifact-root-writable`   | `/tmp/image2-with-codex-service` cannot be written. Permissions. |
| `generated-images-root`    | `~/.codex/generated_images` is missing or not a directory.       |
| `worker-workdir`           | Repo root resolved but not a directory. Internal config issue.   |
| `job-state-path-writable`  | Job state JSON cannot be written. Filesystem / permissions.      |

## `POST /v1/images/generations`

Submit a job. Returns HTTP 202 with `{ ok: true, job: { ... } }`. Errors return HTTP 4xx with `{ ok: false, error: { code, message, details } }`.

Request:

```json
{
  "prompt": "string (required, non-empty after trim)",
  "images": ["/absolute/path/to/reference.png", "..."],
  "timeout_sec": 600
}
```

If `timeout_sec` is omitted the service defaults to `600` (10 minutes). The `job.timeoutMs` in the response echoes the value actually applied, so you can verify the request was honoured.

Response (202):

```json
{
  "ok": true,
  "job": {
    "id": "<uuid>",
    "status": "queued",
    "prompt": "...",
    "timeoutMs": 600000,
    "createdAt": "2026-04-23T10:00:00.000Z",
    "startedAt": null,
    "completedAt": null,
    "expiresAt": null,
    "error": null,
    "result": null
  }
}
```

## `GET /v1/jobs/<id>`

Returns HTTP 200 with the current job state. Terminal states are `completed` and `failed`.

Completed shape:

```json
{
  "ok": true,
  "job": {
    "id": "<uuid>",
    "status": "completed",
    "prompt": "...",
    "createdAt": "...",
    "startedAt": "...",
    "completedAt": "...",
    "expiresAt": "...",
    "error": null,
    "result": {
      "outputPath": "/tmp/image2-with-codex-service/<uuid>.png",
      "sourceImagePath": "/Users/<you>/.codex/generated_images/<codex-file>.png",
      "size": 123456,
      "elapsedSec": 42,
      "timedOutRescued": false,
      "restartRescued": false
    }
  }
}
```

Two "rescue" flags may appear on a successful `completed` job. Both mean **the image is valid** and should be delivered to the user normally; they only exist for observability.

- `result.timedOutRescued: true` — `codex exec` exceeded `timeoutMs` but a freshly generated PNG was found in the execution window, so the worker returned it instead of failing.
- `result.restartRescued: true` — the service was restarted while the job was still `running`, but the artifact PNG was already on disk at `<artifactRoot>/<job-id>.png` when the new service instance loaded state. The new instance finalized the job as `completed`. `sourceImagePath` is `null` in this case (unknown). `elapsedSec` is the wall-clock delta from `startedAt` to restart-detection, not codex's real runtime.

Failed shape: `status: "failed"`, `result: null`, `error: { code, message, details }`. See `error-codes.md`.

Unknown job id: HTTP 404, `code: "job-not-found"`.

## Notes

- Jobs live for `IMAGE2_WITH_CODEX_JOB_TTL_MS` (default 1h) after terminal. After that they're cleaned from the in-memory map.
- Request body is capped at 1 MiB.
- The queue is serial: one codex exec at a time. Concurrent submissions wait.
- Default `timeout_sec` is 600 (10 min). image2 generation usually finishes well under that, but `codex exec` adds reasoning / post-processing overhead. If 600 still trips, see `error-codes.md` on `codex-exec-timeout`.
