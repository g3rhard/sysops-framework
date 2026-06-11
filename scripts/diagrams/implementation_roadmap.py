"""
Implementation Roadmap for Chapter 5

Portrait A4 layout: a vertical timeline of the 6-month SysOps Framework roll-out.
Each phase is a card linked to a numbered node on the timeline spine, showing its
month span (a mini ruler preserves the overlap view) and key deliverables.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _design_system import (
    COLORS, FONTS, setup_figure, set_lims,
    draw_card, _rounded_rect,
)
import matplotlib.patches as mpatches


# ── Layout constants (A4 portrait) ────────────────────────────────────────────

_FIG_W, _FIG_H = 8.5, 11.0
_XLIM = (0.0, 8.5)
_YLIM = (0.0, 11.0)

_SPINE_X   = 1.00      # x of the vertical timeline spine
_NODE_R    = 0.30      # phase node radius

_CARD_X    = 1.55
_CARD_W    = 6.65
_CARD_TOP  = 10.00     # top edge of the first phase card
_CARD_H    = 1.84
_CARD_GAP  = 0.15
_HEADER_H  = 0.44
_RADIUS    = 0.14

# Mini month ruler inside each card
_MONTH_MIN = 1.0
_MONTH_MAX = 7.0


def _card_top(i):
    return _CARD_TOP - i * (_CARD_H + _CARD_GAP)


# ── Phase data ────────────────────────────────────────────────────────────────

_PHASES = [
    {
        "name":   "Phase 1: Foundation",
        "color":  COLORS["phase1"],
        "start":  1.0, "end": 3.0,
        "tasks":  ["Current-state assessment", "Team training & onboarding",
                   "Basic monitoring setup"],
    },
    {
        "name":   "Phase 2: Daily Operations",
        "color":  COLORS["phase2"],
        "start":  2.0, "end": 3.5,
        "tasks":  ["Daily cycle implementation", "Incident response process",
                   "On-call rotation design"],
    },
    {
        "name":   "Phase 3: Improvement Cadence",
        "color":  COLORS["phase3"],
        "start":  3.0, "end": 4.5,
        "tasks":  ["Weekly cycle activation", "Process documentation",
                   "Advanced monitoring & alerts"],
    },
    {
        "name":   "Phase 4: Strategy Layer",
        "color":  COLORS["phase4"],
        "start":  4.0, "end": 5.5,
        "tasks":  ["Monthly cycle activation", "Capacity planning model",
                   "Performance optimisation"],
    },
    {
        "name":   "Phase 5: Optimise & Sustain",
        "color":  COLORS["phase5"],
        "start":  5.0, "end": 6.5,
        "tasks":  ["Advanced automation rollout", "Continuous improvement loop",
                   "Maturity self-assessment"],
    },
]


# ── Diagram builder ───────────────────────────────────────────────────────────

def create_diagram():
    """Create the implementation roadmap for Chapter 5."""
    fig, ax = setup_figure(
        figsize=(_FIG_W, _FIG_H),
        title="SysOps Framework: 6-Month Implementation Roadmap",
        title_y=0.975,
    )
    set_lims(ax, _XLIM, _YLIM)

    n = len(_PHASES)

    def _month_x(card_x, card_w, month):
        x0 = card_x + 0.35
        x1 = card_x + card_w - 0.35
        return x0 + (month - _MONTH_MIN) / (_MONTH_MAX - _MONTH_MIN) * (x1 - x0)

    # ── Timeline spine ────────────────────────────────────────────────────────
    y_first = _card_top(0) - _CARD_H / 2
    y_last  = _card_top(n - 1) - _CARD_H / 2
    ax.plot([_SPINE_X, _SPINE_X], [y_last, y_first],
            color=COLORS["border"], lw=3.0, zorder=1,
            solid_capstyle="round")

    for i, phase in enumerate(_PHASES):
        color  = phase["color"]
        top    = _card_top(i)
        bottom = top - _CARD_H
        mid_y  = top - _CARD_H / 2

        # ── Timeline node ─────────────────────────────────────────────────────
        ax.add_patch(mpatches.Circle(
            (_SPINE_X, mid_y), _NODE_R,
            facecolor=color, edgecolor=COLORS["white"], lw=2.0, zorder=4,
        ))
        ax.text(_SPINE_X, mid_y, str(i + 1),
                ha="center", va="center",
                fontsize=12, fontweight="bold", color=COLORS["white"], zorder=5)
        # connector from node to card
        ax.plot([_SPINE_X + _NODE_R, _CARD_X], [mid_y, mid_y],
                color=color, lw=1.6, zorder=2)

        # ── Phase card ────────────────────────────────────────────────────────
        draw_card(ax, _CARD_X, bottom, _CARD_W, _CARD_H, color,
                  title=None, radius=_RADIUS)

        # Custom header: phase name (left) + month range (right)
        hb_y = top - _HEADER_H
        _rounded_rect(ax, _CARD_X, hb_y, _CARD_W, _HEADER_H, color,
                      edge_color="none", lw=0, radius=_RADIUS, zorder=3)
        ax.add_patch(mpatches.Rectangle(
            (_CARD_X, hb_y), _CARD_W, _HEADER_H / 2,
            facecolor=color, edgecolor="none", zorder=3,
        ))
        ax.text(_CARD_X + 0.28, hb_y + _HEADER_H / 2, phase["name"],
                ha="left", va="center",
                fontsize=11.5, fontweight="bold", color=COLORS["white"], zorder=4)
        ax.text(_CARD_X + _CARD_W - 0.28, hb_y + _HEADER_H / 2,
                f"Months {phase['start']:g}\u2013{phase['end']:g}",
                ha="right", va="center",
                fontsize=9, fontweight="bold", color=COLORS["white"],
                alpha=0.95, zorder=4)

        # ── Task bullets ──────────────────────────────────────────────────────
        ty = hb_y - 0.30
        for task in phase["tasks"]:
            ax.text(_CARD_X + 0.30, ty, f"\u2022  {task}",
                    ha="left", va="center",
                    fontsize=9, color=COLORS["mid"], zorder=5)
            ty -= 0.28

        # ── Mini month ruler (preserves the overlap view) ─────────────────────
        ruler_y = hb_y - 1.22
        rx0 = _month_x(_CARD_X, _CARD_W, _MONTH_MIN)
        rx1 = _month_x(_CARD_X, _CARD_W, _MONTH_MAX)
        ax.add_patch(mpatches.FancyBboxPatch(
            (rx0, ruler_y - 0.07), rx1 - rx0, 0.14,
            boxstyle="round,pad=0,rounding_size=0.07",
            facecolor=COLORS["divider"], edgecolor="none", zorder=3,
        ))
        ax.add_patch(mpatches.FancyBboxPatch(
            (_month_x(_CARD_X, _CARD_W, phase["start"]), ruler_y - 0.07),
            _month_x(_CARD_X, _CARD_W, phase["end"])
            - _month_x(_CARD_X, _CARD_W, phase["start"]), 0.14,
            boxstyle="round,pad=0,rounding_size=0.07",
            facecolor=color, edgecolor="none", zorder=4,
        ))
        # month tick labels under the last card only
        if i == n - 1:
            for mlab in range(1, 7):
                ax.text(_month_x(_CARD_X, _CARD_W, mlab), ruler_y - 0.26,
                        f"M{mlab}", ha="center", va="top",
                        fontsize=7, color=COLORS["muted"], zorder=4)

    return fig


# ── Diagram metadata ──────────────────────────────────────────────────────────

DIAGRAM_INFO = {
    "filename":    "sysops-roadmap.png",
    "description": "Implementation Roadmap",
    "chapter":     5,
}
