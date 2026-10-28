# Audio, transcription, captions and timing

## Timeline contract
All events use seconds from start = 0. Beat list, `word.start/end`, `sfx.at` and scene transitions share one zero point. If original narration or song audio exists, measure it with `ffprobe` before cutting; never set a guessed duration.

## Spoken content
Use actual speech transcription or supplied exact script and forced alignment. Store aligned words as `[{"word":"...","start":0.0,"end":0.3,"estimated":false}]`. If timing is not measured, mark `estimated:true` and ask for verification. Word-by-word highlights happen at the exact measured start; phrase captions may pre-appear by 0.06–0.1s but never misrepresent spoken words. Handle Hindi/Nepali as full Unicode grapheme clusters and test a font with real Devanagari coverage.

## Character mouth
RMS energy over 20–33ms windows can make a cartoon mouth react to a voice, but it cannot locate /p/, /m/, /a/ or exact visemes. Never advertise as precise lip-sync without a phoneme aligner and tested model.

## Offline SFX and mastering
Choose one timbral palette that matches the medium (paper = dry swish/marker; UI = small ticks/clicks; cinematic = low impact plus riser). No repetitive whoosh for every transition. Build a sparse event manifest with `type, at, gain`. Synthesized foley in this repo is original mono 48kHz PCM. The sample's SFX playback has no narration; when a user supplies narration, mix it at precedence and reduce music/foley levels.

Use FFmpeg to mux outside the browser and confirm final video/audio streams via ffprobe. Avoid `-shortest` as a sole duration guarantee; output should reach the requested visual end even when input audio is shorter. Voice ducking can be added through `sidechaincompress` where available; the shipped mixer currently uses conservative fixed volumes and a limiter, so do not call it adaptive ducking.

## Rights
Use only supplied/owned/licensed music and footage. Do not transcribe-and-republish full commercial song lyrics or bundle recordings as stock. Do not scrape Instagram private content or bypass access controls.
