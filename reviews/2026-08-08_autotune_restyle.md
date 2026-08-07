# Review — Real Voice or Autotune restyle (no_autotune_part1 re-render) — 2026-08-08

**Verdict: APPROVE — now matches @VoiceVsAutotune's exact style.**

Re-rendered `no_autotune_part1.mp4` on the new `style="autotune"`. `verify: PASS`
(1665 frames, 30fps CFR, 0 stutters).

## Matches the competitor
- ✅ **Yellow brand title band** with **"No Autotune"(teal) VS(white) "Autotune"(red)**
  — their exact wording + colors (was "REAL VOICE VS AUTOTUNE" on black).
- ✅ **Rank rail 1–5** fills with artist + song as it plays; #1 (Adam Levine) last.
- ✅ **Numeric scores in GREEN** (≥7/10) — red kicks in automatically for any <7.
- ✅ **A/B reveal**: "REAL VOICE"(teal) / "AUTOTUNE"(red) label switches per half.
- ✅ **"WHO SHOULD BE NEXT?"** prompt on the final segment (subscribe/comment driver).
- ✅ Metadata title updated to **"Who Sings Better? No Autotune VS Autotune"**.

## Notes / next polish
- Footage is near full-bleed under a ~300px yellow band. Competitor's yellow is more
  dominant (artist keyed onto yellow); exact match would need background removal per
  clip (heavy/unreliable). Current read is unmistakably their format — good.
- **Scores are all green** because this roster inflates top ranks (10/10, 12/10,
  13/10). To get the green+red mix the competitor uses, future rosters should include
  some genuinely low scores (e.g. 2/10, 4/10) — the renderer already colors <7 red.
- Parts 2–9 still render in the old style; re-render the queue with the new build.

## Files
`T:\Youtube Shorts 2\no_autotune_part1.mp4` (+ _KIT.md, _qc.jpg). Engine changes in
`ranking_pipeline/render.py` (autotune title/canvas/score) + `make_autotune.py` (title).
