# Contributing

New styles should be original. Add `instagram-reels/styles/<slug>.md` and a matching entry in `instagram-reels/styles/registry.json`. Each should specify concrete colors, fonts, material look, movement durations, transition mechanics, SFX and mobile QA checks. Do not mirror influencer footage or private upstream paths. Extend `tests/` with all new render/audio behavior.

Run:

```bash
python instagram-reels/scripts/check.py
REELS_BROWSER_TEST=1 python -m unittest discover -s tests -v
python instagram-reels/scripts/demo.py --draft
```

Inspect a real contact sheet. Include screenshots or an MP4 for motion changes. Preserve MIT license notices for original code. Do not copy AGPL OpenNolan source into this MIT repository or commit unlicensed media, API secrets, large Whisper models, or rendered per-user private footage.
