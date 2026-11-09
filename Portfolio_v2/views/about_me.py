import reflex as rx

from Portfolio_v2.components.certifications import certifications
from Portfolio_v2.components.section import section
from Portfolio_v2.components.social_links import social_links
from Portfolio_v2.components.stack import stack
from Portfolio_v2.data import LINKS, PROFILE
from Portfolio_v2.styles.colors import Color, TextColor
from Portfolio_v2.styles.fonts import Font


def quick_fact(label: str, value: str, icon: str) -> rx.Component:
    return rx.hstack(
        rx.icon(icon, size=16, color=TextColor.MUTED.value),
        rx.vstack(
            rx.text(
                label,
                font_family=Font.MONO.value,
                font_size="0.65rem",
                letter_spacing="0.14em",
                color=TextColor.MUTED.value,
                text_transform="uppercase",
            ),
            rx.text(value, font_size="0.9rem", color=TextColor.PRIMARY.value),
            spacing="1",
            align="start",
        ),
        spacing="3",
        align="start",
        padding="0.9rem 0",
        border_bottom=f"1px solid {Color.BORDER.value}",
        width="100%",
    )


def about_me() -> rx.Component:
    return section(
        "sobre-mi",
        "01 — Sobre mí",
        "Un poco sobre mí",
        "Desarrollo, despliegue y aprendizaje continuo.",
        rx.grid(
            rx.vstack(
                rx.text(
                    PROFILE["bio"],
                    font_size="1rem",
                    color=TextColor.SECONDARY.value,
                ),
                rx.text(
                    PROFILE["bio_2"],
                    font_size="1rem",
                    color=TextColor.SECONDARY.value,
                ),
                rx.el.a(
                    rx.hstack(
                        "Hablemos",
                        rx.icon("arrow-up-right", size=16),
                        spacing="2",
                        align="center",
                    ),
                    href=LINKS["linkedin"],
                    target="_blank",
                    rel="noopener noreferrer",
                    style={
                        "font_size": "0.9rem",
                        "color": TextColor.PRIMARY.value,
                        "text_decoration": "none",
                        "margin_top": "0.5rem",
                    },
                    _hover={"color": TextColor.SECONDARY.value},
                ),
                spacing="4",
                align="start",
            ),
            rx.vstack(
                quick_fact("Ubicación", PROFILE["location"], "map-pin"),
                quick_fact("Modalidad", PROFILE["availability"], "globe"),
                quick_fact("Enfoque", PROFILE["focus"], "code"),
                quick_fact("Actualmente", PROFILE["current"], "briefcase"),
                spacing="0",
                align="start",
                padding="1.25rem",
                border=f"1px solid {Color.BORDER.value}",
                border_radius="0.75rem",
                background_color=Color.SURFACE.value,
                width="100%",
            ),
            columns=rx.breakpoints(initial="1", md="2"),
            spacing="8",
            width="100%",
            align="start",
        ),
        rx.divider(border_color=Color.BORDER.value, margin_y="3rem"),
        stack(),
        rx.divider(border_color=Color.BORDER.value, margin_y="3rem"),
        certifications(),
        rx.divider(border_color=Color.BORDER.value, margin_y="3rem"),
        social_links(),
    )
