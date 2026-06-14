# Contributing to SysOps Framework

## Before you start

- Read the **[TODO](TODO.md)** to see what's planned and in progress.
- Read the **Style Guide** below before writing or editing content.

---

## Style Guide

### Language

- **Variant**: US English (`-ize` spellings — organize, prioritize; `-or` — behavior, color; `-er` — center, meter; `-ed` — learned, spelled)
- **Exceptions**: Direct quotes and URLs preserve their original spelling
- **Pronouns**: "they" as singular when gender is unknown or irrelevant

### Voice & Tone

- **Audience**: Interrupt-driven ops teams — highly skilled, sceptical of process, tired of agile cargo-cults
- **Voice**: Direct, opinionated, human. Mix dense reference with jokes, stories, and wry asides
- **What to avoid**: Passive voice, weasel words ("synergize", "leverage", "robust"), corporate blandness
- **Rule of thumb**: If a sentence would sound wrong spoken aloud in a team standup, rewrite it

### Headings

- **H1** (`#`): Never used in chapters (reserved for site title)
- **H2** (`##`): Chapter sections — learning objectives, major topic areas
- **H3** (`###`): Subsections within a topic
- **H4** (`####`): Sub-subsections or component breakdowns
- **Rule**: No skipped levels. Never jump from H2 to H4.
- Every heading must be descriptive enough to navigate by — "Results" is too vague, "DR Test Results" is fine

### Emoji

- **Safe emojis** (render correctly in PDF): 📊, 🚨, 🔄, 📈, 📚, 👥, 🤝, 🚀, 🗄️, 🎫, 💰, 🔒, 🛡️, ⚡, 💡, 🎯, 🔮, 💭, 🎮, 🏆, ✅
- **Unsafe emojis** (may not render in PDF): Flags (🏴), skin-toned emojis, newer Unicode additions
- **Rule**: Don't overuse. Max 1 emoji per heading, sparingly in body text

### Callouts

Pattern: `> **Label**. Text`

| Callout       | Label                  | When to Use                                            |
| ------------- | ---------------------- | ------------------------------------------------------ |
| Note          | `> **Note.**`          | Supplementary information                              |
| Reality check | `> **Reality check.**` | Cynical/realistic counterpoint to aspirational content |
| Warning       | `> **Warning.**`       | Critical caution — ignoring this has real consequences |
| In practice   | `> **In practice.**`   | Concrete implementation advice from experience         |
| Template      | `> **Template:**`      | Cross-reference to an appendix template                |
| Invariant     | `> **Invariant**`      | What stays the same when technology changes            |
| Audience      | `> **Audience**`       | Who should pay attention to a specific section         |
| Pro tip       | `> **Pro tip.**`       | Practical shortcut or advice                           |

### Tables

- Use `|---|---|---|` separators consistently
- Left-align text columns, right-align numbers
- Every table must have a header row
- Tables wider than 5 columns should be avoided — split into two tables

### Code Blocks

- ` ```yaml` for YAML configurations
- ` ```bash` / ` ```sh` for shell commands
- ` ```rego` for OPA/Rego policies
- ` ```text` for form templates and log examples
- ` ```mermaid` for diagrams — always preceded by a `> **Diagram**:` alt-text caption
- Inline code `` `like this` `` for file names, commands, variables, and tool names

### Citations

- **Format**: Inline Markdown link immediately after the claim — `([source name](URL))`
- **First occurrence only** in each chapter
- **Link to specific section**, not the homepage
- Use the approved source registry in `TODO.md` — do not cite blog posts, vendor marketing pages, Wikipedia, or unofficial tutorials

### File Naming

- Markdown files: `chapter-NN-topic.md` (`NN` = zero-padded chapter number)
- Assets: descriptive kebab-case, stored in `static/assets/`
- Templates: kebab-case, stored in `templates/`

### Diagrams

- All diagrams use Mermaid syntax (` ```mermaid`)
- Every diagram must have a `> **Diagram**: [description]` caption immediately above the code block
- Diagram captions must be meaningful for accessibility — describe the relationships shown, not just the title

### Appendices

- Tick-box checklists and detailed templates live in `chapter-13-appendices.md`
- Chapters keep the narrative — point to the appendix for granular material

### Review Checklist

Before submitting a PR, verify:

- [ ] US English spelling (-ize, -or, -er, -ed)
- [ ] No passive voice where active would do
- [ ] Headings follow hierarchy (no skipped levels)
- [ ] Every Mermaid diagram has an alt-text caption
- [ ] Citations link to primary sources, not Wikipedia
- [ ] No fabricated links (no "coming soon" or "see community page" without a real URL)
- [ ] Jokes and asides preserved — the book should not read like a corporate document

---

## Ways to Contribute

### Documentation Improvements

- Fixing typos, grammar, or formatting issues
- Clarifying explanations or adding examples
- Improving chapter organization or flow
- Adding visual diagrams or illustrations
- Adding real-world case studies with citations to documented, publicly verifiable incidents

### Framework Development

- Refinements to core principles or practices
- New templates in `templates/`
- OPA Rego policies, Kyverno rules, automation scripts
- Implementation guidance and best practices

### Translations

- Translating content to other languages
- Adapting examples for different cultural contexts

## How to Contribute

1. **Fork the repository** and create a feature branch
2. **Follow the style guide** above
3. **Include citations** for any research or external sources
4. **Test your changes** — run `hugo server` and verify the build is clean
5. **Submit a pull request** with a clear description of changes

### Branch naming

- `docs/<topic>` — documentation changes
- `fix/<topic>` — bug fixes
- `feat/<topic>` — new features

### Content Guidelines

- **Accuracy**: All technical information must be correct and current
- **Clarity**: Write for diverse experience levels; use simple, direct language
- **Practical focus**: Include concrete examples, not abstract descriptions
- **Anonymization**: Remove or disguise sensitive organizational information in case studies
- **Attribution**: Properly credit sources and contributors

## What not to contribute (yet)

- Gamification elements — tracked as P3 in TODO; design not finalized
- Interactive exercises — same, P3
- Training/certification materials — not scoped

## PR checklist

- [ ] US English spelling (`-ize`, `-or`, `-er`, `-ed`)
- [ ] Headings follow hierarchy (no skipped levels)
- [ ] Every Mermaid diagram has an `> **Diagram**:` alt-text caption
- [ ] Links go to primary sources, not Wikipedia
- [ ] No fabricated URLs ("coming soon", "see community page")
- [ ] Runs clean through `markdownlint-cli2`

## License

By contributing, you agree your contributions are licensed under MIT.
