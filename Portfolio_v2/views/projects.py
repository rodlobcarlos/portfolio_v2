import reflex as rx

import Portfolio_v2.styles.styles as styles
from Portfolio_v2.components.background import animated_background
from Portfolio_v2.components.tags import tag_list
from Portfolio_v2.data import PROJECTS
from Portfolio_v2.styles.colors import Color, TextColor
from Portfolio_v2.styles.fonts import Font
from Portfolio_v2.views.footer import footer
from Portfolio_v2.views.navbar import navbar


def project_visual(project: dict, index: int) -> rx.Component:
    is_alt = index % 2 == 1
    accent = Color.SUCCESS.value if is_alt else Color.ACCENT.value
    soft = Color.SUCCESS_SOFT.value if is_alt else Color.ACCENT_SOFT.value
    visual_background = (
        f"radial-gradient(circle at 30% 20%, {soft}, transparent 65%), "
        f"linear-gradient(135deg, {Color.SURFACE_ALT.value}, "
        f"{Color.SURFACE.value})"
    )

    if project.get("image"):
        return rx.box(
            rx.image(
                src=rx.asset(project["image"]),
                alt=project["title"],
                width="100%",
                height="100%",
                object_fit="cover",
                object_position="center",
                transition="transform 0.35s ease",
                _hover={"transform": "scale(1.04)"},
            ),
            width="100%",
            height="170px",
            flex_shrink="0",
            overflow="hidden",
            border_bottom=f"1px solid {Color.BORDER.value}",
            background_color=Color.SURFACE_ALT.value,
        )

    return rx.box(
        rx.icon(
            project.get("icon", "code"),
            size=36,
            color=accent,
        ),
        width="100%",
        height="170px",
        flex_shrink="0",
        display="flex",
        align_items="center",
        justify_content="center",
        border_bottom=f"1px solid {Color.BORDER.value}",
        background_image=visual_background,
    )


def project_card(project: dict, index: int) -> rx.Component:
    links: list[rx.Component] = [
        rx.el.a(
            "Ver en GitHub",
            href=project["github"],
            target="_blank",
            rel="noopener noreferrer",
            style={
                "font_size": "0.82rem",
                "color": Color.ACCENT.value,
                "text_decoration": "none",
            },
            _hover={"color": Color.ACCENT_2.value},
        ),
    ]
    if project.get("linkedin_portfolio"):
        links.append(
            rx.el.a(
                "Ver en LinkedIn",
                href=project["linkedin_portfolio"],
                target="_blank",
                rel="noopener noreferrer",
                style={
                    "font_size": "0.82rem",
                    "color": Color.ACCENT.value,
                    "text_decoration": "none",
                },
                _hover={"color": Color.ACCENT_2.value},
            )
        )

    if project.get("linkedin_devops"):
        links.append(
            rx.el.a(
                "Ver en LinkedIn",
                href=project["linkedin_devops"],
                target="_blank",
                rel="noopener noreferrer",
                style={
                    "font_size": "0.82rem",
                    "color": Color.ACCENT.value,
                    "text_decoration": "none",
                },
                _hover={"color": Color.ACCENT_2.value},
            )
        )

    if project.get("demo"):
        links.append(
            rx.el.a(
                "Demo",
                href=project["demo"],
                target="_blank",
                rel="noopener noreferrer",
                style={
                    "font_size": "0.82rem",
                    "color": Color.ACCENT.value,
                    "text_decoration": "none",
                },
                _hover={"color": Color.ACCENT_2.value},
            )
        )

    return rx.box(
        project_visual(project, index),
        rx.vstack(
            rx.hstack(
                rx.text(
                    f"0{index + 1}",
                    font_family=Font.MONO.value,
                    font_size="0.68rem",
                    color=Color.ACCENT.value,
                ),
                rx.spacer(),
                rx.el.a(
                    rx.icon("arrow-up-right", size=16),
                    href=project["github"],
                    target="_blank",
                    rel="noopener noreferrer",
                    style={
                        "color": TextColor.MUTED.value,
                        "text_decoration": "none",
                    },
                    _hover={"color": Color.ACCENT.value},
                ),
                width="100%",
                align="center",
            ),
            rx.heading(
                project["title"],
                as_="h3",
                font_size="1.15rem",
                font_weight="600",
                line_height="1.3",
                color=TextColor.PRIMARY.value,
            ),
            rx.text(
                project["description"],
                font_size="0.92rem",
                color=TextColor.SECONDARY.value,
            ),
            tag_list(project["tech"]),
            rx.hstack(
                *links,
                spacing="4",
                margin_top="auto",
                padding_top="0.5rem",
            ),
            spacing="3",
            align="start",
            padding="1.25rem",
            flex="1",
        ),
        border=f"1px solid {Color.BORDER.value}",
        border_radius="0.75rem",
        overflow="hidden",
        background_color=Color.SURFACE.value,
        transition="all 0.2s ease",
        _hover={
            "border_color": Color.ACCENT_BORDER.value,
            "transform": "translateY(-2px)",
            "box_shadow": "0 14px 34px rgba(0, 0, 0, 0.35)",
        },
        height="100%",
        display="flex",
        flex_direction="column",
    )


def projects_page() -> rx.Component:
    return rx.box(
        animated_background(),
        rx.box(
            navbar("projects"),
            rx.box(
                rx.vstack(
                    rx.text(
                        "PROYECTOS",
                        font_family=Font.MONO.value,
                        font_size="0.68rem",
                        letter_spacing="0.18em",
                        color=Color.ACCENT.value,
                    ),
                    rx.heading(
                        "Cosas que he construido",
                        as_="h1",
                        font_size=rx.breakpoints(initial="2.2rem", md="3.5rem"),
                        line_height="1.1",
                        letter_spacing="-0.04em",
                        color=TextColor.PRIMARY.value,
                    ),
                    rx.text(
                        "Selección de proyectos personales, cada uno "
                        "me ha servido para aprender algo nuevo ya sea en desarrollo o relacionado con la metodología DevOps.",
                        font_size="1rem",
                        color=TextColor.SECONDARY.value,
                        max_width="680px",
                    ),
                    spacing="4",
                    align="start",
                    max_width="760px",
                ),
                rx.grid(
                    *[
                        project_card(project, index)
                        for index, project in enumerate(PROJECTS)
                    ],
                    columns=rx.breakpoints(initial="1", md="2", lg="3"),
                    spacing="5",
                    width="100%",
                    margin_top="3rem",
                ),
                rx.el.a(
                    rx.hstack(
                        rx.icon("arrow-left", size=16),
                        "Volver al inicio",
                        spacing="2",
                        align="center",
                        padding_top="2%",
                    ),
                    href="/",
                    style={
                        "font_size": "0.85rem",
                        "color": TextColor.SECONDARY.value,
                        "text_decoration": "none",
                        "margin_top": "3rem",
                    },
                    _hover={"color": Color.ACCENT.value},
                ),
                max_width=styles.MAX_WIDTH,
                margin="0 auto",
                padding_x=rx.breakpoints(initial="1.5rem", md="2rem"),
                padding_top=rx.breakpoints(initial="7rem", md="9rem"),
                padding_bottom=rx.breakpoints(initial="4rem", md="6rem"),
                width="100%",
            ),
            footer(),
            position="relative",
            z_index="1",
            width="100%",
        ),
        min_height="100vh",
        background_color=Color.BACKGROUND.value,
        background_image=styles.PAGE_BACKGROUND,
        position="relative",
    )
