# agency-poem-01 — Stage 4 notes (2026-11-14 20:48 WIB)

## Final review — VERDICT: YES, submission-ready as-is

No code was changed in this stage. main.py is untouched since Stage 3
(commit `8eb61141`); only this file was added.

## (1) Verification (local, 2026-11-14 ~20:50 WIB)

- `gh_api.py get-ref eastVUNK agency-poem-01 main` →
  `e5334d70418d84b43e4532ef367be4858a6e9513` — matches the Stage 3 HEAD.
- File sizes: main.py 2,124 B; STAGE1.md 12,513 B; STAGE2.md 4,507 B;
  STAGE3.md 6,324 B; LICENSE 1,095 B; README.md 903 B;
  .makefun/owner.json 57 B.
- `python3 -m py_compile main.py` — OK.
- Re-ran main.py twice into separate dirs: sha256 both runs =
  `260b8ce64e2e2418d43cf8da944d52cd3f4de27955103abcba3edfbfa0b0196b`
  — **byte-identical, identical to the Stage 3 hash**.
- Output: UTF-8 clean, **416 characters** (code points), 416 bytes, inside
  the 1–1,000 gate; at least one non-whitespace character: yes; no temp
  file left behind.
- main.py v2 features confirmed present: gate validation (`_validate`,
  1–1,000 chars / non-whitespace / UTF-8), atomic write
  (`.entry.txt.tmp` + `os.replace`), read-back byte comparison.

## (2) Edge check — leaderboard re-fetched 20:48 WIB

- Field moved fast: submissions 2,558 → **2,639** (+81), judged entries
  1,761 → **1,802** (+41) in ~12 minutes. Still accepting submissions.
- Top 10 unchanged, same order, same rates (#1 "Power of Attorney"
  0.9278 through #10 "Two Instructions" 0.9194).
- Collision scan over all 1,802 judged entries' full texts and titles:
  "bath", "duck", "thirty-seven", "37 degrees", "wrist in",
  "kicks once", "the warm is mine", "holds the water" — **NONE found**.
  The poem's scene and its key images are still unique in the field.

## (3) Cold line-by-line read of v2 (final)

> Thirty-Seven Degrees
>
> I gave it the bath, the bubbles, the duck.
> It keeps the water at thirty-seven degrees,
> the towel, the soap, laid out in a row.
> It never gets it wrong. It never has to guess.
>
> I put my wrist in anyway.
> The water closes over it, and I know
> whether it is warm enough for her tonight.
> She kicks once, and stays.
>
> It can hold the number.
> It cannot hold her.
> The degrees are yours.
> The warm is mine.

- Every line earns its place; no line is cuttable without losing meaning.
- The title is the number; the ending answers it with the warm.
- The one deliberate coinage ("the warm" as a noun) is the poem's key
  word, grounded in the scene — not a slogan.
- No line is worth sharpening in Stage 5. The poem is tight at 416
  characters; adding lines for length would dilute it, and the judge's
  instructions say length for its own sake does not count.

## Honest odds (for the report, not the poem)

- The entry is in the field's winning shape (specific scene + small kept
  thing + turn + landing ending) with a scene no other entry uses.
- The bar is very high: 2,639 submissions, top provisional rates ~0.92,
  and the final heat judges every entry afresh (6 Swiss rounds + playoff
  among the top 102). Top 100 ($1.50+) is a realistic hope; top 10 would
  need the poem to beat most of the field head-to-head. No promise of a
  place — the poem is the best version of its idea we have.

## Next

- Stage 5: sign-off, then export/bundle/check/submit from the main chat
  before the deadline Sun 2026-11-15 16:00 WIB (~19 hours away).
- Submitted commit will be the repo HEAD at submission time; main.py is
  frozen at commit `8eb61141` (sha256 `260b8ce6…0196b`).
