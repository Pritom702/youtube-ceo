# Review — ranking_scariest_slide_drop_moments_oneclip (Ranked Chaos) — 2026-08-08

**Verdict: APPROVE (format validated) — first correct-mechanic render.**
This is a pipeline-format proof, not a scheduled upload. It validates `make_oneclip.py`.

## Checklist
- ✅ **Format:** ONE continuous POV clip (capsule slide → drop → splash) + fake rank
  overlay. The real winning mechanic, NOT a 6-clip stitch.
- ✅ **Title template:** "Ranking"(white) "Scariest"(red) "Slide Drop"(yellow)
  "Moments"(white) — matches RankZilla exactly.
- ✅ **Rank rail** fills #5→#1 as tension builds; **#1 "DROPPED" reveals exactly at
  the drop/splash** — payoff label on payoff moment. Best held for last.
- ✅ **Scene-specific witty labels** (Looks fun → Wait… glass floor? → Knees locked →
  No way back → DROPPED). No generic fallbacks.
- ✅ **CFR:** 30/1, 841 frames, zero drops. ✅ No baked-in foreign text issues.
- ✅ **Metadata title:** "DON'T CHECK THE SOUND 😭😭".

## Polish notes (for the productionized version)
- **Emoji don't render** in labels (PIL italic font lacks color-emoji glyphs). Text-
  only works; add an emoji-capable font (e.g. Segoe UI Emoji / Noto Color Emoji) to
  the renderer for the extra pop competitors have.
- Consider tightening to ~18–22s (comp range 15–30s); 28s is acceptable.
- Reveal timing is even (5.6s/beat) and happened to align; add per-beat reveal times
  to lock the climax label to the exact payoff frame every time.

## Decision
`make_oneclip.py` is the new Ranked Chaos mechanic. Next: add emoji font + reveal-
timing control, then produce an on-strategy oddly-specific batch for CEO review.
