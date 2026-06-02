"""
Metrics Dashboard for Chapter 7

Four-panel KPI dashboard showing Service Reliability, Operational Efficiency,
Team Performance, and Business Value metrics with health-status colour coding.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _design_system import (
    COLORS, FONTS, apply_global_style,
    _rounded_rect, shadow,
)
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec


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

def _draw_panel(ax, panel):
    """Render a single metric panel on the provided axes."""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    color    = panel["color"]
    header_h = 0.14

    # Card drop-shadow + white body
    shadow(ax, 0.02, 0.02, 0.96, 0.96, radius=0.04)
    _rounded_rect(ax, 0.02, 0.02, 0.96, 0.96,
                  color=COLORS["surface"], edge_color=color,
                  lw=1.8, radius=0.04, zorder=2)

    # Coloured header band
    _rounded_rect(ax, 0.02, 1.0 - header_h - 0.02, 0.96, header_h,
                  color=color, edge_color="none", lw=0, radius=0.04, zorder=3)
    ax.add_patch(plt.Rectangle(
        (0.02, 1.0 - header_h - 0.02), 0.96, header_h / 2,
        facecolor=color, edgecolor="none", zorder=3,
    ))
    ax.text(0.50, 1.0 - header_h / 2 - 0.02,
            panel["title"], ha="center", va="center",
            fontsize=FONTS["panel"], fontweight="bold",
            color=COLORS["white"], zorder=4)

    # Metric rows — distribute evenly in the interior
    n       = len(panel["metrics"])
    # interior: from y=0.04 to y=1.0-header_h-0.04
    int_top = 1.0 - header_h - 0.04
    int_bot = 0.06
    # place rows at equal intervals
    for i, (name, value, status) in enumerate(panel["metrics"]):
        ry = int_top - (i + 0.5) * (int_top - int_bot) / n
        sc = _STATUS_COLOR[status]

        # Alternating row background tint
        rh = (int_top - int_bot) / n
        if i % 2 == 0:
            ax.add_patch(plt.Rectangle(
                (0.04, ry - rh * 0.46), 0.92, rh * 0.92,
                facecolor=color, alpha=0.06,
                edgecolor="none", zorder=2,
            ))

        # Status dot
        ax.add_patch(plt.Circle(
            (0.065, ry), 0.022,
            facecolor=sc, edgecolor="none", zorder=5,
        ))

        # Metric name — start well clear of the dot
        ax.text(0.115, ry, name,
                ha="left", va="center",
                fontsize=FONTS["body"], color=COLORS["mid"], zorder=5)

        # Value pill
        ax.text(0.92, ry, value,
                ha="right", va="center",
                fontsize=FONTS["body"], fontweight="bold",
                color=sc, zorder=5,
                bbox=dict(
                    boxstyle="round,pad=0.28",
                    facecolor=sc, alpha=0.16,
                    edgecolor=sc, linewidth=0.8,
                ))

        # Row divider
        if i < n - 1:
            sep_y = ry - rh * 0.46
            ax.plot([0.06, 0.94], [sep_y, sep_y],
                    color=COLORS["divider"], lw=0.7, zorder=3)


# ── Diagram builder ───────────────────────────────────────────────────────────

def create_diagram():
    """Create the metrics dashboard for Chapter 7."""
    apply_global_style()

    fig = plt.figure(figsize=(16, 12), facecolor=COLORS["bg"])

    fig.text(0.50, 0.97,
             "SysOps Framework: Metrics Dashboard",
             ha="center", va="top",
             fontsize=FONTS["title"], fontweight="bold", color=COLORS["dark"])

    # 2 × 2 panel grid + 1 narrow legend row
    gs = gridspec.GridSpec(
        3, 2,
        height_ratios=[1, 1, 0.16],
        hspace=0.30, wspace=0.20,
        top=0.92, bottom=0.06,
        left=0.03, right=0.97,
    )

    panel_axes = [
        fig.add_subplot(gs[0, 0]),
        fig.add_subplot(gs[0, 1]),
        fig.add_subplot(gs[1, 0]),
        fig.add_subplot(gs[1, 1]),
    ]

    for pax, panel in zip(panel_axes, _PANELS):
        _draw_panel(pax, panel)

    # ── Legend row ────────────────────────────────────────────────────────────
    lax = fig.add_subplot(gs[2, :])
    lax.set_xlim(0, 1)
    lax.set_ylim(0, 1)
    lax.axis("off")

    lax.text(0.50, 0.80, "Health Status Key",
             ha="center", va="center",
             fontsize=FONTS["section"], fontweight="bold",
             color=COLORS["dark"])

    statuses = [
        ("Healthy — Target Met",       _STATUS_COLOR["healthy"]),
        ("Warning — Near Threshold",   _STATUS_COLOR["warning"]),
        ("Critical — Action Required", _STATUS_COLOR["critical"]),
    ]
    for i, (label, sc) in enumerate(statuses):
        lx = 0.22 + i * 0.28
        lax.add_patch(plt.Circle(
            (lx - 0.04, 0.35), 0.04,
            facecolor=sc, edgecolor="none",
        ))
        lax.text(lx + 0.01, 0.35, label,
                 ha="left", va="center",
                 fontsize=FONTS["body"], color=COLORS["mid"])

    return fig


# ── Diagram metadata ──────────────────────────────────────────────────────────

DIAGRAM_INFO = {
    "filename":    "sysops-dashboard.png",
    "description": "Metrics Dashboard",
    "chapter":     7,
}
