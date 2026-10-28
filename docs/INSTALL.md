# Installation — ChatGPT, Claude, Codex, Antigravity, other agents

## ChatGPT (web or mobile)
Open [the complete master prompt](../prompts/PASTE_IN_CHATGPT.md). Paste into a fresh chat or supported Project instructions, then provide the topic, desired style, script and uploaded voice/assets. Attach the chosen style guide if the model cannot read the GitHub file. This is a conversational **instruction workflow**, not a global native skill install, and rendering is only possible when the running ChatGPT session has appropriate tools. If your product configuration offers a dedicated Skills importer, follow its supported import UI for a portable package; this repository alone cannot activate that importer on your account.

## Codex and Antigravity
Clone `https://github.com/chhatramani01/instagram-motiongraphics-reels.git` and open it as the active workspace. `.agents/skills/instagram-reels/SKILL.md` is discovered by compatible agents; the full skill is in `instagram-reels/SKILL.md`.

To make the skill available in **a different project**, copy the **entire** portable skill folder, not just its Markdown instructions:

```bash
mkdir -p /path/to/other-project/.agents/skills
cp -R instagram-reels /path/to/other-project/.agents/skills/instagram-reels
```

The copied folder includes `SKILL.md`, all style and reference files and rendering tools. The agent's execution environment still requires Python, Playwright/Chromium and FFmpeg.

## Claude Code
When this repository is the active project, Claude Code discovers `.claude/skills/instagram-reels/SKILL.md`. For global installation, copy the entire portable package to `~/.claude/skills/instagram-reels`:

```bash
mkdir -p ~/.claude/skills
cp -R instagram-reels ~/.claude/skills/instagram-reels
```

## Additional Agent Skills tools
Any coding agent implementing the Agent Skills format can use the portable `instagram-reels/` directory, with YAML frontmatter and local resources. Put it in that product's recognized skill location; check its documentation instead of guessing paths. Plain text in an arbitrary folder is not always automatically discovered.

## Runtime requirements
- Python 3.10+ and `python -m pip install -r requirements.txt`
- Chromium via `python -m playwright install chromium`, or use `CHROMIUM_PATH=/path/to/chromium`
- FFmpeg with libx264, AAC, and FFprobe installed on PATH
- Originals or permissioned voice, music, brand assets and footage

Try `python instagram-reels/scripts/demo.py --draft` first. Linux environments sometimes need OS libraries for Chromium; `python -m playwright install --with-deps chromium` on Ubuntu with package manager access. When running under restrictive browser policy the renderer can fall back to inline HTML; **custom scenes that depend on external files must provide embedded assets in that environment**.

## Troubleshooting
- `net::ERR_BLOCKED_BY_ADMINISTRATOR`: navigation blocked in a sandbox. Inline HTML fallback supports the bundled standalone Canvas demo; embed custom images/fonts for the same environment.
- `BrowserType.launch`: install Playwright Chromium or set `CHROMIUM_PATH`.
- `ffmpeg not found`: install FFmpeg and ensure its executable is on PATH.
- `Missing window.renderAt(t)`: scene must expose a pure-time rendering function.
- Mismatched video size: 9:16 requires even width and height, e.g., 360×640 or 1080×1920.
- Media has no audio: check source track and run `mux.py`, then `verify.py`.
- Caption drift: use actual speech word alignment; do not infer timing from only text length.
