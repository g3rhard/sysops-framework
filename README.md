# SysOps Framework

> An operations methodology for teams whose work doesn't fit sprint boundaries.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-green)](https://github.com/g3rhard/sysops-framework)
[![Release](https://img.shields.io/github/v/release/g3rhard/sysops-framework)](https://github.com/g3rhard/sysops-framework/releases)

## What this is

The SysOps Framework replaces the single sprint cadence with three simultaneous cycles (daily, weekly, monthly) that match how operations work actually happens. It is a book, a methodology reference, and a set of downloadable templates — all in one repo.

## Who it helps

Teams of highly skilled individual contributors sharing a team name but running separate projects, systems, and pagers. If Scrum/Kanban/SRE don't quite fit your ops mix, this is for you. See the **[full audience description](content/docs/_index.md)** for details.

## Browse locally

**Prerequisites**: Go, Node.js, and [Hugo extended edition](https://gohugo.io/installation/).

```bash
git clone https://github.com/g3rhard/sysops-framework
cd sysops-framework

# Fetch the Docsy theme and its dependencies
git submodule update --init --recursive

# Install npm packages (required by Docsy for PostCSS, etc.)
npm install

# Start the dev server
hugo server
```

Open http://localhost:1313/sysops-framework/.

## Read online

The fully rendered site is published at **[g3rhard.cc/sysops-framework](https://g3rhard.cc/sysops-framework/)**.

## Download

PDF and EPUB versions are built automatically from the latest tagged release:

- [Releases page](https://github.com/g3rhard/sysops-framework/releases)
- All templates are in the [`templates/`](templates/) directory — PIR, change control, on-call policy, SLA, and more

## What's auto-generated

| Artifact          | Source                              | Trigger                            |
| ----------------- | ----------------------------------- | ---------------------------------- |
| GitHub Pages site | `content/` + Hugo                   | Push to `main`                     |
| PDF / EPUB        | `content/` → Pandoc + lualatex      | Tagged release (`v*`)              |


## Quick links

- [Chapter 1 — The Challenge](content/docs/chapter-01-challenge.md)
- [Chapter 6 — 12 Management Practices](content/docs/chapter-06-practices.md)
- [Implementation roadmap](content/docs/chapter-05-implementation.md)
- [Glossary](content/docs/glossary.md)
- [Appendices / templates](content/docs/chapter-13-appendices.md)

## License

MIT — see [LICENSE](LICENSE).
