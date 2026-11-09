from enum import Enum


class Color(Enum):
    """Paleta monocroma oscura."""

    BACKGROUND = "#0A0A0A"
    SURFACE = "#111111"
    SURFACE_ALT = "#171717"
    BORDER = "#262626"
    BORDER_STRONG = "#404040"
    ACCENT = "#FFFFFF"
    ACCENT_MUTED = "#D4D4D4"


class TextColor(Enum):
    PRIMARY = "#F5F5F5"
    SECONDARY = "#A3A3A3"
    MUTED = "#737373"
    INVERSE = "#0A0A0A"
