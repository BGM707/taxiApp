import flet as ft
from components.navigation_bar import NavigationBar

def RegistroScreen(page: ft.Page, navigate_to, theme):
    styles = theme.get_styles()
    
    nombre = ft.TextField(label="Nombre del Pasajero", **styles["input"])
    rut = ft.TextField(label="RUT", **styles["input"])
    fecha = ft.TextField(label="Fecha", **styles["input"])
    direccion_partida = ft.TextField(label="Dirección de Partida", **styles["input"])
    direccion_destino = ft.TextField(label="Dirección de Destino", **styles["input"])
    kilometraje = ft.TextField(label="Kilometraje", **styles["input"])
    tiempo = ft.TextField(label="Tiempo (horas)", **styles["input"])
    ida_vuelta = ft.Checkbox(label="Ida y Vuelta")
    
    def guardar_viaje(_):
        # Implementar lógica para guardar el viaje
        navigate_to("inicio")
    
    return ft.Container(
        content=ft.Column(
            [
                NavigationBar(navigate_to, "registro", theme),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Registrar Viaje", style=styles["header"]),
                            nombre,
                            rut,
                            fecha,
                            direccion_partida,
                            direccion_destino,
                            kilometraje,
                            tiempo,
                            ida_vuelta,
                            ft.ElevatedButton(
                                "Guardar Viaje",
                                style=styles["button"],
                                on_click=guardar_viaje,
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