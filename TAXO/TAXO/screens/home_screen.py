import flet as ft
from components.theme_switch import ThemeSwitch
from styles import AppTheme

def HomeScreen(page: ft.Page, navigate_to, theme: AppTheme):
    styles = theme.get_styles()
    
    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            "Taxi App",
                            size=40,
                            weight="bold",
                            color=theme.PRIMARY_COLOR,
                            text_align="center",
                            expand=True,
                        ),
                        ThemeSwitch(page),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.ElevatedButton(
                                "Registrar Viaje",
                                style=styles["button"],
                                on_click=lambda _: navigate_to("registro"),
                                width=300,
                            ),
                            ft.ElevatedButton(
                                "Gestionar Conductores",
                                style=styles["button"],
                                on_click=lambda _: navigate_to("conductores"),
                                width=300,
                            ),
                            ft.ElevatedButton(
                                "Gestionar Vehículos",
                                style=styles["button"],
                                on_click=lambda _: navigate_to("vehiculos"),
                                width=300,
                            ),
                            ft.ElevatedButton(
                                "Configurar Tarifas",
                                style=styles["button"],
                                on_click=lambda _: navigate_to("configuracion"),
                                width=300,
                            ),
                            ft.ElevatedButton(
                                "Buscar Pasajeros",
                                style=styles["button"],
                                on_click=lambda _: navigate_to("buscar"),
                                width=300,
                            ),
                            ft.ElevatedButton(
                                "Estadísticas",
                                style=styles["button"],
                                on_click=lambda _: navigate_to("estadisticas"),
                                width=300,
                            ),
                        ],
                        spacing=20,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    **styles["card"],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.all(20),
        bgcolor=theme.BACKGROUND_COLOR,
        expand=True,
    )