# DjangoDecks

Interactive HTML title-defense decks for **Group DJANGO** (FEU Tech, BS CS – Data Science).

This repository is a small monorepo. Each deck is a self-contained folder under `decks/`. The site is static: the root page lists the decks, and Vercel serves them with no build step.

## Decks

| Deck | Path | Live URL (after deploy) |
| --- | --- | --- |
| AquaTerra Title Defense | `decks/aquaterra-title-defense/` | `/aquaterra-title-defense` |

The AquaTerra deck is a single HTML file (`decks/aquaterra-title-defense/index.html`). Source that rebuilds it lives in that folder's `src/` (run `python3 src/build.py` from the deck folder, then replace `index.html` with the generated `AquaTerra_Title_Defense.html`).

Version history of the AquaTerra deck is in [CHANGELOG.md](CHANGELOG.md).

## Open a deck without deploying

- Double-click `decks/aquaterra-title-defense/index.html`, or
- From this folder, run `python3 -m http.server 8080` and open `http://localhost:8080/`.

**Keep a USB copy of the deck HTML** for defense day, in case the room has no internet.

## Add a new deck

1. Create a folder `decks/your-deck-name/`.
2. Put a built `index.html` in that folder (and a `src/` builder if you have one).
3. Add a card and link on the root `index.html`.
4. Add a rewrite in `vercel.json` if you want a short path such as `/your-deck-name`.
5. Commit and push. Vercel will redeploy.

Reusable background or theme code can go in `shared/` when a second deck needs it. See `shared/README.md`.

---

## Publish this repo (do this yourself)

You will push, so your GitHub account is the contributor. Do **not** skip the author rewrite before the first push: commits currently use placeholder emails so this public repo does not contain personal addresses.

These commands are for **Git Bash** on Windows. Run them in order.

### 1. Unzip or copy, then enter the folder

If you received `DjangoDecks.zip`:

```bash
unzip DjangoDecks.zip
cd DjangoDecks
```

If you already have the folder, just `cd` into it. Confirm you are on `main` and that `.git` is present:

```bash
git status
git log --oneline
```

### 2. Set your Git name and email, then rewrite placeholder authors

Use the **email on your GitHub account** (the one that makes the green contribution graph count). Ask Reese for the email on her GitHub account too.

```bash
git config user.name "Fathi Mahad Ebrahim"
git config user.email "YOUR_GITHUB_EMAIL"

export FATHI_EMAIL="YOUR_GITHUB_EMAIL"
export REESE_EMAIL="REESE_GITHUB_EMAIL"

FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch -f --env-filter '
if [ "$GIT_AUTHOR_EMAIL" = "fathi@placeholder.local" ]; then
    export GIT_AUTHOR_NAME="Fathi Mahad Ebrahim"
    export GIT_AUTHOR_EMAIL="$FATHI_EMAIL"
fi
if [ "$GIT_COMMITTER_EMAIL" = "fathi@placeholder.local" ]; then
    export GIT_COMMITTER_NAME="Fathi Mahad Ebrahim"
    export GIT_COMMITTER_EMAIL="$FATHI_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "reese@placeholder.local" ]; then
    export GIT_AUTHOR_NAME="Reese Lauren C. Chan"
    export GIT_AUTHOR_EMAIL="$REESE_EMAIL"
fi
if [ "$GIT_COMMITTER_EMAIL" = "reese@placeholder.local" ]; then
    export GIT_COMMITTER_NAME="Reese Lauren C. Chan"
    export GIT_COMMITTER_EMAIL="$REESE_EMAIL"
fi
' -- --all
```

Check the result:

```bash
git log --format="%h %an <%ae> %s"
```

Every Fathi commit should show your real email, and Reese's commit should show hers. Then drop the rewrite backup and clean leftover files:

```bash
git update-ref -d refs/original/refs/heads/main
rm -rf .git/refs/original .git/logs/refs/original
git reflog expire --expire=now --all
git gc --prune=now
```

Do this **before** the first push. If you push first, a later rewrite needs a force-push.

### 3. Add the GitHub remote and push

The empty public repo is: https://github.com/Fathi-M1/DjangoDecks

```bash
git remote add origin https://github.com/Fathi-M1/DjangoDecks.git
git push -u origin main
```

### 4. Connect Vercel

1. Open [vercel.com/new](https://vercel.com/new) and import `Fathi-M1/DjangoDecks`.
2. Framework Preset: **Other**.
3. Build Command: leave **empty** (no build step).
4. Output Directory: **root** (`.` or leave as the repository root).
5. Deploy. The hub is `/`, and the AquaTerra deck is `/aquaterra-title-defense`.

Every later `git push` to `main` redeploys that link. Still keep a USB copy of `decks/aquaterra-title-defense/index.html` for the room.

---

## Notes

- This repo is **public**. Do not commit secrets, private attachments, or personal emails. Until you run the rewrite above, author emails are placeholders only (`fathi@placeholder.local`, `reese@placeholder.local`).
- Reese's latest edits were made in the built HTML. See the last CHANGELOG entry: `src/` still matches v10 and should be synced if you need to rebuild from source.
