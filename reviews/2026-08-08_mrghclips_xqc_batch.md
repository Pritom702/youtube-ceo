# Review — Mr.GHCLIPS xQc batch (5 shorts) — 2026-08-08

**Verdict: APPROVE (5/5) for review-gate — QC-clean, but see the source caveat.**
Ch1's 5 shorts for today (owner asked for ≥5). Owner said "find a streamer that'll
get more views" → CEO pick **xQc** (top English Kick streamer, monetization-safe vs
gambling streamers). Source VOD: xQc 2026-08-07 "Cobblemon tournament" (14e47f30, 6h38).

## The 5 clips (all in `T:\Youtube Shorts\Shorts\Saturday Shorts (2026-08-08)\xQc\`)
| id | Moment | Dur | Hook |
|---|---|---|---|
| xq1 | Threatens to blow up the arena "like Bane" | 29s | villain monologue |
| xq2 | Says "sigh"/"lol" OUT LOUD in real life | 16s | relatable banter |
| xq3 | "I've NEVER played Pokemon in my life" | 20.5s | cocky confession |
| xq4 | "I almost fell to my death!" panic | 23s | panic + Lando Norris/F1 bit |
| xq5 | Brutally honest rant on the grind | 21s | "nothing about this is fun" |

## Passes (CEO §5)
- ✅ Correct **KICK.COM/XQC** branding (fixed a defect — see below), Mr.GHCLIPS header,
  title card per clip, dynamic keyword captions, KICK logo.
- ✅ Complete thoughts (no mid-sentence cuts), clean audio, CFR verify PASS all 5.
- ✅ NO gambling/slots content (this VOD had gambling segments — all avoided).
- ✅ No competitor watermark / no baked-in foreign text.

## Work done to get here (onboarded xQc into Pipeline 1 from scratch)
- Sourced + validated a current xQc VOD via Kick API; scout.sh downloaded (−N16),
  transcribed (6h38), ranked 25 candidates. Picked 5 non-gambling, universally-funny.
- Added `xqc` to CHANNELS (crop/overlay), generated `url_xqc.png`, mapped `xq*→xqc`,
  added CFG+META for xq1–xq5.
- **Defect caught + fixed:** first render branded clips **KICK.COM/GEORGIOPOULLAS**
  (unknown cids defaulted to Georgio). Added the xqc channel entry → re-rendered.
- **160p→1080p time drift:** discovery timestamps were off by up to ~40s; xq4 first
  landed on filler ("aura aura"). Re-pulled from the TRUE timestamp in the full
  transcript (1:31:09) to capture the real "almost fell to my death" line.

## Honest CEO caveat (why these are "review-gate APPROVE," not slam dunks)
This VOD is a **Cobblemon (Minecraft-mod) tournament** — niche gameplay visuals,
xQc's facecam is a tiny left-side box (cropped out), and a few clips open on a
dark frame / inventory menu (weaker first-frame visual hook). The **audio/personality
carries** each clip (the Bane bit + "never played Pokemon" are genuinely funny), and
xQc gaming clips do get views — but this isn't his strongest clip fodder.

**Recommendation for the next Ch1 batch:** source a **reacts / IRL / drama** xQc VOD
(he reacts to viral videos — universally comprehensible, facecam-forward, stronger
hooks) rather than a game tournament. That better serves the "more views" goal.
Owner: watch xq1 + xq3 first (the two strongest); cut any that don't fit the channel.

## Files
5× `short_xqN.mp4` + `_upload.txt`/`.json` kits. QC strips: `reviews/_qc_xqN.jpg` +
`reviews/2026-08-08_xq1_qc.jpg`. HELD for owner's final look; nothing published.
Memory: [[ytdlp-pot-plugin-fix]] applied for the YouTube (MJ) pull earlier today.
