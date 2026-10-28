# Clean Product UI

**Style ID:** `clean-product-ui`  
**When to use:** Software tutorials, startup apps, AI agents, feature demos.

## Visual fingerprint and asset direction
Studio product board with original dashboard elements, cursor, selector states and map connections. Use **Inter-like system sans** as the typographic pairing (use available, properly licensed fonts with reliable fallbacks). Never recreate a particular influencer's branded asset, and never treat source screenshots as public-domain images. Design original shapes and illustrative metaphors for the topic.

## Numerical art direction
- Background `#F6F8FA`; primary foreground `#122D33`; accent `#3E9386`; secondary `#E4B46B`. If content requires a warning/failure semantic, assign it explicitly rather than using a random color.
- Canvas defaults to `1080 × 1920` portrait, `30fps`. Hero text/object stays inside the conservative main safe zone x=9–86%, y=17–77%. Caption group should not bury the hero.
- Hierarchy: one dominant object, one source/proof element, one subordinate annotation. Use negative space to separate them.
- Composition: One interface screenshot-equivalent at hero size; labels around the interface not obscuring it; source UI only if supplied.

## Motion grammar: implement as pure-time functions
Cursor moves along eased 0.45s path, selection glow <=6px, result card enters 0.42s after action. Every item needs specified start/finish values and absolute seconds. Use actual analytic easing and sealed (pre-seeded) decorative noise to keep frame capture deterministic.

## Scene transitions and continuity
Selected UI object lifts from app frame into next full-screen proof; button state becomes node. The exiting element should logically become or point at the next shot's main read. Use 4–8 frame directional wipes when there is no meaningful carry-over, not identical global crossfades after every sentence.

## Sound direction
soft pointer click, switch tick, low confirmation tone. Choose cues only at meaningful state changes, on measured speech/beat events when source audio exists. If no voice was supplied, never claim the demo includes spoken narration.

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
