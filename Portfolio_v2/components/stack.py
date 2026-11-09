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
            filter="grayscale(1)",
            opacity="0.8",
            transition="all 0.2s ease",
            _hover={"filter": "grayscale(0)", "opacity": "1"},
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
        background_color=Color.SURFACE.value,
        transition="border-color 0.2s ease",
        _hover={"border_color": Color.BORDER_STRONG.value},
    )


def stack() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Stack tecnológico",
            font_family=Font.MONO.value,
            font_size="0.68rem",
            letter_spacing="0.18em",
            color=TextColor.MUTED.value,
            text_transform="uppercase",
        ),
        rx.grid(
            *[
                rx.vstack(
                    rx.hstack(
                        rx.icon(
                            group["icon"],
                            size=16,
                            color=TextColor.SECONDARY.value,
                        ),
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
                    border_radius="0.75rem",
                    background_color=Color.SURFACE.value,
                    height="100%",
                )
                for group in STACK
            ],
            columns=rx.breakpoints(initial="1", md="2"),
            spacing="4",
            width="100%",
        ),
        spacing="4",
        align="start",
        width="100%",
    )
