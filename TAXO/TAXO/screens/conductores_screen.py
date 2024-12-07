import flet as ft
import sqlite3
from components.navigation_bar import NavigationBar

def ConductoresScreen(page: ft.Page, navigate_to, theme):
    styles = theme.get_styles()
    
    def cargar_conductores():
        conn = sqlite3.connect("taxi_app.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, rut, foto FROM conductores")
        conductores = cursor.fetchall()
        conn.close()
        return conductores
    
    def agregar_conductor(_):
        file_picker = ft.FilePicker(
            on_result=lambda e: guardar_foto(e.files[0] if e.files else None)
        )
        page.overlay.append(file_picker)
        page.update()
    
    def guardar_foto(file):
        if file:
            # Implementar lógica para guardar la foto
            pass
    
    conductores_list = ft.GridView(
        expand=True,
        runs_count=3,
        max_extent=200,
        spacing=10,
        run_spacing=10,
        child_aspect_ratio=1,
    )
    
    for conductor in cargar_conductores():
        conductores_list.controls.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.CircleAvatar(
                            content=ft.Icon(ft.icons.PERSON),
                            radius=30,
                            bgcolor=theme.PRIMARY_COLOR,
                        ),
                        ft.Text(conductor[1], size=16, weight="bold"),
                        ft.Text(conductor[2], size=14),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                **styles["card"],
            )
        )
    
    return ft.Container(
        content=ft.Column(
            [
                NavigationBar(navigate_to, "conductores", theme),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Gestionar Conductores", style=styles["header"]),
                                    ft.ElevatedButton(
                                        "Agregar Conductor",
                                        style=styles["button"],
                                        on_click=agregar_conductor,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            conductores_list,
                        ],
                        spacing=20,
                    ),
                    **styles["card"],
                ),
            ],
            spacing=20,
        ),
        padding=20,
        bgcolor=theme.BACKGROUND_COLOR,
        expand=True,
    )