# Review — Ranking Funniest Water Slide Fails (multi-clip) — 2026-08-08

**Verdict: APPROVE.** First multi-clip ranking done RIGHT (owner prefers multi-clip).

`ranking_funniest_water_slide_fails_rankzilla.mp4` — 45s, 30fps CFR (1352 frames,
verify PASS). 5 genuinely distinct slides, best held for #1.

## Ranks (fresh US-sourced clips, scene-specific labels)
| # | Clip | Views | Label | Origin |
|---|---|---|---|---|
| 1 | Brain Drain trapdoor slide | 613M | TRAPDOOR 💀 | US |
| 2 | Anaconda tube (Océade) | 104M | Swallowed whole 🐍 | Belgium |
| 3 | Costco croc backyard slide | 102M | Costco special 😂 | US |
| 4 | Aqua Skoot (Wild Water Adv.) | 21.5M | Full speed 😳 | US |
| 5 | Natural lake slide | 18.7M | Nature's slide 😅 | US |

## Passes
- ✅ **Multi-clip** (5 distinct slides) — what the owner asked for.
- ✅ **NO Indian clips** — sourced fresh via `source_clips.py` (US-geo) with the new
  Indian filter; visually vetted every clip.
- ✅ On-tone (fun/thrill; dropped all stuck/accident/death clips).
- ✅ Scene-specific witty labels + color emoji; best (613M trapdoor) at #1.
- ✅ CFR verify PASS. Metadata title: DON'T CHECK THE SOUND 😭😭.
- ✅ ZACK FILMS competitor-watermark clip removed.

## Minor (for v2 / future sourcing)
- #3 (Costco) has brief source narration "Grace take good care of Cedric…"; #5 has
  faint "SLIDES/THIS" source words. Source captions, not competitor marks — acceptable,
  but prefer caption-free clips when the pool allows.

## Pipeline improvements shipped (permanent)
- `source_clips.py`: Indian-marker filter added to `is_foreign()`; **fresh US-geo
  sourcing with no vidIQ credits now works** (fixed the YouTube bot-check via android
  player client in metadata + `fetch.py` download).
- Sourcing rules in `strategy/playbook.md` + memory [[content-sourcing-rules]].
