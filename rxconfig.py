import reflex as rx

config = rx.Config(
    app_name="Portfolio_v2",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                accent_color="teal",
                radius="none",
                has_background=True,
            )
        ),
    ],
)
