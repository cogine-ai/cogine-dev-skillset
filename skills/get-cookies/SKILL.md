---
name: get-cookies
description: Use when a site under review requires authentication and you need to import cookies from a real browser session into your local browser automation helper. Trigger on "get-cookies", cookie import, browser session reuse, authenticated QA, or protected pages behind login.
---

# get-cookies

Cogine internal skill for importing cookies from a real browser session into local browser automation.

## Cross-Platform Notes

- When this skill says `AskUserQuestion`, use the platform's question or confirmation tool if available; otherwise ask the user directly and wait.
- Ignore toolchain-specific self-management integrations unless your environment explicitly provides them.
- This skill assumes your environment has a browser automation helper that supports cookie import. If it does not, stop and ask the user which local browser tool to use.

## Preamble (run first)

```bash
_BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
echo "BRANCH: $_BRANCH"
```

## AskUserQuestion Format

**ALWAYS follow this structure for every AskUserQuestion call:**
1. **Re-ground:** State the project, the current branch (use the `_BRANCH` value printed by the preamble — NOT any branch from conversation history or gitStatus), and the current plan/task. (1-2 sentences)
2. **Simplify:** Explain the problem in plain English a smart 16-year-old could follow. No raw function names, no internal jargon, no implementation details. Use concrete examples and analogies. Say what it DOES, not what it's called.
3. **Recommend:** `RECOMMENDATION: Choose [X] because [one-line reason]`
4. **Options:** Lettered options: `A) ... B) ... C) ...`

Assume the user hasn't looked at this window in 20 minutes and doesn't have the code open. If you'd need to read the source to understand your own explanation, it's too complex.

Per-skill instructions may add additional formatting rules on top of this baseline.

# Setup Browser Cookies

Import logged-in sessions from your real Chromium browser into the headless browse session.

## How it works

1. Find the browse binary
2. Check whether the current automation session is already attached to a real browser profile
3. Run `cookie-import-browser` to detect installed browsers and open the picker UI
4. User selects which cookie domains to import in their browser
5. Cookies are decrypted and loaded into the Playwright session

## Steps

### 1. Find the browse binary

## SETUP (run this check BEFORE any browse command)

```bash
_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
B="${COGINE_BROWSE_BIN:-}"
[ -z "$B" ] && [ -n "$_ROOT" ] && [ -x "$_ROOT/.cogine/tools/browse" ] && B="$_ROOT/.cogine/tools/browse"
[ -z "$B" ] && [ -x "$HOME/.cogine/tools/browse" ] && B="$HOME/.cogine/tools/browse"
[ -z "$B" ] && command -v browse >/dev/null 2>&1 && B="$(command -v browse)"
if [ -n "$B" ] && [ -x "$B" ]; then
  echo "READY: $B"
else
  echo "NEEDS_SETUP"
fi
```

If `NEEDS_SETUP`:
1. Tell the user: "Cogine browser tooling is not configured on this machine. Point me to the browser helper binary or tell me which browser automation stack to use." Then STOP and wait.
2. If the user provides a path, export it as `COGINE_BROWSE_BIN` for the current session and continue.

### 2. Check for real-browser / CDP mode

If the browser automation helper is already connected to a real browser profile through CDP or an equivalent "use my existing browser" mode, cookie import is usually unnecessary. Verify before opening the picker:

```bash
$B status 2>/dev/null || true
```

If the status output indicates an attached real browser profile, tell the user: "This session already appears to be using your real browser profile, so cookie import is not needed unless a specific domain still fails authentication." Then continue with the authenticated QA task.

If the helper has no `status` command or the output is inconclusive, continue to cookie import.

### 3. Open the cookie picker

```bash
$B cookie-import-browser
```

This auto-detects installed Chromium browsers (Comet, Chrome, Arc, Brave, Edge) and opens
an interactive picker UI in your default browser where you can:
- Switch between installed browsers
- Search domains
- Click "+" to import a domain's cookies
- Click trash to remove imported cookies

Tell the user: **"Cookie picker opened — select the domains you want to import in your browser, then tell me when you're done."**

### 4. Direct import (alternative)

If the user specifies a domain directly (e.g., `/get-cookies github.com`), skip the UI:

```bash
$B cookie-import-browser comet --domain github.com
```

Replace `comet` with the appropriate browser if specified.

### 5. Verify

After the user confirms they're done:

```bash
$B cookies
```

Show the user a summary of imported cookies (domain counts).

## Notes

- First import per browser may trigger a macOS Keychain dialog — click "Allow" / "Always Allow".
- On Linux, Chromium cookie decryption may depend on libsecret/Secret Service and the browser's current cookie storage version. If imports fail on Linux, report the exact helper output and ask whether to use an already-authenticated CDP session instead.
- Cookie picker is served on the same port as the browse server (no extra process)
- Only domain names and cookie counts are shown in the UI — no cookie values are exposed.
- Do not print cookie values, raw SQLite rows, decrypted secrets, or Keychain/libsecret output.
- The importer should read browser cookie stores through a temporary read-only copy and avoid writing plaintext cookies to disk outside the automation session.
- The browse session persists cookies between commands, so imported cookies work immediately.
