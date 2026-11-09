import reflex as rx

from Portfolio_v2.data import SOCIALS
from Portfolio_v2.styles.colors import Color, TextColor


def social_links() -> rx.Component:
    return rx.flex(
        *[
            rx.el.a(
                rx.hstack(
                    rx.icon(social["icon"], size=16),
                    rx.text(social["name"], font_size="0.85rem"),
                    spacing="2",
                    align="center",
                ),
                href=social["url"],
                target="_blank",
                rel="noopener noreferrer",
                style={
                    "color": TextColor.SECONDARY.value,
                    "text_decoration": "none",
                    "padding": "0.55rem 0.8rem",
                    "border": f"1px solid {Color.BORDER.value}",
                    "border_radius": "0.5rem",
                    "background_color": Color.SURFACE.value,
                    "transition": "all 0.2s ease",
                },
                _hover={
                    "color": TextColor.PRIMARY.value,
                    "border_color": Color.BORDER_STRONG.value,
                },
            )
            for social in SOCIALS
        ],
        wrap="wrap",
        gap="0.6rem",
    )
