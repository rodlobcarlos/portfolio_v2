import reflex as rx

import Portfolio_v2.styles.styles as styles
from Portfolio_v2.components.links import action_link, nav_links
from Portfolio_v2.data import PROFILE
from Portfolio_v2.styles.colors import Color, TextColor
from Portfolio_v2.styles.fonts import Font


def navbar(current_page: str = "home") -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.el.a(
                rx.hstack(
                    rx.text(
                        PROFILE["short_name"],
                        font_size="1rem",
                        font_weight="700",
                        letter_spacing="-0.04em",
                        color=TextColor.PRIMARY.value,
                    ),
                    rx.text(
                        ".dev",
                        font_family=Font.MONO.value,
                        font_size="0.8rem",
                        color=Color.ACCENT.value,
                    ),
                    spacing="0",
                    align="center",
                ),
                href="/" if current_page == "projects" else "#inicio",
                style={"text_decoration": "none"},
            ),
            rx.spacer(),
            nav_links(current_page),
            action_link(
                "CV",
                rx.asset(PROFILE["cv"]),
                primary=False,
                icon="file-text",
                download=PROFILE["cv"],
                compact=True,
            ),
            width="100%",
            align="center",
            justify="between",
            flex_wrap="wrap",
            gap="0.75rem",
        ),
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="50",
        width="100%",
        padding_x=rx.breakpoints(initial="1.25rem", md="2rem"),
        padding_y="0.8rem",
        background_color="rgba(18, 18, 18, 0.85)",
        backdrop_filter="blur(14px)",
        border_bottom=f"1px solid {Color.ACCENT_BORDER.value}",
    )
