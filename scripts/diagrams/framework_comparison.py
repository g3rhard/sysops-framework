"""
Agile Frameworks Comparison Chart for Chapter 4

Three-column card layout.  Each card has three sections:
  1. Key Characteristics  (5 bullets)
  2. Best Used For        (3 bullets)
  3. Limitations          (2 bullets)

Dividers are placed dynamically so content fills the card top-to-bottom.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _design_system import (
    COLORS, FONTS, setup_figure, set_lims,
    draw_card, draw_section_label, draw_h_divider,
    bullet_list, label_badge,
)
import matplotlib.patches as mpatches

# ── Layout constants ──────────────────────────────────────────────────────────

_FIG_W, _FIG_H  = 18.0, 11.5
_XLIM           = (0.0, 18.0)
_YLIM           = (0.0, 12.0)

_CARD_W         = 5.20
_CARD_H         = 9.40
_CARD_BOTTOM    = 0.90
_HEADER_H       = 0.58
_RADIUS         = 0.16

_CARD_X         = [0.50, 6.40, 12.30]   # left x of each card

_CHAR_DY        = 0.44   # bullet spacing — Key Characteristics
_BF_DY          = 0.44   # bullet spacing — Best For
_SECTION_GAP    = 0.30   # gap from last bullet to divider
_AFTER_DIV      = 0.30   # gap from divider to next section label
_BULLET_TOP_GAP = 0.38   # gap from bottom of label band to first bullet

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
        title_y=0.97,
    )
    set_lims(ax, _XLIM, _YLIM)

    for fw, cx in zip(_FRAMEWORKS, _CARD_X):
        color  = fw["color"]
        cx_mid = cx + _CARD_W / 2

        # ── Card shell ────────────────────────────────────────────────────────
        draw_card(ax, cx, _CARD_BOTTOM, _CARD_W, _CARD_H, color,
                  title=fw["name"], header_h=_HEADER_H, radius=_RADIUS)

        # Top of interior (y coordinate just below the header band)
        y_top = _CARD_BOTTOM + _CARD_H - _HEADER_H

        # ── Cadence badge ─────────────────────────────────────────────────────
        y_badge = y_top - 0.38
        label_badge(ax, cx_mid, y_badge, fw["cadence"], color=color, fontsize=8.5)

        # ── Section 1: Key Characteristics ───────────────────────────────────
        y_s1 = y_badge - 0.52
        draw_section_label(ax, cx + 0.12, y_s1, _CARD_W - 0.24,
                           "Key Characteristics", color, fontsize=8.5)

        y_b1_first = y_s1 - _BULLET_TOP_GAP
        bullet_list(ax, cx, y_b1_first, fw["characteristics"],
                    dy=_CHAR_DY, fontsize=9.5,
                    color=COLORS["mid"], indent=0.28)

        n_char    = len(fw["characteristics"])
        y_b1_last = y_b1_first - (n_char - 1) * _CHAR_DY

        # ── Divider 1 ─────────────────────────────────────────────────────────
        y_div1 = y_b1_last - _SECTION_GAP
        draw_h_divider(ax, cx + 0.18, y_div1, _CARD_W - 0.36,
                       color=COLORS["border"])

        # ── Section 2: Best Used For ──────────────────────────────────────────
        y_s2 = y_div1 - _AFTER_DIV
        draw_section_label(ax, cx + 0.12, y_s2, _CARD_W - 0.24,
                           fw["best_for_label"], color, fontsize=8.5)

        y_b2_first = y_s2 - _BULLET_TOP_GAP
        bullet_list(ax, cx, y_b2_first, fw["best_for"],
                    dy=_BF_DY, fontsize=9.5,
                    color=COLORS["mid"], indent=0.28)

        n_bf      = len(fw["best_for"])
        y_b2_last = y_b2_first - (n_bf - 1) * _BF_DY

        # ── Divider 2 ─────────────────────────────────────────────────────────
        y_div2 = y_b2_last - _SECTION_GAP
        draw_h_divider(ax, cx + 0.18, y_div2, _CARD_W - 0.36,
                       color=COLORS["border"])

        # ── Section 3: Limitations ────────────────────────────────────────────
        y_s3 = y_div2 - _AFTER_DIV
        draw_section_label(ax, cx + 0.12, y_s3, _CARD_W - 0.24,
                           "Limitations", color, fontsize=8.5)

        y_b3_first = y_s3 - _BULLET_TOP_GAP
        bullet_list(ax, cx, y_b3_first, fw["limits"],
                    dy=0.40, fontsize=9.0,
                    color=COLORS["light"], indent=0.28)

    # ── Bottom legend strip ───────────────────────────────────────────────────
    legend_y = 0.45
    for fw, cx in zip(_FRAMEWORKS, _CARD_X):
        lx = cx + _CARD_W / 2
        ax.add_patch(mpatches.Rectangle(
            (lx - 0.55, legend_y - 0.18), 1.1, 0.28,
            facecolor=fw["color"], edgecolor="none", alpha=0.18, zorder=1,
        ))
        ax.text(lx, legend_y, fw["name"],
                ha="center", va="center",
                fontsize=8.5, fontweight="bold", color=fw["color"])

    return fig


# ── Diagram metadata ──────────────────────────────────────────────────────────

DIAGRAM_INFO = {
    "filename":    "agile-frameworks-comparison.png",
    "description": "Framework Comparison Chart",
    "chapter":     4,
}
