# DjangoDecks

Interactive HTML decks by Group DJANGO.

## Decks

| Deck | Folder |
| --- | --- |
| AquaTerra Title Defense | `decks/aquaterra-title-defense/` |

## Folder layout

```
decks/<name>/
  src/        slide content, styles and scripts (edit these)
  src/build.py  builds the deck into one file
  index.html  the built deck (single file, works offline)
  img/        images embedded at build time
  test/       layout and screenshot checks
shared/       notes and pieces shared across decks
index.html    hub page linking to every deck
```

## Open or rebuild a deck

- Open: double-click `decks/<name>/index.html` in any browser. Arrow keys move through slides; `?` lists all keys.
- Rebuild after editing `src/`:

```
cd decks/<name>/src
python3 build.py
```

- Check layout (needs Playwright): `python3 decks/<name>/test/test.py`

Always edit `src/` and rebuild. Edits made only in `index.html` are lost on the next build.

## Add a new deck

1. Copy an existing deck folder to `decks/<new-name>/`.
2. Replace the slides in `src/slides.py` (and `src/data.py` for Q&A and references).
3. Run `python3 build.py` in `src/`.
4. Add a row to the table above and a link in the root `index.html`.

## Deck conventions

- Plain, descriptive slide titles; no slogans.
- Readable from the back of the room: body text at least 22px, labels at least 18px at 1920×1080.
- Proposal decks use future tense ("we will…").
- Sources from 2020 onward; any older foundational or legal source is listed separately.
- Invented example numbers are labelled ILLUSTRATIVE.
- Motion stays subtle; `M` toggles it and reduced-motion settings are respected.
