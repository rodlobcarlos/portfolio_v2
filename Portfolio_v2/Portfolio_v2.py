import reflex as rx

import Portfolio_v2.styles.styles as styles
from Portfolio_v2.components.background import animated_background
from Portfolio_v2.styles.colors import Color
from Portfolio_v2.views.about_me import about_me
from Portfolio_v2.views.career import career
from Portfolio_v2.views.footer import footer
from Portfolio_v2.views.hero import hero
from Portfolio_v2.views.navbar import navbar
from Portfolio_v2.views.projects import projects_page


def index() -> rx.Component:
    return rx.box(
        animated_background(),
        rx.box(
            navbar("home"),
            rx.box(
                hero(),
                about_me(),
                career(),
                width="100%",
            ),
            footer(),
            position="relative",
            z_index="1",
            width="100%",
        ),
        width="100%",
        min_height="100vh",
        background_color=Color.BACKGROUND.value,
        background_image=styles.PAGE_BACKGROUND,
        position="relative",
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style={**styles.BASE_STYLE, **styles.CUSTOM_STYLE},
    head_components=[
        rx.el.link(
            rel="icon",
            type="image/png",
            sizes="any",
            href=rx.asset("c.png"),
        ),
    ],
    # Ocultar reflex badge
    style={
        "a[href*='reflex.dev']": {
            "display": "none !important",
            "visibility": "hidden !important",
            "opacity": "0 !important",
            "pointer_events": "none !important",
        }
    }
)

app.add_page(
    index,
    title="Carlos Rodríguez Lobato — Portfolio",
    description=(
        "Portfolio personal de Carlos Rodríguez Lobato, desarrollador "
        "full-stack y DevOps."
    ),
)
app.add_page(
    projects_page,
    route="/proyectos",
    title="Proyectos — Carlos Rodríguez Lobato",
    description=(
        "Proyectos personales y académicos de Carlos Rodríguez Lobato."
    ),
)
