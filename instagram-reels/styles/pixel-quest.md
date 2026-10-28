# Pixel Quest Story

**Style ID:** `pixel-quest`  
**When to use:** Product tutorials, progress stories, levels/stages, skill lists.

## Visual fingerprint and asset direction
Pixel RPG overworld with tile-based geometry, quest markers, physical inventory and clean data panes. Use **pixel display for headings + legible sans for captions** as the typographic pairing (use available, properly licensed fonts with reliable fallbacks). Never recreate a particular influencer's branded asset, and never treat source screenshots as public-domain images. Design original shapes and illustrative metaphors for the topic.

## Numerical art direction
- Background `#E9E2CE`; primary foreground `#352B45`; accent `#7B60B5`; secondary `#DFA64A`. If content requires a warning/failure semantic, assign it explicitly rather than using a random color.
- Canvas defaults to `1080 × 1920` portrait, `30fps`. Hero text/object stays inside the conservative main safe zone x=9–86%, y=17–77%. Caption group should not bury the hero.
- Hierarchy: one dominant object, one source/proof element, one subordinate annotation. Use negative space to separate them.
- Composition: Narrative world occupies middle 55%; proof panels rendered as crisp UI inventory cards, not tiny pixel type.

## Motion grammar: implement as pure-time functions
Avatar moves on 8/12fps stepped tween within a 30fps overall export; UI labels ease 0.25s; particles seeded. Every item needs specified start/finish values and absolute seconds. Use actual analytic easing and sealed (pre-seeded) decorative noise to keep frame capture deterministic.

## Scene transitions and continuity
A door or portal becomes next diagram window; use authentic map-like wayfinding for sequences. The exiting element should logically become or point at the next shot's main read. Use 4–8 frame directional wipes when there is no meaningful carry-over, not identical global crossfades after every sentence.

## Sound direction
8-bit confirm blip, small quest chime, no constant gaming soundtrack. Choose cues only at meaningful state changes, on measured speech/beat events when source audio exists. If no voice was supplied, never claim the demo includes spoken narration.

## 12-second example skeleton
| Time | Visual | Reading task | Motion & SFX |
|---|---|---|---|
| 0.0–1.5s | Hero contrast using this material | Recognize the problem/promise | Immediate object change / impact |
| 1.5–4.0s | Specific before state and why it fails | Understand stakes | Single meaningful relation moves |
| 4.0–7.3s | Mechanism built one piece at a time | See cause and effect | Connectors/transform tied to spoken clauses |
| 7.3–10.8s | Tangible result, artifact, or verified evidence | Understand payoff | Change of scale, one short soft-settle |
| 10.8–12.0s | Complete conclusion with readable hold | Remember outcome | Settled hero; quiet audio tail |

## Rejection checklist
- Reject a static text template with arbitrary zooms in place of a material-specific scene.
- Reject facts, logos or assets that were not provided or verified.
- Reject text clipped at 360px-wide mobile view or behind an Instagram side rail.
- Reject motion that resets context without an explanatory transition.
- Reject sound effects that compete with actual voiceover.
- Re-render contact sheet and final audio/video stream check after revisions.
