# CEO Learnings — append-only

The CEO gets smarter about YouTube every day. Each entry: what I learned, the
source, and how it changes what we make. Newest at top. Never repeat a lesson
already here — build on it.

---

## 2026-08-08 — DEFINITIVE: how ranking shorts work (3 competitors reverse-engineered)
Studied top-10 shorts of @RankZilla23 (399M/238M/102M), @PepeRanker (139M/41M/38M),
@VoiceVsAutotune (36M/24M/13M). Full teardown: `HOW_RANKING_SHORTS_WORK.md`.
- **THE format = ONE continuous oddly-specific clip + a fake ranking overlay** that
  fills with witty scene-specific labels as it plays, best held for last. **NOT a
  6-clip compilation.** Our pipeline builds the wrong mechanic — this is THE fix.
- **Title template (burned, top):** "Ranking [ADJ-RED] [TOPIC-YELLOW] Moments",
  white "Ranking". Identical every upload = brand.
- **CORRECTION to my earlier lesson:** "DON'T CHECK THE SOUND 😭😭" is NOT a bad
  duplicate title — it's the PROVEN metadata hook used by ALL three giants on nearly
  every video (dares you to unmute → sound-on + comments). Two-title system: metadata
  bait + burned on-screen topic. Keep using it.
- **Labels must be scene-specific + witty + emoji** ("Almost died 😱", "R.I.P phone
  😭", "The burn 😖", "-$140", "15%"). Generic fallbacks ("Nailed it") = death.
- **Niches are oddly-specific/absurd/ASMR**, not generic "funny fails": Chicken
  Screaming, Toilet Design, Deep Sea Hunting, Physics Glitch, Muscle Cramp, Cologne
  Atomizers, Bad Day. Weird = curiosity = click.
- **Tight ~15–30s.** RankZilla23 is the originator; PepeRanker cloned him exactly.
- **Music (VoiceVsAutotune):** bold solid YELLOW bg, "No Autotune VS Autotune" title,
  rank rail + numeric SCORES (green/red), often ONE artist, recognizable artists,
  "Who Sings Better?" metadata. Our Real Voice channel lacks the bg + scores.

## 2026-08-08 — First real analytics (all 3 channels) → hard lessons
Data: `analytics/2026-08-08_all_channels.md`.
- **Niche coherence beats variety (biggest lever).** Ranked Chaos dumped glow-ups,
  pressure washing, autotune, fragrance, "weight on planets", AI tools into one
  channel → median stuck at 1–3K despite two 24K+ hits. A coherent channel builds
  an audience; a grab-bag can't. LOCK each channel to ONE lane.
- **Proven winners must be serialized, not abandoned.** Ranked Chaos: pranks 27.7K,
  waterslide 24.5K — yet only 1 prank Part 2 exists and no waterslide Part 2. Part-2
  every winner immediately; that's also the subscribe reason.
- **Gym fails is a LOSER on Ranked Chaos (1.7K).** Stop making them. (Directly
  caused today's Video 1 REVISE.)
- **Mr.GHCLIPS winning lane = strength feats + emotional coach/mentor stories +
  Larry being humbled (10–22K).** Losing lane = political skits (Zohran, ~0.1–1.8K)
  and generic celeb interviews. Feed the winners, cut the skits.
- **Real Voice or Autotune has the best floor (every video 1.8–6K, zero flops) but
  only 6 videos.** Safest compounding bet — scale volume; legends (Freddie 6K,
  Whitney) overperform. Lead with legendary vocalists.
- **Packaging note (REVISED same day):** the identical "DON'T CHECK THE SOUND" title
  is actually the proven metadata hook (see the competitor teardown above) — the real
  gap is the FORMAT behind it (6-clip stitch vs one-clip overlay) and the burned
  on-screen topic title, not the metadata title.
- **Pipeline QC gap:** generic fallback rank labels ship when no scene-specific
  labels TSV exists. Require a `*_labels.tsv` (scene-specific) before approval.

## 2026-08-08 — First research pass (trends)
- 2026 Shorts reward **fast comprehension + rewatch loops + instantly-recognizable
  formats**. Build every video to be understood in 1s and re-watched.
- **Comedy = highest virality**; **relatable ("this is literally me")** and
  **transformation/glow-up** spread fastest. Proven shells: Before vs After, POV,
  Myth Busting, Ranking, Challenge Variations.
- **Lane assignment locked for testing:** Ranked Chaos = comedy/fails ranking;
  Channel 3 = transformation/glow-up ranking (own lane, provisional until named).
- **Kick sourcing:** track daily top clips at streamscharts.com/clips?platform=kick
  and kickcharts.net/clips; cut clutch feats / big reactions / drama.

## 2026-08-08 — Setup baseline
- **Established the operating system.** Two pipelines, three channels, one CEO.
  Brief → generate → submit → review → verdict → learn loop is now mandatory.
- **Retention (`avg % viewed`) is the primary metric**; views follow it. Every
  brief is judged on hook strength first.
- **Volume is the biggest lever** toward 111,000 views/day/channel, but never at
  the cost of a QC fail (throttling risk).
- **Adopted the vidIQ method as core doctrine** (`strategy/vidiq_method.md`).
  Key rules now driving every brief:
  - Shorts distribute via an **explore/exploit seed test**; the deciding signal is
    **Viewed vs. Swiped Away**. Everything serves beating the swipe.
  - **First 3 seconds** decide retention; state topic + tease payoff up front.
  - **Rewatches/loops count as views** → build loopable payoffs (satisfying #1).
  - **Engaged views** (real watches/likes/comments) are what count toward YPP.
  - Best-performing lengths per vidIQ: **~13s or 60s** (test against our 30–45s).
  - Package: keyword in title+description, `#shorts`+niche tags, custom thumbnail,
    say the topic aloud early.
  - Pick topics from **outliers**, titles from **keyword score**; clone shapes not
    clips. Validate niche across 0–10k/10k–100k/100k+ tiers. Pillar/cluster/bridge.
  - **200+ published Shorts** correlates with sustained growth → reinforces volume.
## 2026-08-08 — Ch1 is a COMBAT-SPORTS channel (owner correction)
- **Mr.GHCLIPS = combat sports / athletic action ONLY** (MMA, boxing, street fights,
  knockouts, gym beasts / strength feats, ninja-warrior fails, viral action clips,
  Larry Wheels). Owner's channel description confirms it. See memory
  mrghclips-channel-identity. Gaming/variety/gambling = OFF-BRAND.
- **Mistake to not repeat:** picked xQc's Cobblemon *gaming* tournament for a "more
  views" batch — 5 clips rendered clean but were entirely off-brand → SCRAPPED.
  "Other streamer than Larry" means other COMBAT/athletic streamers (Ryan Garcia,
  Rampage, MMA fighters), never a big streamer whose content isn't combat/action.
- **Pipeline 1 gotcha — 160p→1080p time drift:** discovery-pass (scout) timestamps
  drift up to ~40s from true VOD time. Set final clip windows from the FULL
  `work/stream.srt` timestamps (accurate), not the ranked-candidate list. Cost a re-pull.
- **New-streamer onboarding checklist:** add to CHANNELS (crop+overlay), generate
  `url_<name>.png`, map `CLIP_CHANNEL` (unknown cids default to georgiopoullas → wrong
  KICK URL burned in). xQc is now onboarded.
- Avoid gambling/slots segments entirely (demonetization) even on non-gambling streamers.

- _Next research pass: pull current Shorts trend shifts, competitor outlier
  medians (e.g. @EverythingRankedYT ~191K), and format changes to apply tomorrow._
