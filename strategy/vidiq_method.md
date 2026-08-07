# The vidIQ Method — the CEO's core playbook

The CEO runs the operation on vidIQ's data-driven method. Pipeline 2 already uses
vidIQ's API (`vq.py`, `vidiq_outliers`). This is the doctrine behind every brief,
every review, and every daily research pass. (Researched 2026-08-08 from vidIQ.)

## 1. How the Shorts algorithm actually distributes (design for this)
- **Explore & Exploit ("seed audience")**: every Short first gets a small test
  audience. Strong engagement → broader promotion; weak → it stalls. **We must win
  the seed test.** That means the hook and the first-viewer retention are everything.
- **The one signal that decides the test: "Viewed vs. Swiped Away."** Lower
  swipe-away = advance. So every creative choice is judged by: does this stop the
  swipe?
- **Rewatches/loops now count as extra views.** Design short, loopable payoffs — a
  satisfying #1, a punchline that makes people re-watch — to multiply views.
- **Engaged views** (real watches + likes + comments) are what count toward
  monetization (YPP) and revenue — not empty impressions.

## 2. The hook (80% of outcome)
- **First 3 seconds are the whole ballgame.** State the topic + tease the payoff
  in the opening frame. For ranking: open on the worst rank / tease #1. For kick:
  open on the hook line.
- Judge every short on its first frame + first line BEFORE anything else (review §5).

## 3. Length
- **13s or 60s perform best per vidIQ.** Our ranking target of 30–45s is fine, but
  test tighter 13–20s cuts and full 60s versions to find each channel's sweet spot.
- Never pad. Never cut mid-story to hit a number — pick shorter clips instead.

## 4. Packaging (earn the click AND the watch)
- **Title/description**: put the niche keyword in both. Ranking = two-line title,
  teal keyword, promise a payoff.
- **Hashtags**: `#shorts` + niche-relevant tags every time.
- **Custom thumbnail** (upload via YouTube mobile app) for when the Short surfaces
  in the regular feed — most visible asset there.
- **Say the topic out loud in the first seconds** so the algorithm categorizes it.

## 5. Niche & channel architecture (vidIQ niche validation)
- **Validate a niche**: confirm creators exist at every subscriber tier
  (0–10k, 10k–100k, 100k+). If they do, the niche pays and scales.
- **Content architecture** per channel:
  - **Pillar**: broad, high-traffic topics (our proven outlier shapes).
  - **Cluster**: specific long-tail spin-offs (Part 2/3, sub-niches).
  - **Bridge**: videos that connect clusters and keep sessions going.
- Keep each channel a **coherent niche** — the two ranking channels stay in
  separate lanes (see `playbook.md`).

## 6. Data-driven selection (outliers + keyword score)
- **Outlier finder** = the engine. Pull proven breakout topics
  (`python vq.py vidiq_outliers ...`), clone the *shape*, not the clip.
- **Keyword score**: chase keywords with high search + low competition for the
  title/topic. Track which title formulas move performance and double down.
- Especially high-leverage for channels **under 50k subs** (all three of ours).

## 7. Retention & session time
- Keep `avg % viewed` the north-star metric; views follow retention.
- Raise **session time**: end screens / pinned comment / "Part 2" pointing to the
  next Short keeps viewers on the channel — a subscribe reason too.

## 8. Consistency & volume
- **200+ published Shorts** is where channels see sustained growth — reinforces the
  90-day volume push. Post at peak audience times (Studio → Audience →
  "When your viewers are on YouTube").
- Experiment continuously; let data, not taste, pick winners.

## The daily loop, vidIQ-style
1. Pull outliers + keyword scores for each channel's niche.
2. Brief videos whose topic is a proven outlier shape, packaged with a scored
   keyword title, a 3-second hook, and a loopable payoff.
3. After posting, read swipe-away / avg % viewed; keep winners (Part 2), cut flops.
4. Log the new lesson to `../research/LEARNINGS.md`.
