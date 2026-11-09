import reflex as rx

import Portfolio_v2.styles.styles as styles
from Portfolio_v2.data import PROFILE, SOCIALS
from Portfolio_v2.styles.colors import Color, TextColor
from Portfolio_v2.styles.fonts import Font


def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.divider(border_color=Color.BORDER.value),
            rx.hstack(
                rx.text(
                    f"© 2026 {PROFILE['name']}",
                    font_size="0.8rem",
                    color=TextColor.MUTED.value,
                ),
                rx.spacer(),
                rx.hstack(
                    *[
                        rx.el.a(
                            social["name"],
                            href=social["url"],
                            target="_blank",
                            rel="noopener noreferrer",
                            style={
                                "font_size": "0.8rem",
                                "color": TextColor.MUTED.value,
                                "text_decoration": "none",
                            },
                            _hover={"color": TextColor.PRIMARY.value},
                        )
                        for social in SOCIALS
                    ],
                    spacing="4",
                    wrap="wrap",
                ),
                width="100%",
                align="center",
                wrap="wrap",
                gap="1rem",
            ),
            rx.text(
                "Hecho con Reflex y Python.",
                font_family=Font.MONO.value,
                font_size="0.68rem",
                color=TextColor.MUTED.value,
            ),
            spacing="4",
            max_width=styles.MAX_WIDTH,
            margin="0 auto",
            padding_x=rx.breakpoints(initial="1.5rem", md="2rem"),
            padding_y="2rem",
            width="100%",
        ),
        width="100%",
    )
