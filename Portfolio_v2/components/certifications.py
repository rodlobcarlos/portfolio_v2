import reflex as rx

import Portfolio_v2.styles.styles as styles
from Portfolio_v2.data import CERTIFICATIONS
from Portfolio_v2.styles.colors import Color, TextColor
from Portfolio_v2.styles.fonts import Font


def cert_card(cert: dict) -> rx.Component:
    return rx.flex(
        rx.box(
            rx.image(
                src=rx.asset(cert["image"]),
                alt=cert["name"],
                width="100%",
                height="100%",
                object_fit="contain",
            ),
            width=rx.breakpoints(initial="96px", md="140px"),
            height=rx.breakpoints(initial="96px", md="140px"),
            padding="1rem",
            background_color=Color.SURFACE_ALT.value,
            border=f"1px solid {Color.BORDER.value}",
            border_radius="0.5rem",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.hstack(
                rx.text(
                    cert["issuer"],
                    font_family=Font.MONO.value,
                    font_size="0.68rem",
                    letter_spacing="0.14em",
                    color=Color.WARNING.value,
                    text_transform="uppercase",
                    font_weight="bold",
                ),
                rx.icon("award", size=14, color=Color.WARNING.value),
                spacing="2",
                align="center",
            ),
            rx.heading(
                cert["name"],
                as_="h3",
                font_size="1.1rem",
                font_weight="600",
                color=TextColor.PRIMARY.value,
            ),
            rx.text(
                cert["description"],
                font_size="0.9rem",
                color=TextColor.SECONDARY.value,
            ),
            rx.el.a(
                rx.hstack(
                    "Ver certificado",
                    rx.icon("arrow-up-right", size=14),
                    spacing="1",
                    align="center",
                ),
                href=cert["url"],
                target="_blank",
                rel="noopener noreferrer",
                style={
                    "font_size": "0.85rem",
                    "color": Color.ACCENT.value,
                    "text_decoration": "none",
                },
                _hover={"color": Color.ACCENT_2.value},
            ),
            spacing="2",
            align="start",
        ),
        spacing="4",
        direction=rx.breakpoints(initial="column", md="row"),
        align=rx.breakpoints(initial="start", md="center"),
        padding="1.25rem",
        border=f"1px solid {Color.BORDER.value}",
        border_radius="0.75rem",
        background_color=Color.SURFACE.value,
        background_image=styles.WARNING_GRADIENT_SUBTLE,
        transition="all 0.2s ease",
        _hover={"border_color": Color.WARNING_BORDER.value},
        width="100%",
    )


def certifications() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Certificaciones",
            font_family=Font.MONO.value,
            font_size="0.68rem",
            letter_spacing="0.18em",
            color=Color.WARNING.value,
            text_transform="uppercase",
        ),
        rx.vstack(
            *[cert_card(cert) for cert in CERTIFICATIONS],
            spacing="4",
            width="100%",
            max_width="760px",
        ),
        spacing="4",
        align="start",
        width="100%",
    )
