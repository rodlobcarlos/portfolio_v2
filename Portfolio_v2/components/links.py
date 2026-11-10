import reflex as rx

import Portfolio_v2.styles.styles as styles
from Portfolio_v2.styles.colors import Color, TextColor


def action_link(
    label: str,
    href: str,
    primary: bool = True,
    new_tab: bool = False,
    icon: str | None = None,
    download: str | None = None,
    compact: bool = False,
) -> rx.Component:
    """Enlace con apariencia de botón, sin depender de estado ni backend."""

    style = dict(styles.BUTTON_PRIMARY if primary else styles.BUTTON_SECONDARY)
    hover = dict(
        styles.BUTTON_PRIMARY_HOVER if primary else styles.BUTTON_SECONDARY_HOVER
    )
    if compact:
        style.update({"padding": "0.45rem 0.7rem", "font_size": "0.8rem"})

    children: list[rx.Component] = [rx.text(label)]
    if icon:
        children.append(rx.icon(icon, size=15))

    # `rx.download` descarga en cliente sin navegar. Usar un botón evita que el
    # router intercepte el clic y abra el PDF en lugar de descargarlo.
    if download:
        return rx.el.button(
            *children,
            type="button",
            on_click=rx.download(url=href, filename=download),
            style={**style, "font_family": "inherit"},
            _hover=hover,
        )

    return rx.el.a(
        *children,
        href=href,
        target="_blank" if new_tab else "_self",
        rel="noopener noreferrer" if new_tab else None,
        style=style,
        _hover=hover,
    )


def nav_link(
    label: str,
    href: str,
    active: bool = False,
    new_tab: bool = False,
) -> rx.Component:
    return rx.el.a(
        label,
        href=href,
        target="_blank" if new_tab else "_self",
        rel="noopener noreferrer" if new_tab else None,
        style={
            "font_size": "0.85rem",
            "font_weight": "600" if active else "400",
            "color": Color.ACCENT.value
            if active
            else TextColor.SECONDARY.value,
            "padding": "0.35rem 0",
            "border_bottom": (
                f"1px solid {Color.ACCENT.value}"
                if active
                else "1px solid transparent"
            ),
            "transition": "color 0.2s ease, border-color 0.2s ease",
        },
        _hover={
            "color": Color.ACCENT_2.value,
            "border_bottom_color": Color.ACCENT_BORDER.value,
        },
    )


def nav_links(current_page: str = "home") -> rx.Component:
    is_projects = current_page == "projects"

    return rx.hstack(
        nav_link(
            "Inicio",
            "/#inicio" if is_projects else "#inicio",
            active=not is_projects,
        ),
        nav_link(
            "Sobre mí",
            "/#sobre-mi" if is_projects else "#sobre-mi",
        ),
        nav_link(
            "Trayectoria",
            "/#trayectoria" if is_projects else "#trayectoria",
        ),
        nav_link(
            "Proyectos",
            "/proyectos",
            active=is_projects,
            new_tab=not is_projects,
        ),
        spacing=rx.breakpoints(initial="3", md="6"),
        align="center",
        wrap="wrap",
    )
