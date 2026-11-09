import reflex as rx

import Portfolio_v2.styles.styles as styles
from Portfolio_v2.styles.colors import TextColor
from Portfolio_v2.styles.fonts import Font


def section(
    section_id: str,
    eyebrow: str,
    title: str,
    description: str = "",
    *children: rx.Component,
) -> rx.Component:
    header: list[rx.Component] = [
        rx.text(
            eyebrow,
            font_family=Font.MONO.value,
            font_size="0.68rem",
            letter_spacing="0.18em",
            color=TextColor.MUTED.value,
            text_transform="uppercase",
        ),
        rx.heading(
            title,
            as_="h2",
            font_size=rx.breakpoints(initial="1.8rem", md="2.5rem"),
            line_height="1.15",
            color=TextColor.PRIMARY.value,
        ),
    ]

    if description:
        header.append(
            rx.text(
                description,
                font_size="1rem",
                color=TextColor.SECONDARY.value,
                max_width="680px",
            )
        )

    return rx.box(
        rx.vstack(*header, spacing="3", align="start", margin_bottom="3rem"),
        *children,
        id=section_id,
        width="100%",
        max_width=styles.MAX_WIDTH,
        margin="0 auto",
        padding_x=rx.breakpoints(initial="1.5rem", md="2rem"),
        padding_y=rx.breakpoints(initial="4rem", md="6rem"),
        scroll_margin_top=styles.NAV_HEIGHT,
    )
