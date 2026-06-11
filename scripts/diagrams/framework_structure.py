"""
SysOps Framework Structure Diagram for Chapter 3

Portrait A4 layout: the three operational cycles (Daily / Weekly / Monthly) are
stacked as full-width cards, linked by escalate / aggregate flow arrows and a
monthly feedback loop.  A supporting-practices panel underpins all cycles.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _design_system import (
    COLORS, FONTS, setup_figure, set_lims,
    draw_card, _rounded_rect, label_badge, arrow_curved, arrow_dashed,
)
import matplotlib.patches as mpatches


# ── Layout constants (A4 portrait) ────────────────────────────────────────────

_FIG_W, _FIG_H = 8.5, 11.0
_XLIM = (0.0, 8.5)
_YLIM = (0.0, 11.0)

# Three cycle cards, stacked
_CARD_X      = 0.35
_CARD_W      = 7.10
_CARD_TOP    = 10.00     # top edge of first card
_CARD_H      = 1.66
_CARD_GAP    = 0.56      # vertical gap between cards (room for flow arrows)
_HEADER_H    = 0.46
_RADIUS      = 0.15

_FB_X        = 7.95      # x of the feedback loop / right channel

# Supporting-practices panel
_SUP_X   = 0.35
_SUP_W   = 7.10
_SUP_TOP = 3.40
_SUP_BOT = 0.40
_SUP_HEADER_H = 0.50


def _card_top(i):
    return _CARD_TOP - i * (_CARD_H + _CARD_GAP)


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
        title_y=0.975,
    )
    set_lims(ax, _XLIM, _YLIM)

    card_mid_x = _CARD_X + _CARD_W / 2

    # ── Cycle cards (stacked) ────────────────────────────────────────────────
    for idx, cycle in enumerate(_CYCLES):
        color  = cycle["color"]
        top    = _card_top(idx)
        bottom = top - _CARD_H

        draw_card(ax, _CARD_X, bottom, _CARD_W, _CARD_H, color,
                  title=None, radius=_RADIUS)

        # Custom header: cycle name (left) + cadence (right)
        hb_y = top - _HEADER_H
        _rounded_rect(ax, _CARD_X, hb_y, _CARD_W, _HEADER_H, color,
                      edge_color="none", lw=0, radius=_RADIUS, zorder=3)
        ax.add_patch(mpatches.Rectangle(
            (_CARD_X, hb_y), _CARD_W, _HEADER_H / 2,
            facecolor=color, edgecolor="none", zorder=3,
        ))
        ax.text(_CARD_X + 0.30, hb_y + _HEADER_H / 2, cycle["name"],
                ha="left", va="center",
                fontsize=12.5, fontweight="bold", color=COLORS["white"], zorder=4)
        ax.text(_CARD_X + _CARD_W - 0.30, hb_y + _HEADER_H / 2,
                cycle["cadence"], ha="right", va="center",
                fontsize=9.5, fontweight="bold", color=COLORS["white"],
                alpha=0.95, zorder=4)

        # Four activity bullets in two columns (2 + 2)
        items = cycle["items"]
        col_x = [_CARD_X + 0.30, _CARD_X + _CARD_W / 2 + 0.10]
        row_y = [hb_y - 0.36, hb_y - 0.78]
        for k, item in enumerate(items):
            cx = col_x[k % 2]
            cy = row_y[k // 2]
            ax.text(cx, cy, f"\u2022  {item}",
                    ha="left", va="center",
                    fontsize=9.5, color=COLORS["mid"], zorder=5)

    # ── Flow arrows between stacked cards ────────────────────────────────────
    def _down_arrow(y_from, y_to, color, label):
        ax.annotate(
            "", xy=(card_mid_x, y_to), xytext=(card_mid_x, y_from),
            arrowprops=dict(arrowstyle="-|>", color=color, lw=2.4,
                            mutation_scale=18),
            zorder=6,
        )
        ax.text(card_mid_x + 0.25, (y_from + y_to) / 2, label,
                ha="left", va="center",
                fontsize=FONTS["small"], color=color, style="italic", zorder=6)

    gap1_top = _card_top(0) - _CARD_H
    gap1_bot = _card_top(1)
    _down_arrow(gap1_top - 0.04, gap1_bot + 0.04, COLORS["daily"], "escalate")

    gap2_top = _card_top(1) - _CARD_H
    gap2_bot = _card_top(2)
    _down_arrow(gap2_top - 0.04, gap2_bot + 0.04, COLORS["weekly"], "aggregate")

    # ── Monthly feedback loop (right channel, bottom → top) ──────────────────
    y_bottom_mid = _card_top(2) - _CARD_H / 2
    y_top_mid    = _card_top(0) - _CARD_H / 2
    arrow_curved(ax,
                 _CARD_X + _CARD_W + 0.02, y_bottom_mid,
                 _CARD_X + _CARD_W + 0.02, y_top_mid,
                 color=COLORS["monthly"], rad=-0.32, lw=2.2)
    ax.text(_FB_X + 0.18, (y_bottom_mid + y_top_mid) / 2,
            "strategic priorities & feedback",
            ha="center", va="center", rotation=90,
            fontsize=FONTS["small"], color=COLORS["monthly"], style="italic")

    # ── Supporting practices panel ───────────────────────────────────────────
    draw_card(ax, _SUP_X, _SUP_BOT, _SUP_W, _SUP_TOP - _SUP_BOT,
              accent=COLORS["support"], title=None, radius=_RADIUS)

    hb_y = _SUP_TOP - _SUP_HEADER_H
    _rounded_rect(ax, _SUP_X, hb_y, _SUP_W, _SUP_HEADER_H, COLORS["support"],
                  edge_color="none", lw=0, radius=_RADIUS, zorder=3)
    ax.add_patch(mpatches.Rectangle(
        (_SUP_X, hb_y), _SUP_W, _SUP_HEADER_H / 2,
        facecolor=COLORS["support"], edgecolor="none", zorder=3,
    ))
    ax.text(_SUP_X + _SUP_W / 2, hb_y + _SUP_HEADER_H / 2,
            "Supporting Practices  —  Underpin All Cycles",
            ha="center", va="center",
            fontsize=12, fontweight="bold", color=COLORS["white"], zorder=4)

    # 2 × 2 grid of supporting practices
    cell_w = _SUP_W / 2
    content_top = hb_y
    content_bot = _SUP_BOT
    row_cy = [content_top - 0.62, content_top - 1.92]
    for i, sp in enumerate(_SUPPORT_ITEMS):
        c = i % 2
        r = i // 2
        cell_cx = _SUP_X + (c + 0.5) * cell_w
        cy = row_cy[r]

        # column divider
        if c == 1:
            ax.plot([_SUP_X + cell_w, _SUP_X + cell_w],
                    [content_bot + 0.25, content_top - 0.20],
                    color=COLORS["border"], lw=0.9, zorder=3)

        ax.text(cell_cx, cy + 0.30, sp["name"].replace("\n", " "),
                ha="center", va="center",
                fontsize=11, fontweight="bold",
                color=COLORS["support"], zorder=5)
        ax.text(cell_cx, cy - 0.18, sp["line1"],
                ha="center", va="center",
                fontsize=8.5, color=COLORS["mid"], zorder=5)
        ax.text(cell_cx, cy - 0.48, sp["line2"],
                ha="center", va="center",
                fontsize=8.5, color=COLORS["mid"], zorder=5)

    # horizontal divider between the two rows
    ax.plot([_SUP_X + 0.30, _SUP_X + _SUP_W - 0.30],
            [(row_cy[0] + row_cy[1]) / 2 - 0.18] * 2,
            color=COLORS["divider"], lw=0.7, zorder=3)

    # ── Dashed connectors: support panel → cycle stack ───────────────────────
    for fx in (_SUP_X + _SUP_W * 0.25, _SUP_X + _SUP_W * 0.5,
               _SUP_X + _SUP_W * 0.75):
        arrow_dashed(ax, fx, _SUP_TOP + 0.04,
                     fx, _card_top(2) - _CARD_H - 0.04,
                     color=COLORS["support"], lw=1.4)

    return fig


# ── Diagram metadata ──────────────────────────────────────────────────────────

DIAGRAM_INFO = {
    "filename":    "sysops-framework-diagram.png",
    "description": "Framework Structure Diagram",
    "chapter":     3,
}
