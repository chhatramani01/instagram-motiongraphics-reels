# Premium motion system — design as values, not adjectives

## Closed-form time functions
Implement animation as `position = fn(absoluteSeconds)`; never step a state machine frame by frame. For each element define an entrance start, entrance duration, rest state, optional hold/ambient motion, and exit. For independent frame sampling, all transforms must be calculated without reading the previous frame.

### Useful easing functions
- Soft smoothstep: `u*u*(3-2*u)` for camera travel or long diagram moves.
- Quintic smootherstep: `u^3*(u*(u*6-15)+10)` for elegant held moves.
- Out cubic: `1-(1-u)^3` for fast UI response without an exaggerated bounce.
- Damped spring analytic: `1 - exp(-ζωt) * (cos(ωd t) + ζω/ωd sin(ωd t))` for `0 < ζ < 1`. Choose damping near critical for restrained UI objects.

Clamp normalized time `u=(t-start)/duration` to [0,1]. When t is before the start, avoid negative-scale artifacts. Use physically motivated travel distance that is smaller when the object is close to final position.

## Smooth premium defaults (adapt to content)
- Kinetic word: 0.28–0.36s, 12–18px upward travel, 0→1 alpha, tiny 1.03→1.0 settle.
- Editorial cards: 0.38–0.55s, 36–64px horizontal travel with low acceleration, max 1.02 peak scale.
- Connector: 0.35–0.75s draw-on progress along an actual diagram path.
- Camera: slow 1.00→1.02 push only when it creates focus; no constant synthetic drift.
- Transitions: 4–8 frames purposeful wipe/object match. Hold exact statements after reveal.
- SFX: ~10–20ms early if it improves perceived sync; never replace a factual beat with noise.

## Perceived motion quality
Subpixel coordinates, stable letter spacing, clean anti-aliasing, consistent light/shadows. Don't animate all components with identical ease or enter at once. Establish a hierarchy: primary item → evidence object → annotation. Visual-only movement should not obscure voice-timed captions.

## Determinism test
Take a screenshot for time `3.2s`, render `0.5s`, then screenshot `3.2s` again. The pixels must match. Repeat with seeded noise. No `Date.now()`, `performance.now()` inside `renderAt(t)`; use clock only in preview runner.
