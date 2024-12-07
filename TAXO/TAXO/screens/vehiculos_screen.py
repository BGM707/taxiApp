import flet as ft
from components.navigation_bar import NavigationBar
import sqlite3

def VehiculosScreen(page: ft.Page, navigate_to, theme):
    styles = theme.get_styles()
    
    def cargar_vehiculos():
        conn = sqlite3.connect("taxi_app.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT v.*, c.nombre as conductor_nombre 
            FROM vehiculos v 
            LEFT JOIN conductores c ON v.conductor_id = c.id
        """)
        vehiculos = cursor.fetchall()
        conn.close()
        return vehiculos
    
    def agregar_vehiculo(_):
        # Implementar diálogo para agregar vehículo
        pass
    
    vehiculos_list = ft.GridView(
        expand=True,
        runs_count=3,
        max_extent=300,
        spacing=10,
        run_spacing=10,
        child_aspect_ratio=1.5,
    )
    
    for vehiculo in cargar_vehiculos():
        vehiculos_list.controls.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.icons.DIRECTIONS_CAR, size=40, color=theme.PRIMARY_COLOR),
                        ft.Text(f"{vehiculo[1]} {vehiculo[2]}", size=16, weight="bold"),
                        ft.Text(f"Patente: {vehiculo[6]}", size=14),
                        ft.Text(f"Conductor: {vehiculo[-1] or 'Sin asignar'}", size=14),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                **styles["card"],
            )
        )
    
    return ft.Container(
        content=ft.Column(
            [
                NavigationBar(navigate_to, "vehiculos", theme),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Gestionar Vehículos", style=styles["header"]),
                                    ft.ElevatedButton(
                                        "Agregar Vehículo",
                                        style=styles["button"],
                                        on_click=agregar_vehiculo,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            vehiculos_list,
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