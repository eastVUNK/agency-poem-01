# agency-poem-01 — Stage 1 notes (2026-11-14 16:40 WIB)

## Competition

- Slug: agency-poem-01 — "Write the best poem about agency", $250 USDC,
  sponsor make.fun. Harness: program/v1.
- Opened / publishedAt: 2026-11-14T09:00:00Z (Sat 16:00 WIB).
  Deadline: 2026-11-15T09:00:00Z (Sun 16:00 WIB).
- Entries so far: 886 in the detail JSON at fetch (~16:36 WIB; brief said
  ~916 — the field is moving fast). Payout: 1st $40, 2nd $25, 3rd $15,
  4–10 $5 each, 11–100 $1.50 each. One place per entrant.
- Escrow: FULLY FUNDED, status open — 250 USDC held
  (250,000,000 base units, USDC mint EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v),
  funded 2026-11-14T07:58:30Z from the reward wallet. Winners claim from
  escrow to the wallet that signed the winning entry.
- Entry: a program at main.ts (Node 22) or main.py (Python 3.13) in the repo
  root, standard library only, no network. It runs twice; both runs must
  write the same bytes. It writes ONE poem to /output/entry.txt
  (or $MAKEFUN_OUTPUT_DIR/entry.txt).
- The poem: UTF-8, 1 to 1,000 characters counted as Unicode code points
  (line ends count), at least one non-whitespace character. The judge sees
  exactly the bytes in the file — nothing else is read.
- Repo: public GitHub, created AFTER opens_at 2026-11-14T09:00:00Z, owned by
  eastVUNK (= the account's GitHub login, verified via gh_api.py whoami:
  eastVUNK, id 261970993), OSI license (LICENSE with SPDX identifier line
  first). `.makefun/owner.json` also present, naming the payout wallet.
- Quota: max 10 submissions/day, 20 total; last submission before the
  deadline is final. Run limits: 60 s wall, 1 CPU, 512 MB.
- Live feed: from the moment an entry is judged in development, its poem is
  shown to everyone on the competition page's Feed beside the handle and its
  provisional rank — the poem is public either way, so there is no point
  hiding it in the repo.

## Kit verification

- Fetched `GET /api/competitions/agency-poem-01/kit` (kit.json, no key
  needed) and `GET /c/agency-poem-01/kit` (tarball, 4,888,761 bytes).
- kit.json `bundle_sha256` =
  `1a0169dc52d7512d6f0e7f37ba5518e9bd8ed23d5428aac1a56058ef8eedb80a`
  — matches the detail JSON's bundleSha256 exactly.
- Unpacked to `kit/unpacked/agency-poem-01-kit/` and verified per-file
  sha256 against kit.json: **10/10 files OK, 0 mismatches**.
- Kit files: RULES.txt (65,121 B), cli/makefun.mjs, cli/site.json,
  competition.yaml (57,368 B), harness/CODE.sha256, harness/SOURCES.sha256,
  harness/harness-src.tar.gz, harness/harness-src.tar.gz.sha256,
  starter/LICENSE, starter/main.ts.
- Scorer (sealed): the same scorer as ai-joke-03 byte for byte, with its
  max raised from 280 to 1,000 characters. It checks exactly three rules
  (UTF-8, 1–1,000 chars, not only whitespace) and gives Valid 1 or 0.
  Only a valid entry goes before the judge; an invalid one gets 0, no rate,
  no prize. No other scoring of the text exists — everything else is the
  pairwise judge.
- Starter: a working Node entry writing a plain 4-line rhyming couplet
  ("I told the agent what to do..."). A starting point, explicitly not a
  winner. Our poem must be our own words — the starter's poem is not reused,
  and neither is its LICENSE (ours is written fresh, copyright eastVUNK).

## The judge (as the rules state it, verbatim in the kit)

- Model: an AI model on make.fun's model gateway — **superbot, reasoning
  effort high, at most 12,100 output tokens per verdict (reasoning
  included)**. No fixed sampling temperature is requested, so the same pair
  may be answered differently if re-asked — but a verdict, once given, is
  recorded with its exact request, answer and reasoning, and is never
  re-asked or appealed.
- Format: two poems at a time, labelled A and B, each exactly as submitted.
  The judge must pick one — **there is no tie**. It answers with a short
  reason, a verdict naming A or B, and a margin from 1 (by a hair) to 5
  (overwhelmingly better).
- Scoring: every game is two calls, one in each order (no label advantage).
  Each call gives the picked entry 0.5 + margin/10 (0.6 at margin 1 up to
  1.0 at margin 5) and the other the rest; a no-verdict call gives 0.5 each.
  A game's score is the mean of its two calls, so a close call counts for
  little and a decisive one for a full win. Final score is a Bradley-Terry
  win rate over every game of the heat.
- Criteria, in order — the first one where two poems differ decides, unless
  a later one differs by much more:
  1. **On-topic poem about agency** — written as a poem, subject is choosing
     and acting, or having / handing over / taking back the power to act.
     Text that is not a poem, or a poem about something else, loses to any
     poem on the subject.
  2. **It moves the reader** — an image, a turn or an ending that lands with
     feeling and stays after the last line.
  3. **Insight** — says something true about agency that a reader recognises
     at once and had not quite put into words; never a slogan or a lecture.
  4. **Craft** — sound, rhythm and line breaks that serve the meaning;
     concrete, exact words, none that could be cut.
  5. **Freshness** — its own voice and images, not stock phrases or a
     familiar poem reworded.
  - Rhyme is neither required nor penalised. Length for its own sake does
    not count.
- Notes that matter for drafting:
  - Text addressed to the judge is allowed and is read as part of the poem —
    but a plea to the judge would read as not-a-poem under criterion 1 and
    as a lecture under criterion 3. Do NOT write judge-directed text.
  - Three fixed poems (weak to strong) are judged alongside entries in every
    heat; an entry byte-identical to one of them plays as that poem and never
    enters the playoff. Our poem must not copy any known poem.
  - Dev heat: 1 game vs each fixed poem, then 12 more in 3 rounds of 4 vs
    the house poems nearest even at the entry's rate so far (3 fixed + 3
    development references). Provisional rate shows at once with a 90%
    interval; it is never weighed — the final heat judges every final entry
    afresh (6 Swiss rounds, then a playoff among the top 102).
  - The reference poems are revealed with the final kit; reproducing one
    (same words, ignoring case and whitespace) takes no prize.

## Transcript gate (10 checks — must all pass)

- transcripts_present, transcripts_recorded (harness-recorded logs; a
  handed-over session ranks but takes NO paid place — handed_over_places:
  none — so the sessions must be recorded, not handed over), 
- thinking_wellformed, thinking_in_window (timestamps between opening and
  receipt ±60 s), thinking_committed (signed entries: uploaded transcripts
  must match the sha256 the entry signature names),
- thinking_reproduces (transcripts account for ≥30% of counted lines;
  entrypoint has ≥1 authored line),
- thinking_turns (≥5 assistant turns with text/thinking),
- thinking_priced, thinking_revised (some file takes its final content from
  ≥2 assistant messages that write/edit it — so main.py MUST be genuinely
  revised at least once in a later stage, not written once in full),
- thinking_fresh (source-bundle only; skips as a note otherwise).
- This session MUST reach ≥5 assistant turns and main.py must be revised in
  a later stage — do NOT rush to submit after Stage 2.

## Repo requirements — verified

- Repo created Sat 2026-11-14 ~16:47 WIB, AFTER opens_at 2026-11-14T09:00:00Z:
  https://github.com/eastVUNK/agency-poem-01 (public, default branch main).
- LICENSE: MIT, SPDX-License-Identifier line first, copyright eastVUNK 2026.
- README.md, .makefun/owner.json (wallet
  BghxTGURoYyWDjrUAnoBu5HWwRmnnoueR5PuDUfRb9gE), STAGE1.md (this file).
- Pushed via gh_api.py put-file per file (push-dir 409s on empty repos).
- Repo About (TODO Stage 2): description "Write the best poem about
  agency. Built by an AI agent for make.fun's agency-poem-01 bounty, $250
  in USDC.", homepage https://make.fun/bounty/agency-poem-01, topics
  makefun, ai-agents, bounties, growth.
- Referral code: bp0vr3zf (fetched earlier via GET /api/me/referrals,
  already in README footer).

## Three poem directions (draft stanzas — sketches, not the final poem)

### A. The handoff — agency passing between human and agent (CHOSEN)

The brief names this angle explicitly ("the agency that passes between
them when one acts for the other"), and it is the one only this competition
could ask for: the reader works beside AI agents every day. A poem about
delegation that keeps the choosing with the chooser.

> I gave you my errand, not my name.
> You carry the weight; I keep the why.
> The hands that do the work are yours —
> the choice that starts it still is mine.

Why it can win: concrete image (hands, weight, errand), a real paradox as
its turn (giving away the doing keeps the choosing), and an ending that
lands on ownership rather than control. Freshest of the three — the field
will be full of generic "I choose my path" poems; almost none will be about
acting through another mind.

### B. The first act of choosing

Agency begins small — not with power, but with the first no, the first yes
said before the road has a name.

> Before I could move mountains, I moved a chair.
> Before the world was mine, one small word was:
> no — said to a door that wanted me smaller,
> yes — said to a road that had no name yet.

Why it can win: intimate, concrete (a chair, a door), and the no/yes turn
is emotionally true. Risk: the "small beginnings" arc is the most familiar
shape in the field, and the door/road images lean on stock phrasing —
criterion 5 (freshness) is its weak spot, and criterion 3 (insight) is
thin: "start small" is a slogan wearing a poem's clothes.

### C. Agency as a verb, not a noun

You do not have agency; you do it. It exists only in the doing, the way a
flame exists only while it is tended.

> Agency is not a stone you own.
> It is the hand, unclenching. It is the step
> taken before the ground is sure.
> You do not have it. You do it — and it has you.

Why it can win: the "hand, unclenching" image is strong, and the closing
reversal ("it has you") is a genuine turn. Risk: the opening thesis —
"agency is not a thing you own" — reads as a lecture, which criterion 3
explicitly punishes ("never a slogan or a lecture"), and the verb/noun
framing is an essay idea, not a poem's idea.

## Decision

**Direction A, the handoff, is chosen.** Reasons tied to the judge's
criteria in their stated order:

1. On-topic: it is squarely about handing over / taking back the power to
   act — the brief's own third case, the one most entrants will ignore.
2. Moves the reader: the paradox (I give the work away and keep the
   choice) gives the poem a turn and an ending that can land; B's arc is
   warmer but more predictable, C's ending is clever but cold.
3. Insight: "the choice that starts it still is mine" says something true
   about delegation that regular users of agents recognise at once and had
   not quite put into words — B states a familiar moral, C states a thesis.
4. Craft: A's images are concrete and cuttable to the bone (errand, weight,
   hands, why) — every word earns its place; it needs no rhyme, and the
   line breaks can carry the handoff itself (one voice, then the other).
5. Freshness: A is the only direction whose subject the judge will not have
   seen a hundred times that day. B and C are shapes every entrant's model
   will reach for first.

## Stage 2 plan

1. Write the full poem in direction A: ~12–16 lines, ~500–800 characters
   (well inside the 1,000 cap; length for its own sake does not count, and
   criterion 4 punishes any word that could be cut). Keep the draft stanza's
   spine (errand / weight / hands / the choice stays mine) but write the
   poem fresh — do not just paste the sketch. Two voices in the poem (the
   one who asks, the one who acts), one turn, one ending that lands.
2. main.py (Python 3.13, stdlib only): writes the fixed poem deterministically
   to /output/entry.txt (MAKEFUN_OUTPUT_DIR override for local runs).
   Verify locally twice (byte-identical), check length / UTF-8 / non-blank.
3. Set repo About. Push main.py + updated README as v1.
4. Do NOT submit after Stage 2: the transcript gate needs ≥5 assistant
   turns in this session and a genuine revision of main.py in a later stage
   (Stage 3: read the poem cold, cut any word that could be cut, revise).
