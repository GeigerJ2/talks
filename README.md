# talks

Every talk, poster and workshop in one place, one directory per event under
`slides/`, named `YYYY-MM-DD-venue-topic`.

Each directory has a `README.md` giving the venue, the date, a link to the
Google Slides deck where one exists, and a link to the GitHub repo the material
came from. Recent decks are [Slidev](https://sli.dev); older ones are
PowerPoint, Inkscape or marp.

`figs/` is the shared figure store: logos, portraits, QR codes. Slidev only
serves assets from a deck's own `public/`, so each Slidev deck symlinks `public`
to it and refers to figures as root-absolute paths, `/logos/psi.png` for
`figs/logos/psi.png`.

A talk's `media/` directory holds its videos, PowerPoint originals, Blender
scenes and multi-megabyte Inkscape figures. Those are on disk but not in git,
because together they run to about 1.6 GB. Anything at or above 1 MB goes there,
and the per-talk GitHub repos still hold copies. Put new heavy files in `media/`
rather than loosening `.gitignore`.

`notes -> ~/notes` is a local convenience symlink, excluded through
`.git/info/exclude` rather than `.gitignore` so it never reaches a clone.
