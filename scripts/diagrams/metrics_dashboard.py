"""Generate the Chapter 7 observability-style metrics dashboard."""

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


BG = "#111217"
PANEL = "#181B1F"
GRID = "#2B3038"
TEXT = "#D8D9DA"
MUTED = "#8E9299"
GREEN = "#73BF69"
YELLOW = "#F2CC0C"
ORANGE = "#FF9830"
RED = "#F2495C"
BLUE = "#5794F2"
PURPLE = "#B877D9"


def _panel(fig, rect, title):
    ax = fig.add_axes(rect, facecolor=PANEL)
    for spine in ax.spines.values():
        spine.set_color(GRID)
        spine.set_linewidth(1)
    ax.tick_params(colors=MUTED, labelsize=8)
    ax.grid(color=GRID, linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)
    ax.text(
        0.025,
        0.95,
        title,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        fontweight="bold",
        color=TEXT,
    )
    return ax


def _stat(fig, x, title, value, color, detail):
    ax = _panel(fig, [x, 0.745, 0.215, 0.145], title)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    ax.text(
        0.05,
        0.46,
        value,
        transform=ax.transAxes,
        ha="left",
        va="center",
        fontsize=27,
        fontweight="bold",
        color=color,
    )
    ax.text(
        0.05,
        0.14,
        detail,
        transform=ax.transAxes,
        ha="left",
        va="center",
        fontsize=8.5,
        color=MUTED,
    )
    ax.add_patch(
        mpatches.Circle(
            (0.91, 0.48),
            0.035,
            transform=ax.transAxes,
            facecolor=color,
            edgecolor="none",
        )
    )


def _style_timeseries(ax, y_ticks=None, y_labels=None):
    ax.set_xlim(1, 30)
    ax.set_xticks([1, 5, 10, 15, 20, 25, 30])
    ax.set_xticklabels(["Jul 1", "5", "10", "15", "20", "25", "30"])
    if y_ticks is not None:
        ax.set_yticks(y_ticks)
    if y_labels is not None:
        ax.set_yticklabels(y_labels)


def create_diagram():
    """Create an illustrative operations dashboard."""
    fig = plt.figure(figsize=(16, 9), facecolor=BG)

    fig.text(
        0.035,
        0.955,
        "SysOps / Operations Overview",
        ha="left",
        va="top",
        fontsize=20,
        fontweight="bold",
        color=TEXT,
    )
    fig.text(
        0.035,
        0.918,
        "production  |  last 30 days  |  illustrative data - replace with your baseline",
        ha="left",
        va="top",
        fontsize=9,
        color=MUTED,
    )
    fig.text(
        0.965,
        0.947,
        "refreshed 5m ago",
        ha="right",
        va="top",
        fontsize=8.5,
        color=MUTED,
    )

    _stat(fig, 0.035, "Availability", "99.97%", GREEN, "SLO 99.90%  |  +0.03% vs baseline")
    _stat(fig, 0.275, "Error budget remaining", "72%", GREEN, "30-day window  |  8h 38m available")
    _stat(fig, 0.515, "Median time to recover", "23m", YELLOW, "target < 30m  |  n=7 incidents")
    _stat(fig, 0.755, "Open incidents", "1", ORANGE, "SEV1 0  |  SEV2 1  |  SEV3/4 0")

    days = list(range(1, 31))
    availability = [
        99.97, 99.98, 99.96, 99.99, 99.97, 99.95, 99.94, 99.97, 99.98, 99.99,
        99.98, 99.96, 99.91, 99.86, 99.93, 99.97, 99.98, 99.99, 99.98, 99.96,
        99.95, 99.97, 99.98, 99.99, 99.97, 99.96, 99.94, 99.98, 99.99, 99.97,
    ]
    burn = [
        0.12, 0.10, 0.18, 0.08, 0.15, 0.22, 0.25, 0.14, 0.09, 0.07,
        0.11, 0.16, 0.38, 1.18, 0.52, 0.20, 0.13, 0.08, 0.10, 0.17,
        0.22, 0.14, 0.11, 0.09, 0.16, 0.19, 0.28, 0.12, 0.08, 0.14,
    ]

    ax = _panel(fig, [0.035, 0.425, 0.57, 0.275], "Service reliability")
    _style_timeseries(ax, [99.8, 99.9, 100.0], ["99.80%", "99.90%", "100%"])
    ax.set_ylim(99.78, 100.02)
    ax.plot(days, availability, color=GREEN, linewidth=2.2, label="Availability")
    ax.fill_between(days, availability, 99.78, color=GREEN, alpha=0.10)
    ax.axhline(99.90, color=YELLOW, linewidth=1.2, linestyle="--", label="SLO threshold")
    ax.axvline(14, color=RED, linewidth=1, alpha=0.75)
    ax.text(14.25, 99.805, "SEV2", color=RED, fontsize=8, va="bottom")
    legend = ax.legend(
        loc="lower left",
        ncol=2,
        frameon=False,
        fontsize=8,
        labelcolor=TEXT,
    )
    for line in legend.get_lines():
        line.set_linewidth(2)

    ax = _panel(fig, [0.63, 0.425, 0.335, 0.275], "Error budget burn rate")
    _style_timeseries(ax, [0, 0.5, 1.0, 1.5], ["0x", "0.5x", "1x", "1.5x"])
    ax.set_ylim(0, 1.5)
    ax.plot(days, burn, color=BLUE, linewidth=2)
    ax.fill_between(days, burn, color=BLUE, alpha=0.12)
    ax.axhline(1.0, color=RED, linewidth=1.2, linestyle="--")
    ax.text(29.5, 1.04, "budget consumed faster than window", color=RED, fontsize=7.5, ha="right")

    reactive = [42, 39, 45, 44, 41, 38, 36, 35]
    improvement = [8, 10, 9, 12, 14, 15, 17, 18]
    weeks = list(range(1, 9))
    ax = _panel(fig, [0.035, 0.085, 0.37, 0.285], "Operational load - hours per week")
    ax.set_xlim(1, 8)
    ax.set_xticks(weeks)
    ax.set_xticklabels([f"W{i}" for i in weeks])
    ax.set_ylim(0, 50)
    ax.plot(weeks, reactive, color=ORANGE, marker="o", linewidth=2, label="Reactive")
    ax.plot(weeks, improvement, color=BLUE, marker="o", linewidth=2, label="Improvement")
    ax.legend(loc="upper right", frameon=False, fontsize=8, labelcolor=TEXT)

    change_rate = [91, 93, 95, 92, 96, 97, 94, 96]
    ax = _panel(fig, [0.43, 0.085, 0.255, 0.285], "Change success rate")
    ax.set_xlim(1, 8)
    ax.set_xticks(weeks)
    ax.set_xticklabels([f"W{i}" for i in weeks])
    ax.set_ylim(85, 100)
    ax.set_yticks([85, 90, 95, 100])
    ax.set_yticklabels(["85%", "90%", "95%", "100%"])
    ax.plot(weeks, change_rate, color=PURPLE, marker="o", linewidth=2)
    ax.axhline(95, color=GREEN, linewidth=1.2, linestyle="--")
    ax.text(8, 95.4, "target", color=GREEN, fontsize=8, ha="right")

    ax = _panel(fig, [0.71, 0.085, 0.255, 0.285], "Incident volume")
    severities = ["SEV1", "SEV2", "SEV3", "SEV4"]
    counts = [0, 2, 5, 11]
    colors = [RED, ORANGE, YELLOW, BLUE]
    bars = ax.barh(severities, counts, color=colors, height=0.55)
    ax.set_xlim(0, 12)
    ax.set_xticks([0, 3, 6, 9, 12])
    ax.invert_yaxis()
    for bar, count in zip(bars, counts):
        ax.text(
            count + 0.25,
            bar.get_y() + bar.get_height() / 2,
            str(count),
            ha="left",
            va="center",
            fontsize=9,
            fontweight="bold",
            color=TEXT,
        )

    return fig


DIAGRAM_INFO = {
    "filename": "sysops-dashboard.png",
    "description": "Observability-Style Metrics Dashboard",
    "chapter": 7,
}
