"""
Implementation Roadmap for Chapter 5

Gantt-style diagram showing the 6-month SysOps Framework roll-out with
overlapping phases and per-phase task breakdowns.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _design_system import (
    COLORS, FONTS, setup_figure, set_lims,
    draw_card, _rounded_rect, label_badge, draw_h_divider,
)
import matplotlib.patches as mpatches


# ── Layout constants ──────────────────────────────────────────────────────────

_FIG_W, _FIG_H = 18.0, 11.0

_XLIM = (0.0, 18.0)
_YLIM = (2.0, 11.2)   # bottom trimmed to remove dead whitespace

# Timeline x-range: months 1–6 map linearly onto [_TL_X0, _TL_X1]
_TL_X0    = 2.8    # x where month 1 starts
_TL_X1    = 14.2   # x where month 6 ends
_TL_UNITS = _TL_X1 - _TL_X0
_MONTH_W  = _TL_UNITS / 6

_BAR_H    = 0.60   # Gantt bar height
_LABEL_X  = 0.15   # left label column right edge
_TASK_X   = 14.5   # right task column left edge

# Phase row y-centres (top to bottom)
_ROW_Y = [9.2, 7.7, 6.2, 4.7, 3.2]

_HEADER_Y = 10.30
_HEADER_H = 0.55

# Bottom of the grid area (matches YLIM bottom)
_GRID_BOTTOM = 2.1


def _mx(month_float):
    """Convert a month number (1-based float) to x data coordinate."""
    return _TL_X0 + (month_float - 1) * _MONTH_W


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
        title_y=0.97,
    )
    set_lims(ax, _XLIM, _YLIM)

    # ── Column header strip ───────────────────────────────────────────────────
    ax.text((_LABEL_X + _TL_X0) / 2, _HEADER_Y + _HEADER_H / 2,
            "Phase", ha="center", va="center",
            fontsize=FONTS["axis"], fontweight="bold", color=COLORS["light"])

    for m in range(1, 7):
        col_x0 = _mx(m)
        col_x1 = _mx(m + 1)
        if m % 2 == 0:
            ax.add_patch(mpatches.Rectangle(
                (col_x0, _GRID_BOTTOM), col_x1 - col_x0,
                _HEADER_Y + _HEADER_H - _GRID_BOTTOM,
                facecolor=COLORS["border"], alpha=0.22, edgecolor="none", zorder=1,
            ))
        ax.text((col_x0 + col_x1) / 2, _HEADER_Y + _HEADER_H / 2,
                f"Month {m}", ha="center", va="center",
                fontsize=FONTS["axis"], fontweight="bold", color=COLORS["dark"])

    ax.text((_TASK_X + _XLIM[1]) / 2, _HEADER_Y + _HEADER_H / 2,
            "Key Deliverables", ha="center", va="center",
            fontsize=FONTS["axis"], fontweight="bold", color=COLORS["light"])

    draw_h_divider(ax, 0, _HEADER_Y, _XLIM[1], color=COLORS["border"], lw=1.0)
    draw_h_divider(ax, 0, _HEADER_Y + _HEADER_H, _XLIM[1],
                   color=COLORS["border"], lw=0.8)

    for m in range(1, 8):
        ax.plot([_mx(m), _mx(m)], [_GRID_BOTTOM, _HEADER_Y],
                color=COLORS["border"], lw=0.7, zorder=1)

    # ── Phase rows ────────────────────────────────────────────────────────────
    for i, phase in enumerate(_PHASES):
        row_y  = _ROW_Y[i]
        color  = phase["color"]
        bar_x0 = _mx(phase["start"])
        bar_x1 = min(_mx(phase["end"]), _TL_X1)
        bar_w  = bar_x1 - bar_x0

        ax.text(_LABEL_X + 0.05, row_y,
                phase["name"], ha="left", va="center",
                fontsize=FONTS["body"], fontweight="bold", color=color)

        # Bar shadow
        ax.add_patch(mpatches.FancyBboxPatch(
            (bar_x0 + 0.05, row_y - _BAR_H / 2 - 0.04), bar_w, _BAR_H,
            boxstyle="round,pad=0,rounding_size=0.10",
            facecolor="#00000018", edgecolor="none", zorder=2,
        ))
        # Bar fill
        ax.add_patch(mpatches.FancyBboxPatch(
            (bar_x0, row_y - _BAR_H / 2), bar_w, _BAR_H,
            boxstyle="round,pad=0,rounding_size=0.10",
            facecolor=color, edgecolor=color,
            alpha=0.90, linewidth=1.2, zorder=3,
        ))
        ax.text(bar_x0 + 0.22, row_y,
                str(i + 1), ha="center", va="center",
                fontsize=FONTS["body"], fontweight="bold",
                color=COLORS["white"], zorder=4)

        # Task list (right column)
        n   = len(phase["tasks"])
        top = row_y + (n - 1) * 0.30 / 2
        for j, task in enumerate(phase["tasks"]):
            ax.text(_TASK_X + 0.15, top - j * 0.30,
                    f"\u2022  {task}",
                    ha="left", va="center",
                    fontsize=FONTS["small"], color=COLORS["mid"])

        # Row separator
        if i < len(_PHASES) - 1:
            sep_y = (row_y + _ROW_Y[i + 1]) / 2
            draw_h_divider(ax, 0.10, sep_y, _XLIM[1] - 0.20,
                           color=COLORS["divider"], lw=0.6)

    # ── Overlap annotations ───────────────────────────────────────────────────
    for note, nx, ny in [
        ("Parallel kick-off",  _mx(2.0), _ROW_Y[0] - _BAR_H / 2 - 0.05),
        ("Continuous overlap", _mx(4.5), _ROW_Y[2] - _BAR_H / 2 - 0.05),
    ]:
        ax.text(nx, ny, note, ha="center", va="top",
                fontsize=7.5, color=COLORS["muted"], style="italic")

    # ── Bottom legend ─────────────────────────────────────────────────────────
    handles = [
        mpatches.Patch(facecolor=p["color"], label=p["name"])
        for p in _PHASES
    ]
    ax.legend(
        handles=handles,
        loc="lower center",
        ncol=5,
        bbox_to_anchor=(0.5, -0.01),
        fontsize=FONTS["small"],
        frameon=False,
        handlelength=1.2,
        handleheight=0.8,
    )

    return fig


# ── Diagram metadata ──────────────────────────────────────────────────────────

DIAGRAM_INFO = {
    "filename":    "sysops-roadmap.png",
    "description": "Implementation Roadmap",
    "chapter":     5,
}
