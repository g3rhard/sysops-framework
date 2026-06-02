# SysOps Framework Scripts

This directory contains utility scripts for maintaining and generating content for the SysOps Framework documentation.

## 📊 Diagram Generator (`generate_diagrams.py`)

Generates high-quality PNG diagrams using matplotlib. Outputs to `content/assets/` at 300 DPI, ready for both web (Hugo) and PDF builds.

### Usage

```bash
# Generate all diagrams (default output: content/assets/)
.venv/bin/python scripts/generate_diagrams.py

# Custom output directory
.venv/bin/python scripts/generate_diagrams.py --output-dir ./custom-assets

# Custom DPI (default: 300)
.venv/bin/python scripts/generate_diagrams.py --dpi 150
```

### Available Diagrams

| File                              | Chapter | Description                        |
| --------------------------------- | ------- | ---------------------------------- |
| `agile-frameworks-comparison.png` | 4       | Scrum vs SAFe vs SysOps comparison |
| `sysops-framework-diagram.png`    | 3       | Multi-cycle operating model        |
| `sysops-roadmap.png`              | 5       | 6-month implementation roadmap     |
| `sysops-dashboard.png`            | 7       | KPI metrics dashboard              |

### Design System

Shared design tokens live in `diagrams/_design_system.py`. All diagram modules import from there — edit that file to change colours, fonts, or drawing primitives globally.

## 🔧 Prerequisites

- Python 3.8+
- `matplotlib` (install via `pip install -r requirements.txt` or the project venv)
- Validation of Mermaid syntax before file updates
- Template-based diagram generation for consistency
- Export to multiple formats (PNG, SVG, PDF) using Mermaid CLI
