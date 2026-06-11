"""
Metrics Dashboard for Chapter 7

Portrait A4 layout: four KPI panels (Service Reliability, Operational Efficiency,
Team Performance, Business Value) stacked vertically as full-width cards with
health-status colour coding.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _design_system import (
    COLORS, FONTS, setup_figure, set_lims, draw_card,
)
import matplotlib.patches as mpatches


# ── Layout constants (A4 portrait) ────────────────────────────────────────────

_FIG_W, _FIG_H = 8.5, 11.0
_XLIM = (0.0, 8.5)
_YLIM = (0.0, 11.0)

_CARD_X   = 0.35
_CARD_W   = 7.80
_CARD_TOP = 10.00
_CARD_H   = 2.14
_CARD_GAP = 0.18
_HEADER_H = 0.46
_RADIUS   = 0.14


def _card_top(i):
    return _CARD_TOP - i * (_CARD_H + _CARD_GAP)


# ── Metric data ───────────────────────────────────────────────────────────────

_PANELS = [
    {
        "title":   "Service Reliability",
        "color":   COLORS["coral"],
        "metrics": [
            ("Uptime (SLA target 99.9 %)",        "99.97 %",  "healthy"),
            ("Mean Time to Recover (MTTR)",        "23 min",   "healthy"),
            ("Mean Time Between Failures (MTBF)",  "850 hrs",  "healthy"),
            ("SLO Compliance",                     "98.5 %",   "warning"),
        ],
    },
    {
        "title":   "Operational Efficiency",
        "color":   COLORS["orange"],
        "metrics": [
            ("Automation Coverage",                "75 %",     "healthy"),
            ("Avg Incident Response Time",         "12 min",   "healthy"),
            ("Change Success Rate",                "94.2 %",   "healthy"),
            ("Toil Reduction (vs baseline)",       "68 %",     "warning"),
        ],
    },
    {
        "title":   "Team Performance",
        "color":   COLORS["purple"],
        "metrics": [
            ("Knowledge Sharing Sessions / mo",   "8.2",      "healthy"),
            ("Skills Development Completion",      "85 %",     "healthy"),
            ("On-Call Load (avg hrs / week)",      "3.2 hrs",  "healthy"),
            ("Team Satisfaction Score",            "8.4 / 10", "healthy"),
        ],
    },
    {
        "title":   "Business Value",
        "color":   COLORS["red"],
        "metrics": [
            ("Customer-Facing Availability",       "99.95 %",  "healthy"),
            ("Infrastructure Cost Reduction",      "23 %",     "healthy"),
            ("Security Incidents (month)",         "0",        "healthy"),
            ("Customer Impact Rate",               "0.02 %",   "healthy"),
        ],
    },
]

_STATUS_COLOR = {
    "healthy":  COLORS["healthy"],
    "warning":  COLORS["warning"],
    "critical": COLORS["critical"],
}


# ── Drawing helper ────────────────────────────────────────────────────────────

def _draw_panel(ax, panel, top):
    """Render a single full-width metric panel on the shared canvas."""
    color  = panel["color"]
    bottom = top - _CARD_H

    # Card body + coloured header (centred title)
    draw_card(ax, _CARD_X, bottom, _CARD_W, _CARD_H, color,
              title=panel["title"], header_h=_HEADER_H, radius=_RADIUS)

    metrics     = panel["metrics"]
    n           = len(metrics)
    interior_top = top - _HEADER_H
    row_h        = (interior_top - bottom - 0.12) / n

    for i, (name, value, status) in enumerate(metrics):
        ry = interior_top - (i + 0.5) * row_h
        sc = _STATUS_COLOR[status]

        # Alternating row tint
        if i % 2 == 0:
            ax.add_patch(mpatches.Rectangle(
                (_CARD_X + 0.12, ry - row_h * 0.46),
                _CARD_W - 0.24, row_h * 0.92,
                facecolor=color, alpha=0.06, edgecolor="none", zorder=2,
            ))

        # Status dot
        ax.add_patch(mpatches.Circle(
            (_CARD_X + 0.42, ry), 0.075,
            facecolor=sc, edgecolor="none", zorder=5,
        ))

        # Metric name
        ax.text(_CARD_X + 0.66, ry, name,
                ha="left", va="center",
                fontsize=9.5, color=COLORS["mid"], zorder=5)

        # Value pill (right aligned)
        ax.text(_CARD_X + _CARD_W - 0.30, ry, value,
                ha="right", va="center",
                fontsize=10, fontweight="bold", color=sc, zorder=5,
                bbox=dict(
                    boxstyle="round,pad=0.30",
                    facecolor=sc, alpha=0.16,
                    edgecolor=sc, linewidth=0.8,
                ))

        # Row divider
        if i < n - 1:
            sep_y = ry - row_h * 0.5
            ax.plot([_CARD_X + 0.30, _CARD_X + _CARD_W - 0.30],
                    [sep_y, sep_y],
                    color=COLORS["divider"], lw=0.7, zorder=3)


# ── Diagram builder ───────────────────────────────────────────────────────────

def create_diagram():
    """Create the metrics dashboard for Chapter 7."""
    fig, ax = setup_figure(
        figsize=(_FIG_W, _FIG_H),
        title="SysOps Framework: Metrics Dashboard",
        title_y=0.975,
    )
    set_lims(ax, _XLIM, _YLIM)

    for i, panel in enumerate(_PANELS):
        _draw_panel(ax, panel, _card_top(i))

    # ── Health-status legend ─────────────────────────────────────────────────
    statuses = [
        ("Healthy — Target Met",       _STATUS_COLOR["healthy"]),
        ("Warning — Near Threshold",   _STATUS_COLOR["warning"]),
        ("Critical — Action Required", _STATUS_COLOR["critical"]),
    ]
    ax.text(_XLIM[1] / 2, 0.62, "Health Status Key",
            ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=COLORS["dark"])

    span_x0 = 0.95
    step    = 2.30
    for i, (label, sc) in enumerate(statuses):
        lx = span_x0 + i * step
        ax.add_patch(mpatches.Circle(
            (lx, 0.28), 0.075, facecolor=sc, edgecolor="none", zorder=5,
        ))
        ax.text(lx + 0.16, 0.28, label,
                ha="left", va="center",
                fontsize=8.5, color=COLORS["mid"], zorder=5)

    return fig


# ── Diagram metadata ──────────────────────────────────────────────────────────

DIAGRAM_INFO = {
    "filename":    "sysops-dashboard.png",
    "description": "Metrics Dashboard",
    "chapter":     7,
}
