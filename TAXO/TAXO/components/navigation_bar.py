import flet as ft

def NavigationBar(navigate_to, current_route: str, theme):
    styles = theme.get_styles()
    
    return ft.Container(
        content=ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    tooltip="Volver al inicio",
                    on_click=lambda _: navigate_to("inicio"),
                    visible=current_route != "inicio",
                ),
                ft.Text(
                    "Taxi App",
                    size=24,
                    weight="bold",
                    color=theme.PRIMARY_COLOR,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=10,
        bgcolor=theme.CARD_COLOR,
    )