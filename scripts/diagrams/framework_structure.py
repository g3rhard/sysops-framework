"""Generate the Chapter 3 multi-cycle operating model diagram."""

import os
import sys

import matplotlib.patches as mpatches

sys.path.insert(0, os.path.dirname(__file__))
from _design_system import COLORS, FONTS, _rounded_rect, arrow_curved, setup_figure, set_lims


_CYCLES = [
    {
        "name": "DAILY OPERATIONS",
        "cadence": "24-48 HOURS",
        "owner": "Owner: on-call engineer / team",
        "color": COLORS["daily"],
        "input": "Health signals, incidents, urgent requests",
        "phases": ["Monitor", "Respond", "Document", "Review"],
        "outcome": "Stable services and usable evidence",
        "rule": "Act now when service or safety is at risk.",
    },
    {
        "name": "WEEKLY IMPROVEMENT",
        "cadence": "7 DAYS",
        "owner": "Owner: rotating improvement lead",
        "color": COLORS["weekly"],
        "input": "Recurring pain, toil, and action items",
        "phases": ["Plan", "Execute", "Measure", "Improve"],
        "outcome": "Less toil and fewer repeated failures",
        "rule": "Protect one improvement that can finish this week.",
    },
    {
        "name": "MONTHLY STRATEGY",
        "cadence": "4 WEEKS",
        "owner": "Owner: team lead / manager",
        "color": COLORS["monthly"],
        "input": "Risk, demand, capacity, and business priorities",
        "phases": ["Assess", "Design", "Implement", "Evaluate"],
        "outcome": "Decisions, investment, and clear trade-offs",
        "rule": "Fund work too large or cross-cutting for one week.",
    },
]


def _draw_cycle_card(ax, x, cycle):
    y, w, h = 1.8, 4.35, 5.25
    color = cycle["color"]

    _rounded_rect(
        ax,
        x,
        y,
        w,
        h,
        color=COLORS["surface"],
        edge_color=color,
        lw=1.8,
        radius=0.18,
        zorder=2,
    )
    _rounded_rect(
        ax,
        x,
        y + h - 0.72,
        w,
        0.72,
        color=color,
        edge_color="none",
        lw=0,
        radius=0.18,
        zorder=3,
    )
    ax.add_patch(
        mpatches.Rectangle(
            (x, y + h - 0.36),
            w,
            0.36,
            facecolor=color,
            edgecolor="none",
            zorder=3,
        )
    )
    ax.text(
        x + 0.24,
        y + h - 0.36,
        cycle["name"],
        ha="left",
        va="center",
        fontsize=12,
        fontweight="bold",
        color=COLORS["white"],
        zorder=4,
    )

    _rounded_rect(
        ax,
        x + 0.25,
        y + h - 1.25,
        1.35,
        0.36,
        color=color,
        alpha=0.14,
        edge_color="none",
        lw=0,
        radius=0.16,
        zorder=3,
    )
    ax.text(
        x + 0.925,
        y + h - 1.07,
        cycle["cadence"],
        ha="center",
        va="center",
        fontsize=8.5,
        fontweight="bold",
        color=color,
        zorder=4,
    )
    ax.text(
        x + 1.82,
        y + h - 1.07,
        cycle["owner"],
        ha="left",
        va="center",
        fontsize=8.5,
        color=COLORS["mid"],
        zorder=4,
    )

    ax.text(
        x + 0.25,
        y + h - 1.72,
        "INPUT",
        ha="left",
        va="center",
        fontsize=8,
        fontweight="bold",
        color=color,
    )
    ax.text(
        x + 0.25,
        y + h - 2.02,
        cycle["input"],
        ha="left",
        va="center",
        fontsize=9,
        color=COLORS["dark"],
    )

    phase_y = y + h - 2.85
    phase_gap = 0.10
    phase_w = (w - 0.5 - 3 * phase_gap) / 4
    for index, phase in enumerate(cycle["phases"]):
        phase_x = x + 0.25 + index * (phase_w + phase_gap)
        _rounded_rect(
            ax,
            phase_x,
            phase_y,
            phase_w,
            0.58,
            color=color,
            alpha=0.12,
            edge_color=color,
            lw=0.8,
            radius=0.10,
            zorder=3,
        )
        ax.text(
            phase_x + phase_w / 2,
            phase_y + 0.29,
            phase,
            ha="center",
            va="center",
            fontsize=8.2,
            fontweight="bold",
            color=color,
            zorder=4,
        )
        if index < 3:
            ax.text(
                phase_x + phase_w + phase_gap / 2,
                phase_y + 0.29,
                ">",
                ha="center",
                va="center",
                fontsize=9,
                color=COLORS["muted"],
                zorder=4,
            )

    ax.text(
        x + 0.25,
        y + 1.62,
        "OUTCOME",
        ha="left",
        va="center",
        fontsize=8,
        fontweight="bold",
        color=color,
    )
    ax.text(
        x + 0.25,
        y + 1.32,
        cycle["outcome"],
        ha="left",
        va="center",
        fontsize=9,
        color=COLORS["dark"],
    )

    ax.plot(
        [x + 0.25, x + w - 0.25],
        [y + 0.92, y + 0.92],
        color=COLORS["divider"],
        lw=0.8,
        zorder=3,
    )
    ax.text(
        x + 0.25,
        y + 0.55,
        cycle["rule"],
        ha="left",
        va="center",
        fontsize=8.3,
        color=COLORS["mid"],
        style="italic",
    )


def create_diagram():
    """Create the three-cycle operating model."""
    fig, ax = setup_figure(
        figsize=(15, 8.5),
        title="SysOps Framework: Three Cycles, One Operating Model",
        title_y=0.965,
    )
    set_lims(ax, (0, 15), (0, 8.5))

    ax.text(
        7.5,
        7.78,
        "Run simultaneously. Evidence moves upward; priorities flow back into daily work.",
        ha="center",
        va="center",
        fontsize=FONTS["body"],
        color=COLORS["mid"],
    )

    card_x = [0.55, 5.325, 10.10]
    for x, cycle in zip(card_x, _CYCLES):
        _draw_cycle_card(ax, x, cycle)

    ax.annotate(
        "",
        xy=(5.22, 4.45),
        xytext=(4.92, 4.45),
        arrowprops=dict(
            arrowstyle="-|>",
            color=COLORS["weekly"],
            lw=2.2,
            mutation_scale=17,
        ),
        zorder=6,
    )
    ax.text(
        5.07,
        4.78,
        "patterns",
        ha="center",
        va="center",
        fontsize=8,
        color=COLORS["weekly"],
        rotation=90,
    )

    ax.annotate(
        "",
        xy=(10.00, 4.45),
        xytext=(9.70, 4.45),
        arrowprops=dict(
            arrowstyle="-|>",
            color=COLORS["monthly"],
            lw=2.2,
            mutation_scale=17,
        ),
        zorder=6,
    )
    ax.text(
        9.85,
        4.78,
        "evidence",
        ha="center",
        va="center",
        fontsize=8,
        color=COLORS["monthly"],
        rotation=90,
    )

    arrow_curved(
        ax,
        card_x[2] + 2.18,
        1.72,
        card_x[0] + 2.18,
        1.72,
        color=COLORS["monthly"],
        rad=-0.18,
        lw=2.0,
        mutation_scale=16,
        zorder=5,
    )
    ax.text(
        7.5,
        1.15,
        "monthly priorities and capacity decisions return to daily work",
        ha="center",
        va="center",
        fontsize=8.5,
        color=COLORS["monthly"],
        style="italic",
    )

    foundations = [
        "Service ownership",
        "Shared severity",
        "Living runbooks",
        "Metrics & evidence",
    ]
    strip_y = 0.30
    for index, label in enumerate(foundations):
        x = 1.10 + index * 3.45
        _rounded_rect(
            ax,
            x,
            strip_y,
            2.80,
            0.48,
            color=COLORS["support"],
            alpha=0.14,
            edge_color=COLORS["support"],
            lw=0.8,
            radius=0.18,
            zorder=3,
        )
        ax.text(
            x + 1.40,
            strip_y + 0.24,
            label,
            ha="center",
            va="center",
            fontsize=8.8,
            fontweight="bold",
            color=COLORS["support"],
        )

    return fig


DIAGRAM_INFO = {
    "filename": "sysops-framework-diagram.png",
    "description": "Three-Cycle Operating Model",
    "chapter": 3,
}
