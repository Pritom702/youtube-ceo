# HOW RANKING SHORTS ACTUALLY WORK (the master format)

Reverse-engineered 2026-08-08 from the three biggest players in the exact niche:
- **@RankZilla23** — 399M, 238M, 102M, 99M, 80M, 63M, 58M, 44M, 42M, 40M... (originator)
- **@PepeRanker** — 139M, 41M, 38M, 26M, 22M, 21M... (near-identical clone of RankZilla)
- **@VoiceVsAutotune** — 36M, 24M, 13M... (same mechanic applied to music)

Our channels run the SAME genre and get 1–3K. The format below is the gap.

## The single most important insight
**A "ranking short" is ONE continuous clip with a fake ranking overlay on top —
NOT a compilation of 6 separate clips.**

Every mega-viral example is a single oddly-specific viral clip (one guy on a
squeaky elliptical = "Chicken Screaming"; one POV waterslide; one spearfishing
dive; one hand spraying cologne; one leg cramping; one guy breaking his phone =
"Bad Day"). A 1–6 (or 1–7) numbered rail is overlaid on the LEFT and fills in with
short witty labels as that ONE clip plays out, holding the climax for last.

**Our RankZilla pipeline does the opposite** — it stitches 6 unrelated scraped
clips with generic sarcastic labels. That is why it fails. This is fixable.

## The exact anatomy (copy this)
1. **Format = one clip + overlay.** Pick ONE strong, oddly-specific viral clip that
   escalates to a payoff. The "ranking" is a retention game layered on it, not real.
2. **Burned title, top, two lines, centered:**
   `Ranking [ADJECTIVE] [TOPIC] [Moments]`
   - "Ranking" = **white**, ADJECTIVE = **RED** (Funniest / Craziest / Best /
     Hilarious), TOPIC = **YELLOW**, trailing word ("Moments"/"Screaming") = white.
   - Bold condensed font, thin black bar behind it. Identical every upload = brand.
3. **Rank rail, left side, 1–6 (or 7).** Numbers colored top-down (1 green/gold,
   2 orange, 3 gold/red, rest dark/white). Entries fill in **as the clip plays**
   with SHORT scene-specific witty labels + emoji:
   - RankZilla: "Almost died 😱", "Faceplant", "Ouch 🤕", "The burn 😖", "R.I.P
     phone 😭", "Hole in one ❌", "Level 1 💀", "15%", "30%", "-$140".
   - The labels ARE the comedy + the payoff. NEVER generic ("Nailed it", "Flawless").
4. **YouTube title field (metadata) = "DON'T CHECK THE SOUND 😭😭"** on nearly every
   upload, by ALL three channels. It's a curiosity/unmute hook (turns sound on,
   drives comments). Two-title system: metadata bait + on-screen topic.
5. **Oddly-specific / absurd / satisfying / ASMR niches.** Chicken Screaming, Toilet
   Design, Deep Sea Hunting, Physics Glitch, Muscle Cramp, Cologne Atomizers, Extreme
   Wind, Parachute, ASMR Fails, Bad Day. Weird + curiosity, NOT generic "funny fails".
6. **Tight ~15–30s.** Faint center watermark. Best/worst held for last.
7. **Shared niche motifs** exist (a bird-on-a-bare-tree "chicken" shot appears in
   BOTH RankZilla's and Pepe's "Chicken Screaming" videos) — the niche reuses bits.

## For the music channel (VoiceVsAutotune model)
Same skeleton: **bold solid YELLOW background** (own a color), on-screen title
"**No Autotune** VS **Autotune**" (teal/red), rank rail filling with **artist +
numeric score** (green good / red bad), often ONE artist per video, recognizable
artists, question metadata title "Who Sings Better?", tight 15–30s. Score = payoff
+ comment-war fuel.

## What this means for our pipeline (action)
The RankZilla pipeline must be rebuilt from "6-clip compilation + generic labels"
to **"one clip + witty escalating overlay"**:
- Input: one curated oddly-specific clip (+ optional a couple sub-beats).
- Overlay: brand title template + rank rail that reveals scene-specific witty labels
  in sync with the clip's beats; best held for last.
- Metadata: "DON'T CHECK THE SOUND 😭😭".
- Kill: generic fallback labels, random 6-clip stitching, 45–60s runtimes.
See [[competitors/rankzilla23]], [[competitors/peperanker]], [[competitors/voicevsautotune]].
