"""Generate a SysOps capability radar from team questionnaire responses."""

import argparse
import csv
import math
from pathlib import Path
from statistics import median

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


BG = "#FDF8F0"
SURFACE = "#FFFFFF"
DARK = "#3D1C49"
MID = "#5C3870"
MUTED = "#8A6090"
GRID = "#DEC9A8"
PURPLE = "#4F318B"
ORANGE = "#E87927"
GREEN = "#2A7A48"

KEYS = [
    "observability",
    "incident_response",
    "automation",
    "knowledge",
    "delivery_control",
    "asset_cost",
    "policy_enforcement",
]
LABELS = [
    "Observability",
    "Incident\nresponse",
    "Automation",
    "Knowledge",
    "Delivery\ncontrol",
    "Asset & cost\nvisibility",
    "Policy\nenforcement",
]
EXAMPLE = [2, 1, 1, 1, 2, 0, 0]
FOUNDATION = [2] * len(LABELS)
FOUNDATION_INDEXES = (0, 1, 3)
FIRST_MOVES = [
    "Monitor one critical user journey.",
    "Create one accountable alert route.",
    "Automate one documented repeated task.",
    "Write and test one critical runbook.",
    "Add validation and rollback to one change.",
    "Inventory critical services and owners.",
    "Automate one repeated objective check.",
]


def _closed(values):
    return values + values[:1]


def load_responses(path):
    """Return team medians, score ranges, and response count from a CSV file."""
    with Path(path).open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        required = ["respondent", *KEYS]
        missing = [field for field in required if field not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"Missing CSV columns: {', '.join(missing)}")

        answers = {key: [] for key in KEYS}
        response_count = 0
        for line_number, row in enumerate(reader, start=2):
            if not any((row.get(key) or "").strip() for key in KEYS):
                continue
            if not (row.get("respondent") or "").strip():
                raise ValueError(f"Line {line_number}: respondent is required")
            for key in KEYS:
                raw = (row.get(key) or "").strip()
                try:
                    value = int(raw)
                except ValueError as error:
                    raise ValueError(f"Line {line_number}: {key} must be 0, 1, 2, or 3") from error
                if value not in range(4):
                    raise ValueError(f"Line {line_number}: {key} must be 0, 1, 2, or 3")
                answers[key].append(value)
            response_count += 1

    if not response_count:
        raise ValueError("No completed response rows found")

    scores = [median(answers[key]) for key in KEYS]
    ranges = [(min(answers[key]), max(answers[key])) for key in KEYS]
    return scores, ranges, response_count


def _starting_capability(scores):
    weak_foundations = [index for index in FOUNDATION_INDEXES if scores[index] < 2]
    candidates = weak_foundations or list(range(len(scores)))
    return min(candidates, key=lambda index: scores[index])


def create_diagram(scores=None, ranges=None, team_name="Example team profile"):
    """Create a radar using team median scores."""
    scores = list(scores or EXAMPLE)
    ranges = ranges or [(score, score) for score in scores]
    start = _starting_capability(scores)
    spread = ranges[start][1] - ranges[start][0]

    fig = plt.figure(figsize=(13.5, 8), facecolor=BG)
    fig.text(
        0.5,
        0.955,
        "SysOps Capability Radar",
        ha="center",
        va="top",
        fontsize=22,
        fontweight="bold",
        color=DARK,
    )
    fig.text(
        0.5,
        0.91,
        f"{team_name} - team median shown; discuss score ranges of 2 or more",
        ha="center",
        va="top",
        fontsize=10.5,
        color=MID,
    )

    count = len(LABELS)
    angles = [index / count * 2 * math.pi for index in range(count)]
    closed_angles = angles + angles[:1]

    ax = fig.add_axes([0.055, 0.15, 0.57, 0.65], polar=True, facecolor=SURFACE)
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 3)
    ax.set_xticks(angles)
    ax.set_xticklabels(LABELS, fontsize=10, fontweight="bold", color=DARK)
    ax.tick_params(axis="x", pad=15)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["1  sometimes", "2  usually", "3  tested"], fontsize=8, color=MUTED)
    ax.set_rlabel_position(12)
    ax.grid(color=GRID, linewidth=0.9)
    ax.spines["polar"].set_color(GRID)

    ax.plot(
        closed_angles,
        _closed(FOUNDATION),
        color=ORANGE,
        linewidth=1.8,
        linestyle="--",
        label="Minimum useful foundation",
    )
    ax.plot(
        closed_angles,
        _closed(scores),
        color=PURPLE,
        linewidth=2.6,
        marker="o",
        markersize=6,
        label="Team median",
    )
    ax.fill(closed_angles, _closed(scores), color=PURPLE, alpha=0.18)
    ax.scatter(
        [angles[start]],
        [scores[start]],
        s=120,
        facecolor=ORANGE,
        edgecolor=SURFACE,
        linewidth=2,
        zorder=6,
    )

    legend = ax.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, -0.20),
        ncol=2,
        frameon=False,
        fontsize=9,
    )
    for text in legend.get_texts():
        text.set_color(MID)

    side = fig.add_axes([0.68, 0.15, 0.28, 0.65], facecolor=SURFACE)
    side.set_xticks([])
    side.set_yticks([])
    for spine in side.spines.values():
        spine.set_color(GRID)
        spine.set_linewidth(1.1)

    side.text(0.08, 0.92, "START HERE", transform=side.transAxes, fontsize=10, fontweight="bold", color=ORANGE)
    side.text(0.08, 0.84, LABELS[start].replace("\n", " "), transform=side.transAxes, fontsize=17, fontweight="bold", color=DARK)
    side.text(
        0.08,
        0.77,
        f"Team median {scores[start]:g}  |  answers {ranges[start][0]}-{ranges[start][1]}",
        transform=side.transAxes,
        fontsize=9.5,
        color=MID,
    )

    actions = [
        FIRST_MOVES[start],
        "Name one owner and one success signal.",
        "Run the change for 30 days.",
        "Ask the team again and compare evidence.",
    ]
    y = 0.64
    for number, action in enumerate(actions, start=1):
        side.add_patch(
            mpatches.Circle(
                (0.12, y + 0.015),
                0.034,
                transform=side.transAxes,
                facecolor=PURPLE,
                edgecolor="none",
            )
        )
        side.text(
            0.12,
            y + 0.015,
            str(number),
            transform=side.transAxes,
            ha="center",
            va="center",
            fontsize=8,
            fontweight="bold",
            color=SURFACE,
        )
        side.text(0.20, y, action, transform=side.transAxes, ha="left", va="center", fontsize=9.2, color=DARK)
        y -= 0.12

    side.plot([0.08, 0.92], [0.20, 0.20], transform=side.transAxes, color=GRID, linewidth=0.8)
    side.text(
        0.08,
        0.13,
        "Disagreement is useful.",
        transform=side.transAxes,
        fontsize=9,
        fontweight="bold",
        color=GREEN,
    )
    note = "A score spread of 2+ means the process\nis unclear; discuss it before buying tools."
    if spread < 2:
        note = "The team broadly agrees on this score.\nUse the evidence column to choose the move."
    side.text(0.08, 0.07, note, transform=side.transAxes, fontsize=8.7, color=MID, linespacing=1.35)

    return fig


def main():
    parser = argparse.ArgumentParser(description="Draw a SysOps radar from team questionnaire responses")
    parser.add_argument("input", help="CSV file with one completed row per respondent")
    parser.add_argument("--output", default="team-capability-radar.png", help="Output PNG path")
    parser.add_argument("--team", default="Team capability profile", help="Team name shown below the title")
    args = parser.parse_args()

    scores, ranges, count = load_responses(args.input)
    fig = create_diagram(scores, ranges, f"{args.team} ({count} responses)")
    fig.savefig(args.output, dpi=300, bbox_inches="tight", facecolor="white", edgecolor="none", pad_inches=0.2)
    plt.close(fig)


if __name__ == "__main__":
    main()


DIAGRAM_INFO = {
    "filename": "sysops-capability-radar.png",
    "description": "SysOps Capability Radar",
    "chapter": 8,
}
