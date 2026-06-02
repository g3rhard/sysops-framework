"""
SysOps Framework Structure Diagram for Chapter 3

Shows the three interlocking operational cycles (Daily / Weekly / Monthly)
and the supporting practices that underpin all cycles.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _design_system import (
    COLORS, FONTS, setup_figure, set_lims,
    draw_card, draw_section_label, draw_h_divider,
    bullet_list, label_badge, arrow_h, arrow_curved, arrow_dashed,
)


# ── Layout constants ──────────────────────────────────────────────────────────

_FIG_W, _FIG_H = 16.0, 12.0
_XLIM = (0.0, 16.0)
_YLIM = (0.0, 12.0)

# Three cycle cards
_CARD_W       = 4.50
_CARD_H       = 5.20
_CARD_BOTTOM  = 5.90   # y of card bottom edge
_CARD_X       = [0.40, 5.75, 11.10]
_HEADER_H     = 0.64
_RADIUS       = 0.16

# Supporting-practices bar
_SUP_X   = 0.40
_SUP_Y   = 0.60
_SUP_W   = 15.20
_SUP_H   = 4.60


# ── Cycle data ────────────────────────────────────────────────────────────────

_CYCLES = [
    {
        "name":    "Daily Operations Cycle",
        "cadence": "24 hours",
        "color":   COLORS["daily"],
        "items": [
            "Incident response & triage",
            "Urgent maintenance tasks",
            "Service health monitoring",
            "Team handoffs & briefings",
        ],
    },
    {
        "name":    "Weekly Improvement Cycle",
        "cadence": "7 days",
        "color":   COLORS["weekly"],
        "items": [
            "Process improvement tasks",
            "Automation & tooling work",
            "Knowledge sharing sessions",
            "Root cause analysis reviews",
        ],
    },
    {
        "name":    "Monthly Strategy Cycle",
        "cadence": "30 days",
        "color":   COLORS["monthly"],
        "items": [
            "Capacity & resource planning",
            "Architecture review board",
            "Performance trend analysis",
            "Goal-setting & OKR reviews",
        ],
    },
]

# Pre-wrapped text so no auto-splitting causes crowding
_SUPPORT_ITEMS = [
    {
        "name":  "Documentation\n& Runbooks",
        "line1": "Living docs & runbooks",
        "line2": "for all key procedures",
    },
    {
        "name":  "Metrics &\nMonitoring",
        "line1": "SLI / SLO data collection",
        "line2": "feeding cycle dashboards",
    },
    {
        "name":  "Training &\nDevelopment",
        "line1": "Skills matrix & certifications",
        "line2": "cross-training plans",
    },
    {
        "name":  "Feedback\nLoops",
        "line1": "Retros & post-mortems",
        "line2": "fed back into all cycles",
    },
]


# ── Diagram builder ───────────────────────────────────────────────────────────

def create_diagram():
    """Create the SysOps framework structure diagram for Chapter 3."""
    fig, ax = setup_figure(
        figsize=(_FIG_W, _FIG_H),
        title="SysOps Framework: Multi-Cycle Operating Model",
        title_y=0.97,
    )
    set_lims(ax, _XLIM, _YLIM)

    # ── Cycle cards ──────────────────────────────────────────────────────────
    for idx, cycle in enumerate(_CYCLES):
        cx    = _CARD_X[idx]
        color = cycle["color"]
        mid_x = cx + _CARD_W / 2
        inner_top = _CARD_BOTTOM + _CARD_H - _HEADER_H

        draw_card(ax, cx, _CARD_BOTTOM, _CARD_W, _CARD_H, color,
                  title=cycle["name"], header_h=_HEADER_H, radius=_RADIUS)

        # Cadence badge
        badge_y = inner_top - 0.50
        label_badge(ax, mid_x, badge_y, cycle["cadence"], color=color)

        # Activity bullets — distribute evenly in remaining interior space
        # interior below badge: badge_y - 0.30 down to _CARD_BOTTOM + 0.30
        avail_top = badge_y - 0.48
        avail_bot = _CARD_BOTTOM + 0.32
        n_items   = len(cycle["items"])
        item_dy   = (avail_top - avail_bot) / (n_items - 1) if n_items > 1 else 0

        bullet_list(ax, cx, avail_top,
                    cycle["items"], dy=item_dy,
                    fontsize=FONTS["body"], color=COLORS["mid"], indent=0.30)

    # ── Flow arrows between cycle cards ──────────────────────────────────────
    arrow_y = _CARD_BOTTOM + _CARD_H * 0.45

    arrow_h(ax,
            _CARD_X[0] + _CARD_W + 0.10,
            _CARD_X[1] - 0.10,
            arrow_y, color=COLORS["daily"], lw=2.4)
    ax.text((_CARD_X[0] + _CARD_W + _CARD_X[1]) / 2,
            arrow_y + 0.28, "escalate", ha="center",
            fontsize=FONTS["small"], color=COLORS["daily"], style="italic")

    arrow_h(ax,
            _CARD_X[1] + _CARD_W + 0.10,
            _CARD_X[2] - 0.10,
            arrow_y, color=COLORS["weekly"], lw=2.4)
    ax.text((_CARD_X[1] + _CARD_W + _CARD_X[2]) / 2,
            arrow_y + 0.28, "aggregate", ha="center",
            fontsize=FONTS["small"], color=COLORS["weekly"], style="italic")

    # Monthly → Daily feedback loop above cards
    top_y = _CARD_BOTTOM + _CARD_H + 0.18
    arrow_curved(ax,
                 _CARD_X[2] + _CARD_W * 0.5, top_y,
                 _CARD_X[0] + _CARD_W * 0.5, top_y,
                 color=COLORS["monthly"], rad=-0.45, lw=2.2)
    ax.text((_CARD_X[0] + _CARD_X[2] + _CARD_W) / 2,
            top_y + 0.64,
            "strategic priorities & feedback",
            ha="center", fontsize=FONTS["small"],
            color=COLORS["monthly"], style="italic")

    # ── Supporting practices bar ──────────────────────────────────────────────
    draw_card(ax, _SUP_X, _SUP_Y, _SUP_W, _SUP_H,
              accent=COLORS["support"],
              title="Supporting Practices  —  Underpin All Cycles",
              header_h=0.54, radius=_RADIUS)

    col_w = _SUP_W / 4
    for i, sp in enumerate(_SUPPORT_ITEMS):
        col_cx = _SUP_X + i * col_w + col_w / 2

        # Vertical column divider
        if i > 0:
            ax.plot([_SUP_X + i * col_w, _SUP_X + i * col_w],
                    [_SUP_Y + 0.60, _SUP_Y + _SUP_H - 0.60],
                    color=COLORS["border"], lw=0.9)

        # Practice name (multi-line, bold)
        ax.text(col_cx, _SUP_Y + _SUP_H - 1.10, sp["name"],
                ha="center", va="center",
                fontsize=FONTS["section"], fontweight="bold",
                color=COLORS["support"])

        # Two description lines
        ax.text(col_cx, _SUP_Y + _SUP_H - 1.78, sp["line1"],
                ha="center", va="center",
                fontsize=FONTS["small"], color=COLORS["mid"])
        ax.text(col_cx, _SUP_Y + _SUP_H - 2.14, sp["line2"],
                ha="center", va="center",
                fontsize=FONTS["small"], color=COLORS["mid"])

    # ── 3 dashed arrows from support bar top to cycle cards ──────────────────
    for idx, cx in enumerate(_CARD_X):
        src_x = _SUP_X + _SUP_W * (2 * idx + 1) / (2 * len(_CARD_X))
        tgt_x = cx + _CARD_W / 2
        arrow_dashed(ax,
                     src_x, _SUP_Y + _SUP_H + 0.08,
                     tgt_x, _CARD_BOTTOM - 0.08,
                     color=COLORS["support"], lw=1.6)

    return fig


# ── Diagram metadata ──────────────────────────────────────────────────────────

DIAGRAM_INFO = {
    "filename":    "sysops-framework-diagram.png",
    "description": "Framework Structure Diagram",
    "chapter":     3,
}
