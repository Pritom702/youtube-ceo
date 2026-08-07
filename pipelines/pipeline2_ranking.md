# Pipeline 2 — RankZilla Ranking Shorts

- **Project:** `T:\Youtube Shorts 2` · Pipeline: `T:\Youtube Shorts 2\ranking_pipeline`
- **Invoke:** `/ranking-short` (or "make today's video")
- **Feeds:** Channel 2 (Ranked Chaos) and Channel 3 (second ranking channel)

## ⭐ NEW correct mechanic — `make_oneclip.py` (use this for Ranked Chaos)
The viral format is **ONE oddly-specific clip + a fake ranking overlay** (see
`../research/HOW_RANKING_SHORTS_WORK.md`), NOT a 6-clip stitch. New orchestrator:
```bash
cd "T:\Youtube Shorts 2\ranking_pipeline"
PYTHONUTF8=1 python make_oneclip.py --clip <file-or-url> \
  --adj Scariest --subject "Slide Drop" --noun Moments \
  --labels "Looks fun|Wait… glass floor?|Knees locked|No way back|DROPPED" --start 0 --end 28
```
Reuses render.py's title/rail/CFR. Metadata title auto-set to "DON'T CHECK THE SOUND
😭😭"; burned title = "Ranking <adj> <subject> <noun>". Labels worst→best (last=#1
climax). Validated 2026-08-08 (see `../reviews/2026-08-08_oneclip_test_slide_drop.md`).
TODO: emoji-capable label font; per-beat reveal timing.

The old `make_short.py` (6-clip compilation) is deprecated for virality — keep only
for legacy/compat.

## Run it (legacy 6-clip — deprecated)
```bash
cd "T:\Youtube Shorts 2\ranking_pipeline"
python -u make_short.py "Ranking Funniest Dog Moments" --max-total 42
# multiple: python -u make_short.py "Topic One" "Topic Two" --max-total 42
```
Outputs `<slug>.mp4` + `<slug>_KIT.md`. Then QC contact sheet:
```bash
ffmpeg -v error -y -i "<slug>.mp4" -vf "fps=1/4,scale=300:-1,tile=6x2" -frames:v 1 qc.jpg
```

## Hard rules
Render locally (never RankReel) · never ship without `verify()` (constant FPS,
zero stutter) · never trim mid-story (pick shorter clips) · always visually QC.

## Topic selection order
1. `T:\Youtube Shorts 2\analytics\PASTE_ANALYTICS_HERE.md` signal table.
2. vidIQ outliers: `python vq.py vidiq_outliers '{"keyword":"ranking","contentType":"short","minViews":3000000,"publishedWithin":"thisMonth","sort":"breakoutScore","limit":25}'` (~5 credits, 150/mo, resets 25th).
3. Reuse a topic shape that worked, with new clips. Never repeat a cached topic silently.

## CEO integration (MANDATORY)
- **Before generating:** read `T:\Youtube CEO\CEO.md` + today's brief. Use the
  CEO's chosen channel, topic, hook, and title. Keep Ranked Chaos and Channel 3
  on their separate lanes per the brief.
- **After generating:** do NOT publish. Submit `<slug>.mp4`, `qc.jpg`, and the
  KIT to the CEO for review (see `../SUBMIT_FOR_REVIEW.md`). Apply REVISE notes
  and resubmit until APPROVED.

## Constraints
TikTok blocks ~half of downloads by IP (over-source; re-run later) · QC auto-
rejects clips <480px, outside 3–25s, no audio, or subject <45% of frame · 5-clip
minimum · target 30–45s · clips are unlicensed (keep source URLs in the kit).
