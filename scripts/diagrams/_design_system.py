"""
Shared design system for SysOps Framework diagrams.

Import in diagram modules:
    import sys, os
    sys.path.insert(0, os.path.dirname(__file__))
    from _design_system import COLORS, setup_figure, draw_card, bullet_list

Provides a consistent visual language (palette, typography, drawing helpers)
across all generated diagrams.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# ── Colour palette ──────────────────────────────────────────────────────────

# ── Retro Sunset colour palette ─────────────────────────────────────────────
# Source swatches: E8BD3B  E87927  DB4C46  AF3736  4F318B  3D1C49

COLORS = {
    # Raw palette entries
    "yellow":      "#E8BD3B",
    "orange":      "#E87927",
    "coral":       "#DB4C46",
    "red":         "#AF3736",
    "purple":      "#4F318B",
    "dark_purple": "#3D1C49",

    # Framework / cycle semantic aliases
    "scrum":   "#E87927",   # Orange
    "safe":    "#DB4C46",   # Coral
    "sysops":  "#4F318B",   # Purple
    "daily":   "#E87927",
    "weekly":  "#DB4C46",
    "monthly": "#4F318B",
    "support": "#E8BD3B",   # Golden yellow

    # Roadmap phase colours
    "phase1":  "#E8BD3B",
    "phase2":  "#E87927",
    "phase3":  "#DB4C46",
    "phase4":  "#AF3736",
    "phase5":  "#4F318B",

    # Status / health colours (keep semantic)
    "healthy":  "#2A7A48",
    "warning":  "#E87927",
    "critical": "#AF3736",

    # Structural / neutral (warm-toned)
    "bg":      "#FDF8F0",   # Warm off-white page background
    "surface": "#FFFFFF",   # Card/panel surface
    "border":  "#DEC9A8",   # Warm subtle border
    "divider": "#EFE0C8",   # Section divider
    "dark":    "#3D1C49",   # Primary text (dark purple)
    "mid":     "#5C3870",   # Secondary text
    "light":   "#8A6090",   # Tertiary text
    "muted":   "#B09AB8",   # Caption / footnote
    "white":   "#FFFFFF",
}

# ── Typography scale ─────────────────────────────────────────────────────────

FONTS = {
    "title":   20,   # Figure super-title
    "panel":   14,   # Card / panel header
    "section": 12,   # Section label inside a card
    "body":    12,   # Bullet / body text
    "small":   10,   # Footnotes, captions
    "badge":   11,   # Badge / pill label
    "axis":    12,   # Column / axis header labels
}


# ── Global rcParams ──────────────────────────────────────────────────────────

def apply_global_style():
    """Apply consistent rcParams before creating figures."""
    plt.rcParams.update({
        "font.family":       "DejaVu Sans",
        "font.size":         FONTS["body"],
        "figure.facecolor":  COLORS["bg"],
        "axes.facecolor":    COLORS["bg"],
        "text.color":        COLORS["dark"],
        "figure.dpi":        150,   # screen preview; generator overrides to 300
        "savefig.facecolor": COLORS["bg"],
    })


# ── Figure / axes helpers ────────────────────────────────────────────────────

def setup_figure(figsize, title="", title_y=0.96):
    """
    Create a styled figure.  Returns (fig, ax) where ax covers the full
    figure area (axis turned off) — use it as a drawing canvas.
    """
    apply_global_style()
    fig = plt.figure(figsize=figsize, facecolor=COLORS["bg"])
    ax  = fig.add_axes([0.0, 0.0, 1.0, 1.0])
    ax.set_facecolor(COLORS["bg"])
    ax.axis("off")
    if title:
        fig.text(
            0.5, title_y, title,
            ha="center", va="top",
            fontsize=FONTS["title"], fontweight="bold", color=COLORS["dark"],
        )
    return fig, ax


def set_lims(ax, xlim, ylim):
    """Convenience: set axis limits without touching other settings."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)


# ── Low-level drawing primitives ─────────────────────────────────────────────

def _rounded_rect(ax, x, y, w, h, color, alpha=1.0, edge_color=None,
                  lw=1.5, radius=0.14, zorder=2):
    """Draw a single rounded rectangle and return the patch."""
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        facecolor=color, edgecolor=edge_color if edge_color else color,
        alpha=alpha, linewidth=lw, zorder=zorder,
    )
    ax.add_patch(patch)
    return patch


def shadow(ax, x, y, w, h, radius=0.14, zorder=1):
    """Draw a subtle drop-shadow under a card."""
    _rounded_rect(ax, x + 0.07, y - 0.07, w, h,
                  color="#00000018", alpha=1.0,
                  edge_color="none", lw=0, radius=radius, zorder=zorder)


# ── High-level card / panel helpers ─────────────────────────────────────────

def draw_card(ax, x, y, w, h, accent, title=None,
              header_h=0.52, radius=0.14, with_shadow=True):
    """
    Draw a white card with an optional solid coloured header band.

    Parameters
    ----------
    x, y    : bottom-left corner of the card (data coords)
    w, h    : width and height of the card
    accent  : hex colour used for the header and border
    title   : text to display in the header (omit for no header)
    header_h: height of the header band
    radius  : corner rounding radius (data coords)
    """
    if with_shadow:
        shadow(ax, x, y, w, h, radius=radius)

    # Card body
    _rounded_rect(ax, x, y, w, h,
                  color=COLORS["surface"], edge_color=accent,
                  lw=1.6, radius=radius, zorder=2)

    if not title:
        return

    # Coloured header (top portion)
    _rounded_rect(ax, x, y + h - header_h, w, header_h,
                  color=accent, edge_color="none", lw=0,
                  radius=radius, zorder=3)
    # Flatten the bottom edge of the header (hide lower rounding)
    ax.add_patch(Rectangle(
        (x, y + h - header_h), w, header_h / 2,
        facecolor=accent, edgecolor="none", zorder=3,
    ))
    # Title text
    ax.text(
        x + w / 2, y + h - header_h / 2, title,
        ha="center", va="center",
        fontsize=FONTS["panel"], fontweight="bold", color=COLORS["white"], zorder=4,
    )


def draw_section_label(ax, x, y, w, text, accent, fontsize=None, zorder=4):
    """Draw a small accent-coloured section divider label inside a card."""
    if fontsize is None:
        fontsize = FONTS["section"]
    ax.add_patch(Rectangle(
        (x, y - 0.14), w, 0.40,
        facecolor=accent, alpha=0.14, edgecolor="none", zorder=zorder,
    ))
    ax.text(
        x + 0.14, y + 0.06, text,
        ha="left", va="center",
        fontsize=fontsize, fontweight="bold", color=accent, zorder=zorder + 1,
    )


def draw_h_divider(ax, x, y, w, color=None, lw=0.8, zorder=4):
    """Draw a thin horizontal rule inside a card."""
    if color is None:
        color = COLORS["divider"]
    ax.plot([x, x + w], [y, y], color=color, lw=lw, zorder=zorder)


# ── Text / bullet helpers ───────────────────────────────────────────────────

def bullet_list(ax, x, y_top, items, dy=0.55, fontsize=None,
                color=None, indent=0.24, zorder=5):
    """
    Draw a vertical list of bullet-point items.

    Parameters
    ----------
    x     : left x of text block
    y_top : y of the *first* item
    items : list of strings
    dy    : vertical spacing between items
    """
    if color is None:
        color = COLORS["mid"]
    if fontsize is None:
        fontsize = FONTS["body"]
    for i, item in enumerate(items):
        ax.text(
            x + indent, y_top - i * dy,
            f"\u2022  {item}",
            ha="left", va="center",
            fontsize=fontsize, color=color, zorder=zorder,
        )


def label_badge(ax, x, y, text, color, fontsize=None, zorder=5):
    """Draw a small pill-shaped coloured label."""
    if fontsize is None:
        fontsize = FONTS["badge"]
    ax.text(
        x, y, text,
        ha="center", va="center",
        fontsize=fontsize, fontweight="bold", color=COLORS["white"],
        zorder=zorder,
        bbox=dict(
            boxstyle="round,pad=0.35",
            facecolor=color, edgecolor="none", alpha=0.9,
        ),
    )


# ── Arrow helpers ────────────────────────────────────────────────────────────

def arrow_h(ax, x1, x2, y, color, lw=2.0, mutation_scale=16, zorder=5):
    """Horizontal arrow from (x1, y) to (x2, y)."""
    ax.annotate(
        "", xy=(x2, y), xytext=(x1, y),
        arrowprops=dict(
            arrowstyle="-|>", color=color,
            lw=lw, mutation_scale=mutation_scale,
        ),
        zorder=zorder,
    )


def arrow_curved(ax, x1, y1, x2, y2, color, rad=0.35, lw=2.0,
                 mutation_scale=16, zorder=5):
    """Curved arrow using ConnectionPatch-style annotation."""
    ax.annotate(
        "", xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="-|>", color=color,
            lw=lw, mutation_scale=mutation_scale,
            connectionstyle=f"arc3,rad={rad}",
        ),
        zorder=zorder,
    )


def arrow_dashed(ax, x1, y1, x2, y2, color, lw=1.4,
                 mutation_scale=14, zorder=5):
    """Dashed arrow for supporting / auxiliary connections."""
    ax.annotate(
        "", xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="-|>", color=color,
            lw=lw, mutation_scale=mutation_scale,
            linestyle="dashed",
        ),
        zorder=zorder,
    )
