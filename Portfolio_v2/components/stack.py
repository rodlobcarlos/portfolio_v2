import reflex as rx
import Portfolio_v2.styles.styles as styles
from Portfolio_v2.styles.colors import TextColor, Color

def stack():
    return rx.vstack(
        rx.hstack(
            rx.text(
                "Este es mi",
                rx.el.span(" stack ", style={"color": "#7bff00"}),
                "tecnológico hasta la fecha dividido en ",
                rx.el.span("desarrollo", style={"color": "#3589ff"}),
                " y",
                rx.el.span(" DevOps", style={"color": "#d9ff00"}),
                size="7",
                font_style="italic"
            ),
        ),
        rx.box(
            rx.heading("Desarrollo", size="6", align="center", margin_bottom="5%"),
            rx.hstack(
                rx.image(src="angular.png", alt="angular", border_radius="15%", width="120px"),
                rx.image(src="java.png", alt="java", border_radius="15%", width="120px"),
                rx.image(src="mongo.png", alt="mongo", border_radius="15%", width="120px"),
                rx.image(src="mysql.png", alt="mysql", border_radius="15%", width="120px"),
                rx.image(src="node.png", alt="node", border_radius="15%", width="120px"),
                rx.image(src="springboot.png", alt="springboot", border_radius="15%", width="120px"),
                rx.image(src="python.png", alt="python", border_radius="15%", width="120px"),
                
                width="100%",        
                justify="center",    
                wrap="wrap",        
                spacing="5",
            ),
            position="relative",
            width="900px",
            margin_top="5%",
        ),

        rx.box(
            rx.heading("DevOps", size="6", align="center", margin_bottom="5%"),
            rx.hstack(
                rx.image(src="azure.png", alt="azure", border_radius="15%", width="120px"),
                rx.image(src="azureDevOps.png", alt="azureDevops", border_radius="15%", width="120px"),
                rx.image(src="codeql.jpeg", alt="codeql", border_radius="15%", width="120px"),
                rx.image(src="python.png", alt="python", border_radius="15%", width="120px"),
                
                width="100%",        
                justify="center",    
                wrap="wrap",        
                spacing="5",
            ),
            position="relative",
            width="900px",
            margin_top="5%",
        ),
        width="100%",
        align="center",
        margin_top="-15%",
        height= "100vh",
    ),