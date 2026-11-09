import reflex as rx

import Portfolio_v2.styles.styles as styles


def tag(label: str) -> rx.Component:
    return rx.text(label, **styles.TAG_STYLE)


def tag_list(tags: list[str]) -> rx.Component:
    return rx.flex(
        *[tag(item) for item in tags],
        wrap="wrap",
        gap="0.5rem",
    )
