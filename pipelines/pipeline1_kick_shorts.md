# Pipeline 1 — Kick VOD → Viral Shorts

- **Project:** `T:\Youtube Shorts`
- **Invoke:** `/kick-shorts <kick-vod-url>` (or paste a Kick link)
- **Feeds:** Channel 1 (Larry Wheels)
- **Engine:** `make_short.py` (blurred canvas, dynamic captions, title box, KICK
  branding). `clip.py` builds one clip end-to-end with a build cache.

## Flow (what /kick-shorts does)
1. Probe + download 160p analysis copy of the VOD.
2. `scout.sh "<url>"` (background): full word-level transcript (single timeline,
   no drift), per-second `energy.txt`, whole-VOD contact sheet, ranked shortlist.
3. Inspect frames only from the local analysis copy (free). Pull 1080p ONLY for
   final approved clips, batched (`-N 16`).
4. `renderall.sh g1 g2 ...` renders clips in parallel (`FAST_RENDER=1` = NVENC).
5. Re-render a tweak with `python make_short.py <id>` (reuses cached src).

## CEO integration (MANDATORY)
- **Before generating:** read `T:\Youtube CEO\CEO.md` and today's brief
  (`T:\Youtube CEO\daily\<date>_brief.md`). Build exactly to the CEO's clip
  selection, hooks, titles, and format notes.
- **After generating:** do NOT publish. Produce the contact sheet + upload .txt
  and submit to the CEO for review (see `../SUBMIT_FOR_REVIEW.md`).
- Apply the CEO's REVISE notes and resubmit until APPROVED.

## Known constraints
- Full 160p download ~9 min in isolation; slowness comes from contention — use
  the fast path. Set trims/titles from each clip's OWN 1080p `.srt` (160p drifts).
- Cut on complete thoughts only; never stop mid-sentence.
