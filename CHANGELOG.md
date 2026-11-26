# Changelog

AquaTerra title-defense deck, recorded in order. Dates are Asia/Singapore (UTC+8).

## v12 (27 Nov 2026, 2:00 AM Asia/Singapore)

Add Methodology section (data preparation by Pacate, forecasting and value at risk, evaluation) and sync Reese's edits.

- Reese's edits ported into `src/` (cover title "in MIMAROPA", GAMM spelled out, municipal-fisheries definition, MIMAROPA Q3 2025 figure, Research Gaps wording, SO 2 MAE-reduction wording, Limitations heading). Mangrove items excluded (mangroves were dropped).
- New slides 06–08: Methodology: Data Preparation (sources, collect and clean, time split, impute and validate, align and join), Methodology: Forecasting and Value at Risk, Methodology: Evaluation. Potential Clients is now 09 and Thank you 10.
- `build.py` now writes `index.html` directly. README rewritten.

## Reese edit (27 Nov 2026, 1:00 AM Asia/Singapore)

Edits by Reese Lauren C. Chan, made on the built `index.html` (on top of v10). **`src/` was not updated** and still builds the v10 wording. If you need to rebuild from source, port these changes back into `src/` first.

What changed in the built deck:

- Cover title now ends with “in MIMAROPA” instead of “in Selected Philippine Coastal Provinces”.
- Area of Investigation: Inputs add mangrove change (USGS Landsat Collection 2, 2023); Process spells out “Generalized Additive Mixed Model (GAMM)”.
- New sentence defining municipal fisheries: municipal waters up to 15 km from shore, no boat or a boat of 3 gross tons or less.
- Background adds a MIMAROPA-specific figure, kept separate from the national 45M kg/year loss: marine municipal production was 31,073.75 MT in Q3 2025, down 9.2% year on year (PSA RSSO MIMAROPA, 2025).
- Research Gaps: existing forecasts are described as regional across the Philippines; AquaTerra will work at the province × fish-category level within MIMAROPA.
- SO 2 now measures predictor contribution using reductions in MAE, with vs without those predictors on held-out quarters.
- Scope public-data list adds Global Mangrove Watch; the Limitations heading no longer says “click to focus”.
- Section labels: slide 06 kicker becomes “VI · Datasets”; slide 07 becomes “VII · Algorithms” (GAMM spelled out in the workflow card); Potential Clients becomes “VIII”.
- References add U.S. Geological Survey (2023), Landsat Collection 2.

## v10 (26 Nov 2026, 9:41 PM Asia/Singapore)

Restore the v7 swimming-fish design and keep the v9 content and structure.

Keeps Area of Investigation, the hidden nav toggle, and the questions close from v9, but restores the v7 light underwater theme with swimming fish. The illustrated-ocean scene.py is removed. This commit also adds the DjangoDecks monorepo layout (root hub page, Vercel config, shared/ note, tests with relative paths).

## v9 (26 Nov 2026, 9:41 PM Asia/Singapore)

Hide the nav bar behind a toggle, add Area of Investigation, and close on questions.

The bottom nav bar is hidden by default and can be opened with a small toggle. New Area of Investigation slide (what the study covers) sits before Background (why). The closing slide is a short thank-you and an invitation for questions. The Q&A bank and Prediction vs. Causation move to backup slides B1 and B2.

## v8 (26 Nov 2026, 9:31 PM Asia/Singapore)

Try an illustrated ocean scene (later reverted).

Adds an illustrated ocean backdrop (coral, kelp, jellyfish, turtle) via scene.py, with a frosted glass panel over the content for contrast. This look was later dropped in favour of the v7 swimming-fish design.

## v7 (26 Nov 2026, 8:52 PM Asia/Singapore)

Add swimming fish in the background and put group identity and members on the cover.

Canvas fish swim slowly behind the cards and move away from the cursor (M still freezes motion). Cover hook lines are larger. A cover card shows Title Defense, Group DJANGO, BS CS – Data Science, FEU Tech, and the four members.

## v6 (26 Nov 2026, 8:42 PM Asia/Singapore)

Restore the underwater background, add ambient motion, and use plain slide titles.

Drops the FEU template background and returns to the underwater theme. Adds subtle ambient motion (toggle with M). Slide titles are plain descriptive headings (for example, Statement of the Problem and Specific Objectives; Data and Evaluation Overview).

## v5 (26 Nov 2026, 5:49 PM Asia/Singapore)

Switch to the FEU template background and add Research Gaps, MIMAROPA, and one-to-one SOP/SO.

Uses the FEU template background. Content is updated to the current study: MIMAROPA, 31 fish categories, Research Gaps, and SOP/SO pairs mapped one-to-one. Data window runs through 2025 with a 70/15/15 split.

## v4 (26 Nov 2026, 5:01 PM Asia/Singapore)

Drop mangrove change from the study and update the related slides.

Mangrove cover is no longer a study predictor. Wording now tests typhoon exposure, rainfall and sea surface temperature as forecast inputs, and mangrove imagery is removed from the slides.

## v3 (26 Nov 2026, 3:22 PM Asia/Singapore)

Enlarge the spotlight panel, use the notched slide path, and bump fonts.

Slides fill more of the screen (notched spotlight clip-path, panel_path.txt). Headings move into the top band, body and citation fonts are slightly larger, and the cover layout is tightened.

## v2 (26 Nov 2026, 3:10 PM Asia/Singapore)

Fold the title into the cover and drop the standalone Title slide.

The cover now carries the title and key terms. The old page-01 Title slide is gone. Adds a section rail and Landsat / FEU background image support in the build.

## v1 (26 Nov 2026, 2:48 PM Asia/Singapore)

Initial underwater-theme AquaTerra title defense deck.

First saved version of the deck. Underwater theme, standalone Title slide, early slide set (background, objectives, scope, pipeline, algorithms, clients) and backup Q&A / prediction-vs-causation slides.
