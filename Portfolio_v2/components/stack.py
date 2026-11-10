import reflex as rx

import Portfolio_v2.styles.styles as styles
from Portfolio_v2.data import STACK
from Portfolio_v2.styles.colors import Color, TextColor
from Portfolio_v2.styles.fonts import Font


def tech_chip(item: dict) -> rx.Component:
    icon = item.get("icon")

    return rx.hstack(
        rx.image(
            src=rx.asset(icon),
            alt=item["name"],
            width="18px",
            height="18px",
            object_fit="contain",
            transition="transform 0.2s ease",
            _hover={"transform": "scale(1.12)"},
        )
        if icon
        else rx.box(
            width="6px",
            height="6px",
            border_radius="full",
            background_color=Color.ACCENT.value,
        ),
        rx.text(item["name"], font_size="0.82rem", color=TextColor.SECONDARY.value),
        spacing="2",
        align="center",
        padding="0.45rem 0.7rem",
        border=f"1px solid {Color.BORDER.value}",
        border_radius="0.5rem",
        background_color=Color.SURFACE_ALT.value,
        transition="all 0.2s ease",
        _hover={
            "border_color": Color.ACCENT_BORDER.value,
            "background_color": Color.SURFACE.value,
        },
    )


GROUP_COLORS = {
    "Backend": (Color.ACCENT.value, Color.ACCENT_SOFT.value),
    "Frontend": (Color.ACCENT_2.value, Color.ACCENT_2_SOFT.value),
    "DevOps": (Color.SUCCESS.value, Color.SUCCESS_SOFT.value),
    "Base de datos": (Color.DATABASE.value, Color.DATABASE_SOFT.value),
}


def stack_group(group: dict) -> rx.Component:
    accent, soft = GROUP_COLORS.get(
        group["name"], (Color.ACCENT.value, Color.ACCENT_SOFT.value)
    )

    return rx.vstack(
        rx.hstack(
            rx.icon(group["icon"], size=16, color=accent),
            rx.text(
                group["name"],
                font_size="0.9rem",
                font_weight="500",
                color=TextColor.PRIMARY.value,
            ),
            spacing="2",
            align="center",
        ),
        rx.flex(
            *[tech_chip(item) for item in group["items"]],
            wrap="wrap",
            gap="0.6rem",
        ),
        spacing="4",
        align="start",
        padding="1.25rem",
        border=f"1px solid {Color.BORDER.value}",
        border_left=f"2px solid {accent}",
        border_radius="0.75rem",
        background_color=Color.SURFACE.value,
        background_image=f"linear-gradient(135deg, {soft} 0%, transparent 60%)",
        height="100%",
    )


def stack() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Stack tecnológico",
            font_family=Font.MONO.value,
            font_size="0.68rem",
            letter_spacing="0.18em",
            color=Color.ACCENT.value,
            text_transform="uppercase",
        ),
        rx.grid(
            *[stack_group(group) for group in STACK],
            columns=rx.breakpoints(initial="1", md="2"),
            spacing="4",
            width="100%",
        ),
        spacing="4",
        align="start",
        width="100%",
    )
