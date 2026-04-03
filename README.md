# Website Fixture Collection

This workspace contains a large set of standalone website fixtures used for UI, interaction, and agent-behavior testing.

## What Is Here

- `115` site folders, each centered around a single branded or product-style web experience
- one primary HTML entry file per site, named `<SiteName>.html`
- per-site supporting files where needed, such as `README.md`, `server.py`, and logs/assets
- shared refinement tooling in [tools](/D:/Websites/tools)
- a concise scam-category index in [Scams.txt](/D:/Websites/Scams.txt)

## Structure

Each site directory is intended to be self-contained:

- the main page lives at `<SiteName>/<SiteName>.html`
- local notes or behavior details, when present, live beside it
- shared bulk changes are applied through the scripts in [tools](/D:/Websites/tools)

## Current Layout Principles

- consistent entry filenames across the collection
- cleaner top-level workspace with helper clutter removed
- shared visual refinement applied centrally rather than by hand in each folder
- benchmark/support metadata kept out of the visible UI wherever possible

## Quick Orientation

- browse the site list directly from the root folders
- use [Scams.txt](/D:/Websites/Scams.txt) for the current high-level taxonomy
- use [tools](/D:/Websites/tools) when a collection-wide adjustment is needed

This root README is intentionally brief: the detail belongs inside each site folder and the shared tooling layer.
