import flet as ft
from components.navigation_bar import NavigationBar
import sqlite3

def BuscarScreen(page: ft.Page, navigate_to, theme):
    styles = theme.get_styles()
    
    busqueda = ft.TextField(
        label="Buscar por nombre o RUT",
        prefix_icon=ft.icons.SEARCH,
        **styles["input"]
    )
    
    resultados = ft.ListView(
        spacing=10,
        padding=20,
        height=400,
    )
    
    def buscar(_):
        resultados.controls.clear()
        if not busqueda.value:
            return
        
        conn = sqlite3.connect("taxi_app.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT v.*, c.nombre as conductor_nombre
            FROM viajes v
            LEFT JOIN conductores c ON v.conductor_id = c.id
            WHERE v.nombre LIKE ? OR v.rut LIKE ?
        """, (f"%{busqueda.value}%", f"%{busqueda.value}%"))
        viajes = cursor.fetchall()
        conn.close()
        
        for viaje in viajes:
            resultados.controls.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text(viaje[1], size=16, weight="bold"),
                                    ft.Text(f"RUT: {viaje[2]}", size=14),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Text(f"Fecha: {viaje[3]}", size=14),
                            ft.Text(f"Desde: {viaje[4]}", size=14),
                            ft.Text(f"Hasta: {viaje[5]}", size=14),
                            ft.Text(f"Conductor: {viaje[-1] or 'Sin asignar'}", size=14),
                            ft.Text(f"Costo: ${viaje[9]:,.0f}", size=14, weight="bold"),
                        ],
                    ),
                    **styles["card"],
                )
            )
        resultados.update()
    
    busqueda.on_change = buscar
    
    return ft.Container(
        content=ft.Column(
            [
                NavigationBar(navigate_to, "buscar", theme),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Buscar Viajes", style=styles["header"]),
                            busqueda,
                            resultados,
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