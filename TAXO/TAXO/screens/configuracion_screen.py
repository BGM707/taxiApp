import flet as ft
from components.navigation_bar import NavigationBar
import sqlite3

def ConfiguracionScreen(page: ft.Page, navigate_to, theme):
    styles = theme.get_styles()
    
    def cargar_tarifas():
        conn = sqlite3.connect("taxi_app.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarifas WHERE id = 1")
        tarifas = cursor.fetchone()
        conn.close()
        return tarifas
    
    tarifas = cargar_tarifas()
    
    tarifa_km = ft.TextField(
        label="Tarifa por Kilómetro",
        value=str(tarifas[1]),
        **styles["input"]
    )
    tarifa_hora = ft.TextField(
        label="Tarifa por Hora",
        value=str(tarifas[2]),
        **styles["input"]
    )
    tarifa_manejo = ft.TextField(
        label="Tarifa de Manejo",
        value=str(tarifas[3]),
        **styles["input"]
    )
    extra_ida_vuelta = ft.TextField(
        label="Extra por Ida y Vuelta",
        value=str(tarifas[4]),
        **styles["input"]
    )
    
    def guardar_tarifas(_):
        try:
            conn = sqlite3.connect("taxi_app.db")
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE tarifas 
                SET tarifa_km = ?, tarifa_hora = ?, tarifa_manejo = ?, extra_ida_vuelta = ? 
                WHERE id = 1
                """,
                (
                    float(tarifa_km.value),
                    float(tarifa_hora.value),
                    float(tarifa_manejo.value),
                    float(extra_ida_vuelta.value)
                )
            )
            conn.commit()
            conn.close()
            page.show_snack_bar(ft.SnackBar(content=ft.Text("Tarifas actualizadas")))
        except Exception as e:
            page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Error: {str(e)}")))
    
    return ft.Container(
        content=ft.Column(
            [
                NavigationBar(navigate_to, "configuracion", theme),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Configurar Tarifas", style=styles["header"]),
                            tarifa_km,
                            tarifa_hora,
                            tarifa_manejo,
                            extra_ida_vuelta,
                            ft.ElevatedButton(
                                "Guardar Cambios",
                                style=styles["button"],
                                on_click=guardar_tarifas,
                            ),
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