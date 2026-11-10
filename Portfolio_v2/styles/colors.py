from enum import Enum


class Color(Enum):
    """Paleta oscura con acentos teal y menta."""

    BACKGROUND = "#121212"
    SURFACE = "#1A1A1A"
    SURFACE_ALT = "#202020"
    BORDER = "#2E2E2E"
    BORDER_STRONG = "#4A4A4A"
    ACCENT = "#2DD4BF"
    ACCENT_2 = "#5EEAD4"
    ACCENT_SOFT = "rgba(45, 212, 191, 0.10)"
    ACCENT_2_SOFT = "rgba(94, 234, 212, 0.10)"
    ACCENT_BORDER = "rgba(45, 212, 191, 0.35)"
    ACCENT_DARK = "#0B1210"
    DATABASE = "#22D3EE"
    DATABASE_SOFT = "rgba(34, 211, 238, 0.10)"
    DATABASE_BORDER = "rgba(34, 211, 238, 0.35)"
    SUCCESS = "#4ADE80"
    SUCCESS_SOFT = "rgba(74, 222, 128, 0.10)"
    SUCCESS_BORDER = "rgba(74, 222, 128, 0.35)"
    WARNING = "#FBBF24"
    WARNING_SOFT = "rgba(251, 191, 36, 0.10)"
    WARNING_BORDER = "rgba(251, 191, 36, 0.35)"


class TextColor(Enum):
    PRIMARY = "#F5F5F5"
    SECONDARY = "#B3B3B3"
    MUTED = "#808080"
    INVERSE = "#0B1210"
