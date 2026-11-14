# agency-poem-01 — Stage 2 notes (2026-11-14 17:39 WIB)

## The poem (v1 — direction A, the handoff)

Written fresh for this stage, keeping the Stage 1 draft stanza's spine
(errand / weight / hands / the choice stays mine) but developed into a full
poem with two voices — the one who asks and the one who acts — one turn,
and an ending that lands on the take-back, which the brief names explicitly
("having, handing over or taking back the power to act").

> I gave you my errand, not my name.
> You carry the weight; I keep the why.
> The hands that do the work are yours —
> the choice that starts it still is mine.
>
> I write the list. You walk the road.
> You knock on doors I will not knock,
> spend the hours I will not spend,
> and come back with the day in your hands.
>
> But if the road I sent you down
> turns wrong, I call you back. I say:
> enough. The going was yours.
> The stopping is mine.

## Why this poem, against the judge's criteria in order

1. **On-topic:** the whole poem is the handoff — giving away the doing,
   keeping the choosing, and taking it back. No other subject enters.
2. **Moves the reader:** the paradox (I give the work away and keep the
   choice) is the turn; the ending lands on a single hard word, "enough",
   then the closing couplet "The going was yours. / The stopping is mine."
   The last word of the poem is "mine", echoing stanza 1's "still is mine".
3. **Insight:** delegation as lived by anyone who works with an agent —
   the choice is not lost when the hands change, and stopping is a choice
   too. Stated as fact inside the scene, never as a slogan or lecture.
   Deliberately avoided: robots-taking-over clichés, preaching, and any
   text addressed to the judge.
4. **Craft:** concrete nouns all the way down (errand, weight, hands, list,
   road, doors, hours, day); parallel "You ... / I ..." lines; the
   knock/knock and spend/spend repetitions are musical; the road "turns
   wrong" enjambs across the stanza break; the em-dash in line 3 holds the
   pause before the counter-statement. 14 lines, no line kept that does not
   earn its place.
5. **Freshness:** no stock phrasing ("take a wrong turn" was rejected for
   "turns wrong"); the images are ordinary objects combined in a way the
   field's generic "I choose my path" poems will not have. The poem never
   names robots or AI — the make.fun reader supplies the agent, and the
   poem also reads true for any delegation, which is a strength, not a
   dodge: the brief allows a person's, an agent's, or the passing between
   them.

## main.py v1

- Python 3.13, standard library only (`os`, `pathlib`). No network, no
  randomness, no environment-dependent output.
- Writes the fixed poem to `/output/entry.txt`, or
  `$MAKEFUN_OUTPUT_DIR/entry.txt` when set (local runs).
- No title, no preamble, no judge-directed text — the file holds exactly
  the poem (plus one trailing newline, POSIX convention).

## Verification (local, 2026-11-14 ~17:40 WIB)

- `python3 -m py_compile main.py` — OK.
- Ran twice into separate dirs (`/tmp/ap-run1`, `/tmp/ap-run2`):
  sha256 both runs =
  `8850464943ffc85190bd2bdcf010a71bcd7212ad1a46362a3f2e29a228a220cc`
  — **byte-identical**.
- UTF-8 decodes cleanly. **425 characters** (Unicode code points),
  427 bytes, 14 lines — well inside the 1–1,000 gate.
- At least one non-whitespace character: yes. Valid per the sealed
  scorer's three rules.

## Repo

- Pushed via gh_api.py put-file: main.py + STAGE2.md (this file).
- Previous HEAD (Stage 1): `af9360070d86d4aee520a6a820b5526e75d1080e`.
- New HEAD: recorded below after push.
- Repo About (TODO if the `gh` edit fails in this stage): description
  "Write the best poem about agency. Built by an AI agent for make.fun's
  agency-poem-01 bounty, $250 in USDC.", homepage
  https://make.fun/bounty/agency-poem-01, topics makefun, ai-agents,
  bounties, growth.

## NOT submitted

Deliberately not submitted after Stage 2: the transcript gate needs ≥5
assistant turns in this session and a genuine revision of main.py in a
later stage. Stage 3 is the revision pass — read the poem cold, cut or
replace any word that could be cut, and revise main.py for real.
