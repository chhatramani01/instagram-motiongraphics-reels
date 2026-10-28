---
name: instagram-reels
description: Direct, storyboard, animate and render premium vertical Instagram Reels, Shorts and TikToks from a topic, script, footage or voice audio. Use when users request social videos, visual hooks, smooth motion design, word-timed captions, explainer graphics or a finished code-rendered MP4.
---

# Instagram Motion Graphics Reels — Agent Skill

**One source of truth:** https://github.com/chhatramani01/instagram-motiongraphics-reels

This skill directs a film. It does not call an image/video generation model. The agent writes deterministic Canvas/SVG (or deliberately chosen Remotion/Three.js) code; Playwright captures each time step; FFmpeg encodes final H.264 video and muxes audio. The craft comes from specific visual directions, clean story structure, motion polish, sound, and looking at real rendered frames.

## Stage 0 — Scope and availability

When given audio/video/assets, inspect them and obtain actual duration, aspect, permission and original wording. Never invent quoted words, metrics, external screenshots, or a completed render. When missing genuinely essential details, ask once; otherwise default to a **12-second, 1080×1920, 30fps, 9:16** reel with original artwork and sound effects (not invented narration). Explain the chosen format and style. Honor a user's storyboard-approval gate.

**Important cross-agent behavior:** Codex/Antigravity read `.agents/skills/instagram-reels/SKILL.md`, Claude Code reads `.claude/skills/instagram-reels/SKILL.md`, and this full package can be copied to either location. Ordinary ChatGPT users can paste `prompts/PASTE_IN_CHATGPT.md`; that supplies instructions, not shell access. If this skill is installed alone, all required `references`, `styles`, `scripts` and demo files must accompany it.

## Stage 1 — Attention design before animation

1. Write **Topic → Angle → Viewer tension → Format → Proof / Payoff**. Choose the hook family by content: tutorial (utility), personal story (stakes), myth-bust (testable contrast), proof-first (verified evidence). Never use incorrect facts, deliberate typos or deceptive unresolved clickbait to farm comments.
2. Design the first **0–1 second as a meaningful visual event** and the first 2–5 seconds as combined **visual + spoken (only if supplied or generated) + SFX**. Earn the next second with a specific promise or curiosity gap.
3. Give every 1–3 seconds a micro-payoff, not just a random cut: new evidence, a visible mechanism, a before→after step, or a contrast. Viewer attention is an editorial hypothesis, not a guarantee of engagement.
4. End with a resolved takeaway and an optional relevant CTA. A looping reel may connect the last object/state to the opening, but never at the cost of clarity.

Load `references/creative-direction.md` and `references/storyboard-and-retention.md`.

## Stage 2 — Style bible and visual storyboard first

Pick **one** primary look from `styles/INDEX.md` and read its full `styles/<name>.md`. Pick at most one format recipe in `references/format-recipes.md`. Reference materials are **creative descriptions, not pre-implemented engines**. Produce a director's bible with colors in hex, actual type hierarchy, composition, material/texture, layout coordinates, camera grammar, transitions, easing specifications, and intended SFX. Never fall back to centered words on generic gradients.

Show a timed table with each beat's start/end seconds, **visual frame**, exact on-screen text, intended viewer read, motion entrance/continuity/transition, narration alignment and sound cue. Draw static still storyboard panels when tools allow. If user said *storyboard first / wait for OK*, stop before writing the animation until approved. Otherwise continue after showing the plan.

## Stage 3 — Precision motion as code

- Draw everything from **pure time** `window.renderAt(t)`; repeated calls at the same `t` must produce identical pixels regardless of call order. Add a normal `requestAnimationFrame` preview using `performance.now` but disable it in offline mode.
- No unseeded `Math.random()` in render, incrementing frame counters, CSS timer transitions, or history-dependent simulation. Precompute or seed particle locations and use closed-form springs.
- Prefer soft-settle staging: **0.28–0.36s** for key phrase entrance, **12–18px** initial movement, **2–3px** blur at most when useful, scale **1.03→1.00** rather than cartoon overshoot; delay ambient motion until content lands. These are guidelines, not mandatory for every style.
- Use object-driven continuity: carry one graphic between shots, transform a diagram into a proof card, animate connectors as actual relationships, or use a match cut. Every motion must clarify the story or hierarchy.
- Compose for 9:16 *natively*; do not stretch landscape frames. Main text stays in a conservative mobile-safe region approximately **x=9–86% and y=17–77%**; keep captions around y=67–76% unless user footage/layout demands another safe band. These are conservative production defaults, not an official permanent Instagram UI specification.
- Test typography at ~360px phone width and avoid orphan words or clipped Devanagari glyphs. Use properly licensed fonts and preserve exact transcript characters.

Read `references/motion-system.md` and `references/mobile-layout.md`.

## Stage 4 — Audio, speech and captions

- First measure audio with `ffprobe`. If voice is provided, use accurate forced/word alignment when available; if not, label timings **estimated**. Never pass estimated transcript timing off as measured.
- Captions: group 2–5 spoken words at a time, highlight the actual active word, keep sufficient dwell, avoid screen UI and the speaker's face. If language uses Devanagari, shape text as whole Unicode clusters; do not manually split combining marks.
- An RMS-driven cartoon mouth is **approximate** audio reactivity, not phoneme/viseme-level lip-sync.
- SFX should have narrative functions (click for select, whoosh for material travel, thump for emphasis, riser ending on reveal). Often keep cues sparse (~one every couple seconds under dense speech), and avoid random overdesigned effects. When accuracy allows, start an effect ~10–20ms before the target visual action.
- Render/prepare audio **offline**, then mux with FFmpeg. Never claim the video has audio just because a browser preview plays sound. Preserve the target video length even when the voice track ends early.

Read `references/audio-and-captions.md`.

## Stage 5 — Actual rendering and QA

With Python 3.10+, Playwright, Chromium and FFmpeg available:

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
python instagram-reels/scripts/check.py
python instagram-reels/scripts/demo.py --draft
python instagram-reels/scripts/demo.py
```

The repository sample exports `output/reel.mp4`, `output/contact-sheet.png`, and a technical report. For a custom scene, run `scripts/render.py`, `scripts/contact_sheet.py`, `scripts/audio_synth.py`, and `scripts/mux.py` via the CLI help. Review **actual frames** (opening, each beat, cuts, ending), play a half-res draft and listen to the final track. Verify `ffprobe` streams, color/pixel format, and length. If full rendering is unavailable, deliver runnable source and describe exactly which checks could not run.

## Stage 6 — Deliver with accountable critique

Deliver the final MP4 and source paths only if verified, the storyboard as built, style/color/motion rules, and two genuinely weak spots spotted in inspection with concrete fixes. Do not claim polished lip-sync, Instagram reach, external tool execution or uploaded publishing unless demonstrated. The sample contains *only procedural SFX*, not an invented spoken voice.

## Source interpretation and licensing

This is an **original cross-agent implementation** informed by the production and retention concepts in the user-provided OpenNolan Instagram Reels skill (`het8802/OpenNolan`, AGPL-3.0) and other public filmmaking practice. We do **not** bundle or copy OpenNolan's AGPL source code, proprietary session artifacts, linked influencer media, or private directory paths. This repository's own original code is MIT licensed. See `references/provenance.md`.
