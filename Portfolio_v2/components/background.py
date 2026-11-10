import reflex as rx


def animated_background() -> rx.Component:
    """Fondo decorativo de puntos que se desplazan en diagonal."""
    return rx.box(
        rx.box(class_name="dot-layer dot-layer--far"),
        rx.box(class_name="dot-layer dot-layer--near"),
        class_name="dot-background",
        aria_hidden="true",
    )
