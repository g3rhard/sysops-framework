"""
Agile Frameworks Comparison Chart for Chapter 4

Portrait A4 layout: the three frameworks are stacked as full-width rows so the
diagram reads well on a printed page.  Each framework row has a coloured header
(name + cadence) and a two-column body:
  • Left column  : Key Characteristics (5 bullets)
  • Right column : Best Used For (3 bullets) + Limitations (2 bullets)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _design_system import (
    COLORS, FONTS, setup_figure, set_lims,
    draw_card, draw_section_label, _rounded_rect,
    bullet_list,
)
import matplotlib.patches as mpatches

# ── Layout constants (A4 portrait) ────────────────────────────────────────────

_FIG_W, _FIG_H  = 8.5, 11.0
_XLIM           = (0.0, 8.5)
_YLIM           = (0.0, 11.0)

_CARD_X         = 0.35
_CARD_W         = 7.80
_CARD_TOP       = 10.05   # top edge of the first (Scrum) card
_CARD_H         = 3.05
_CARD_GAP       = 0.28
_HEADER_H       = 0.50
_RADIUS         = 0.16

_COL_SPLIT      = _CARD_X + _CARD_W / 2 + 0.05   # x where right column begins
_COL_W          = _CARD_W / 2 - 0.30             # usable width of each column

_BULLET_DY      = 0.32   # vertical spacing between bullets
_LABEL_GAP      = 0.40   # gap from a section label down to its first bullet
_SECTION_GAP    = 0.30   # gap between Best-For block and Limitations label

# ── Framework data ────────────────────────────────────────────────────────────

_FRAMEWORKS = [
    {
        "name":    "Scrum Framework",
        "color":   COLORS["scrum"],
        "cadence": "1–4 week sprints",
        "characteristics": [
            "Fixed-length sprint cadence",
            "Story points & velocity",
            "Sprint commitments & DoD",
            "Definition of Done gates",
            "Retrospectives each sprint",
        ],
        "best_for_label": "Best For: New Product Development",
        "best_for": [
            "Predictable requirements",
            "Project-based timelines",
            "Dedicated development teams",
        ],
        "limits": [
            "Emergencies cause scope creep",
            "Poor fit for unplanned work",
        ],
    },
    {
        "name":    "SAFe Framework",
        "color":   COLORS["safe"],
        "cadence": "8–12 week program increments",
        "characteristics": [
            "Program Increments (PI)",
            "Multiple team coordination",
            "Quarterly release trains",
            "Portfolio-level planning",
            "Agile Release Trains (ART)",
        ],
        "best_for_label": "Best For: Large Organisations",
        "best_for": [
            "50+ person programmes",
            "Quarterly roadmap alignment",
            "Enterprise portfolio management",
        ],
        "limits": [
            "High overhead for small teams",
            "Slow to pivot mid-increment",
        ],
    },
    {
        "name":    "SysOps Framework",
        "color":   COLORS["sysops"],
        "cadence": "Daily / weekly / monthly cycles",
        "characteristics": [
            "Continuous multi-cycle flow",
            "Service reliability metrics",
            "Risk-based work prioritisation",
            "Interruptions are expected",
            "On-call & incident-first",
        ],
        "best_for_label": "Best For: Operations Teams",
        "best_for": [
            "24/7 production services",
            "Mixed reactive/proactive work",
            "High-availability requirements",
        ],
        "limits": [
            "Not designed for greenfield dev",
            "Requires operational maturity",
        ],
    },
]


# ── Diagram builder ───────────────────────────────────────────────────────────

def create_diagram():
    """Create the agile frameworks comparison chart for Chapter 4."""
    fig, ax = setup_figure(
        figsize=(_FIG_W, _FIG_H),
        title="Framework Comparison: Scrum vs SAFe vs SysOps",
        title_y=0.975,
    )
    set_lims(ax, _XLIM, _YLIM)

    for i, fw in enumerate(_FRAMEWORKS):
        color = fw["color"]
        top    = _CARD_TOP - i * (_CARD_H + _CARD_GAP)
        bottom = top - _CARD_H

        # ── Card body (no built-in header — we draw a custom one) ─────────────
        draw_card(ax, _CARD_X, bottom, _CARD_W, _CARD_H, color,
                  title=None, radius=_RADIUS)

        # ── Custom header band: name (left) + cadence (right) ─────────────────
        hb_y = top - _HEADER_H
        _rounded_rect(ax, _CARD_X, hb_y, _CARD_W, _HEADER_H, color,
                      edge_color="none", lw=0, radius=_RADIUS, zorder=3)
        ax.add_patch(mpatches.Rectangle(
            (_CARD_X, hb_y), _CARD_W, _HEADER_H / 2,
            facecolor=color, edgecolor="none", zorder=3,
        ))
        ax.text(_CARD_X + 0.32, hb_y + _HEADER_H / 2, fw["name"],
                ha="left", va="center",
                fontsize=13, fontweight="bold", color=COLORS["white"], zorder=4)
        ax.text(_CARD_X + _CARD_W - 0.32, hb_y + _HEADER_H / 2, fw["cadence"],
                ha="right", va="center",
                fontsize=9.5, fontweight="bold", color=COLORS["white"],
                alpha=0.95, zorder=4)

        interior_top = hb_y - 0.22
        col_l_x = _CARD_X + 0.12
        col_r_x = _COL_SPLIT

        # ── Left column: Key Characteristics ─────────────────────────────────
        draw_section_label(ax, col_l_x + 0.04, interior_top, _COL_W,
                            "Key Characteristics", color, fontsize=10)
        bullet_list(ax, col_l_x, interior_top - _LABEL_GAP,
                    fw["characteristics"], dy=_BULLET_DY, fontsize=9.5,
                    color=COLORS["mid"], indent=0.28)

        # ── Right column: Best Used For ───────────────────────────────────────
        draw_section_label(ax, col_r_x + 0.04, interior_top, _COL_W,
                            fw["best_for_label"], color, fontsize=10)
        y_bf_first = interior_top - _LABEL_GAP
        bullet_list(ax, col_r_x, y_bf_first,
                    fw["best_for"], dy=_BULLET_DY, fontsize=9.5,
                    color=COLORS["mid"], indent=0.28)

        # ── Right column: Limitations (below Best For) ────────────────────────
        y_bf_last  = y_bf_first - (len(fw["best_for"]) - 1) * _BULLET_DY
        y_lim_lbl  = y_bf_last - _SECTION_GAP
        draw_section_label(ax, col_r_x + 0.04, y_lim_lbl, _COL_W,
                            "Limitations", color, fontsize=10)
        bullet_list(ax, col_r_x, y_lim_lbl - _LABEL_GAP,
                    fw["limits"], dy=_BULLET_DY, fontsize=9.0,
                    color=COLORS["light"], indent=0.28)

    return fig


# ── Diagram metadata ──────────────────────────────────────────────────────────

DIAGRAM_INFO = {
    "filename":    "agile-frameworks-comparison.png",
    "description": "Framework Comparison Chart",
    "chapter":     4,
}
