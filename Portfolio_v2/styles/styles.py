import reflex as rx
from enum import Enum

from .colors import Color, TextColor
from .fonts import Font


class Size(Enum):
    """Tamaños reutilizables (se mantiene la clase por compatibilidad)."""

    SMALL = "0.5rem"
    MEDIUM = "1rem"
    LARGE = "1.5rem"
    XL = "2rem"
    BIG = "3rem"


MAX_WIDTH = "1120px"
NAV_HEIGHT = "72px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap",
    "/styles.css",
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background_color": Color.BACKGROUND.value,
    "::selection": {
        "background_color": Color.ACCENT.value,
        "color": Color.BACKGROUND.value,
    },
    rx.heading: {
        "font_weight": "600",
        "letter_spacing": "-0.03em",
    },
    rx.text: {
        "line_height": "1.7",
    },
}

CUSTOM_STYLE = {
    "@keyframes fadeIn": {
        "0%": {"opacity": "0", "transform": "translateY(8px)"},
        "100%": {"opacity": "1", "transform": "translateY(0)"},
    },
}

BUTTON_PRIMARY = {
    "display": "inline-flex",
    "align_items": "center",
    "justify_content": "center",
    "gap": "0.5rem",
    "background_color": Color.ACCENT.value,
    "color": Color.BACKGROUND.value,
    "border": "1px solid transparent",
    "border_radius": "0.5rem",
    "padding": "0.7rem 1.15rem",
    "font_size": "0.9rem",
    "font_weight": "500",
    "cursor": "pointer",
    "transition": "all 0.2s ease",
    "white_space": "nowrap",
}

BUTTON_PRIMARY_HOVER = {
    "background_color": Color.ACCENT_MUTED.value,
}

BUTTON_SECONDARY = {
    "display": "inline-flex",
    "align_items": "center",
    "justify_content": "center",
    "gap": "0.5rem",
    "background_color": "transparent",
    "color": TextColor.PRIMARY.value,
    "border": f"1px solid {Color.BORDER_STRONG.value}",
    "border_radius": "0.5rem",
    "padding": "0.7rem 1.15rem",
    "font_size": "0.9rem",
    "font_weight": "500",
    "cursor": "pointer",
    "transition": "all 0.2s ease",
    "white_space": "nowrap",
}

BUTTON_SECONDARY_HOVER = {
    "border_color": TextColor.SECONDARY.value,
    "background_color": Color.SURFACE.value,
}

TAG_STYLE = {
    "font_family": Font.MONO.value,
    "font_size": "0.68rem",
    "color": TextColor.SECONDARY.value,
    "border": f"1px solid {Color.BORDER.value}",
    "border_radius": "999px",
    "padding": "0.25rem 0.6rem",
    "white_space": "nowrap",
}
