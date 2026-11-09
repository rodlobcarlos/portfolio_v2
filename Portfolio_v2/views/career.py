import reflex as rx

from Portfolio_v2.components.section import section
from Portfolio_v2.components.tags import tag_list
from Portfolio_v2.data import CAREER
from Portfolio_v2.styles.colors import Color, TextColor
from Portfolio_v2.styles.fonts import Font


def timeline_item(item: dict, is_last: bool) -> rx.Component:
    return rx.box(
        rx.box(
            width="9px",
            height="9px",
            border_radius="full",
            background_color=Color.ACCENT.value,
            position="absolute",
            left="-5px",
            top="0.45rem",
        ),
        rx.vstack(
            rx.hstack(
                rx.text(
                    item["period"],
                    font_family=Font.MONO.value,
                    font_size="0.7rem",
                    color=TextColor.MUTED.value,
                ),
                rx.text(
                    item["type"],
                    font_family=Font.MONO.value,
                    font_size="0.62rem",
                    letter_spacing="0.12em",
                    color=TextColor.SECONDARY.value,
                    text_transform="uppercase",
                    padding="0.15rem 0.45rem",
                    border=f"1px solid {Color.BORDER.value}",
                    border_radius="999px",
                ),
                spacing="3",
                align="center",
                wrap="wrap",
            ),
            rx.heading(
                item["title"],
                as_="h3",
                font_size="1.1rem",
                font_weight="600",
                color=TextColor.PRIMARY.value,
            ),
            rx.text(
                item["organization"],
                font_size="0.9rem",
                color=TextColor.SECONDARY.value,
            ),
            rx.text(
                item["description"],
                font_size="0.95rem",
                color=TextColor.SECONDARY.value,
            ),
            tag_list(item["tags"]),
            spacing="2",
            align="start",
            padding_bottom="0" if is_last else "2.5rem",
            width="100%",
        ),
        position="relative",
        border_left=f"1px solid {Color.BORDER.value}",
        padding_left="1.75rem",
        width="100%",
    )


def career() -> rx.Component:
    return section(
        "trayectoria",
        "02 — Trayectoria",
        "Experiencia y formación",
        "Mi recorrido profesional y académico, de lo más reciente a lo más antiguo.",
        rx.vstack(
            *[
                timeline_item(item, index == len(CAREER) - 1)
                for index, item in enumerate(CAREER)
            ],
            spacing="0",
            width="100%",
            max_width="820px",
        ),
    )
