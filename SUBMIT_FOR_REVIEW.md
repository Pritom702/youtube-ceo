# Submit-for-review protocol (pipelines → CEO)

Both pipelines MUST use this. Nothing publishes without a CEO APPROVE.

## What the pipeline submits
For each finished short, hand the CEO:
1. Path to the rendered `.mp4`.
2. The QC contact sheet image (`qc.jpg` for ranking; contact sheet for kick).
3. The upload kit (`<slug>_KIT.md` / `_upload.txt`): title, description, hashtags,
   source URLs.
4. Which channel + which CEO brief item it fulfills.

## How the CEO reviews
The CEO runs the checklist in `CEO.md §5` against the contact sheet and kit —
actually looking at the frames, not the build log. Then logs a verdict to
`reviews/<date>_<slug>.md`:

- **APPROVE** → cleared to upload. CEO may set posting time/caption tweaks.
- **REVISE** → specific, actionable fixes (e.g. "clip 3 cuts mid-sentence, extend
  to 0:14"; "hook weak, lead with the #1 tease"; "watermark bottom-right, reframe").
  Pipeline applies and resubmits.
- **REJECT** → scrap; CEO issues a fresh brief.

## Verdict log format (`reviews/<date>_<slug>.md`)
```
# Review — <slug> (<channel>) — <date>
Verdict: APPROVE | REVISE | REJECT
Brief item: <link to daily brief line>
Checklist fails: <none | list>
Notes / fixes: <...>
Post at: <time or "queue">
```
