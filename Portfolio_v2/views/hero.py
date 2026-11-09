import reflex as rx

import Portfolio_v2.styles.styles as styles
from Portfolio_v2.components.links import action_link
from Portfolio_v2.data import LINKS, PROFILE
from Portfolio_v2.styles.colors import Color, TextColor
from Portfolio_v2.styles.fonts import Font


def hero() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.hstack(
                    rx.box(
                        width="6px",
                        height="6px",
                        border_radius="full",
                        background_color=Color.ACCENT.value,
                    ),
                    rx.text(
                        "DISPONIBLE PARA NUEVOS RETOS",
                        font_family=Font.MONO.value,
                        font_size="0.66rem",
                        letter_spacing="0.18em",
                        color=TextColor.SECONDARY.value,
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.heading(
                    PROFILE["name"],
                    as_="h1",
                    font_size=rx.breakpoints(initial="2.3rem", md="4.4rem"),
                    line_height="1.05",
                    letter_spacing="-0.045em",
                    font_weight="600",
                    color=TextColor.PRIMARY.value,
                    max_width="760px",
                ),
                rx.text(
                    PROFILE["tagline"],
                    font_size=rx.breakpoints(initial="1rem", md="1.2rem"),
                    color=TextColor.SECONDARY.value,
                    max_width="620px",
                ),
                rx.hstack(
                    action_link(
                        "Ver proyectos",
                        "/proyectos",
                        primary=True,
                        new_tab=True,
                        icon="arrow-up-right",
                    ),
                    action_link(
                        "Descargar CV",
                        rx.asset(PROFILE["cv"]),
                        primary=False,
                        icon="download",
                        download=PROFILE["cv"],
                    ),
                    action_link(
                        "Contacto",
                        LINKS["gmail"],
                        primary=False,
                        new_tab=True,
                        icon="mail",
                    ),
                    spacing="3",
                    wrap="wrap",
                ),
                spacing="6",
                align="start",
                max_width="760px",
            ),
            rx.box(
                rx.image(
                    src=rx.asset("profile.jpg"),
                    alt=PROFILE["name"],
                    width="100%",
                    height="100%",
                    object_fit="cover",
                ),
                width=rx.breakpoints(initial="200px", md="280px"),
                height=rx.breakpoints(initial="250px", md="350px"),
                border=f"1px solid {Color.BORDER.value}",
                border_radius="1rem",
                overflow="hidden",
                flex_shrink="0",
                background_color=Color.SURFACE.value,
            ),
            direction=rx.breakpoints(initial="column-reverse", md="row"),
            justify="between",
            align="center",
            gap=rx.breakpoints(initial="2.5rem", md="4rem"),
            width="100%",
        ),
        id="inicio",
        width="100%",
        max_width=styles.MAX_WIDTH,
        margin="0 auto",
        padding_x=rx.breakpoints(initial="1.5rem", md="2rem"),
        padding_top=rx.breakpoints(initial="7.5rem", md="10rem"),
        padding_bottom=rx.breakpoints(initial="4rem", md="7rem"),
        scroll_margin_top=styles.NAV_HEIGHT,
    )
