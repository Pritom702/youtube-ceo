# Review — Real Voice or Autotune Part 2 (new style re-render) — 2026-08-08

**Verdict: APPROVE.** Ch3's 2nd short for today (owner asked for 2/channel).

Re-rendered `no_autotune_part2.mp4` on the approved `style="autotune"` build.
`verify: PASS` (1667 frames, 55.5s, 30fps CFR, 0 stutters).

## Fix applied first
Initial re-render failed: Michael Jackson's studio VIDEO (`use_studio_video`) was
never cached — only the studio audio. Downloaded `michaeljackson_studiovid.mp4`
(studio_id Zi_XLOBDo_Y) via yt-dlp `--no-plugin-dirs` (the bgutil pot-provider
plugin was hanging all YouTube pulls — see memory `ytdlp-pot-plugin-fix`), then
re-rendered clean.

## Matches the competitor style (same as approved Part 1)
- ✅ Yellow band "No Autotune"(teal) VS(white) "Autotune"(red).
- ✅ Rank rail 1–5 fills with artist + song; #1 Michael Jackson (Billie Jean) last.
- ✅ REAL VOICE (teal) / AUTOTUNE (red) A/B labels switch per half.
- ✅ "WHO SHOULD BE NEXT?" prompt on the final segment (sub/comment driver).
- ✅ Consistent framing, legible on every segment, no watermark, clean audio, CFR.

## Roster (reveal #5→#1)
| # | Artist | Song | Score |
|---|---|---|---|
| 5 | Oliver Tree | Miss You | 7/10 |
| 4 | d4vd | Here With Me | 8/10 |
| 3 | Juice WRLD | Lucid Dreams | 10/10 |
| 2 | AURORA | Runaway | 12/10 |
| 1 | Michael Jackson | Billie Jean | 13/10 |

## Notes / next polish (not blockers)
- **All scores green** (all ≥7). Same as Part 1 (approved). For the green+red mix
  the competitor uses, a future roster should include a genuine 2–4/10.
- AURORA live/studio lyric alignment scored weak (0.33) in the align stage; the
  A/B still reads on the contact sheet. Watch the AURORA switch on playback; if the
  sync feels off, swap her live clip in a future part.
- Parts 3–9 still on the OLD style — re-render the queue with the new build over time.

## Files
`T:\Youtube Shorts 2\no_autotune_part2.mp4` (+ `_KIT.md`, `_qc.jpg`).
Cleared to upload. HELD for owner's final look per the review gate.
