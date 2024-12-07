import flet as ft
from components.navigation_bar import NavigationBar
import sqlite3
from datetime import datetime, timedelta

def EstadisticasScreen(page: ft.Page, navigate_to, theme):
    styles = theme.get_styles()
    
    def obtener_estadisticas():
        conn = sqlite3.connect("taxi_app.db")
        cursor = conn.cursor()
        
        # Estadísticas generales
        cursor.execute("""
            SELECT 
                COUNT(*) as total_viajes,
                SUM(kilometraje) as total_km,
                SUM(costo_total) as total_ingresos,
                AVG(costo_total) as promedio_viaje
            FROM viajes
        """)
        stats = cursor.fetchone()
        
        # Viajes por conductor
        cursor.execute("""
            SELECT 
                c.nombre,
                COUNT(*) as total_viajes,
                SUM(v.kilometraje) as total_km,
                SUM(v.costo_total) as total_ingresos
            FROM viajes v
            JOIN conductores c ON v.conductor_id = c.id
            GROUP BY c.id
        """)
        conductores_stats = cursor.fetchall()
        
        conn.close()
        return stats, conductores_stats
    
    stats, conductores_stats = obtener_estadisticas()
    
    return ft.Container(
        content=ft.Column(
            [
                NavigationBar(navigate_to, "estadisticas", theme),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Estadísticas", style=styles["header"]),
                            ft.Row(
                                [
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Text("Total Viajes", size=16),
                                                ft.Text(str(stats[0]), size=24, weight="bold"),
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        **styles["card"],
                                        expand=True,
                                    ),
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Text("Total Kilómetros", size=16),
                                                ft.Text(f"{stats[1]:.1f} km", size=24, weight="bold"),
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        **styles["card"],
                                        expand=True,
                                    ),
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Text("Total Ingresos", size=16),
                                                ft.Text(f"${stats[2]:,.0f}", size=24, weight="bold"),
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        **styles["card"],
                                        expand=True,
                                    ),
                                ],
                                spacing=10,
                            ),
                            ft.Divider(),
                            ft.Text("Estadísticas por Conductor", style=styles["subheader"]),
                            ft.ListView(
                                controls=[
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Text(conductor[0], size=18, weight="bold"),
                                                ft.Row(
                                                    [
                                                        ft.Text(f"Viajes: {conductor[1]}"),
                                                        ft.Text(f"Km: {conductor[2]:.1f}"),
                                                        ft.Text(f"${conductor[3]:,.0f}"),
                                                    ],
                                                    spacing=20,
                                                ),
                                            ],
                                        ),
                                        **styles["card"],
                                    )
                                    for conductor in conductores_stats
                                ],
                                spacing=10,
                                height=300,
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