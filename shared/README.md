# shared/

Reusable theme pieces will live here when a second deck needs them.

The underwater swimming-fish background is still inside the AquaTerra deck:

- `decks/aquaterra-title-defense/src/deck.js` (fish motion, cursor avoidance, M to pause)
- `decks/aquaterra-title-defense/src/deck.css` (ambient water, rays, waves)
- `decks/aquaterra-title-defense/src/build.py` (the `#amb` / `#fish` canvas markup)

It is tightly mixed with that deck's layout, so it was not extracted yet. When another deck needs the same background, move the JS/CSS/markup here and have both decks include it.
