# main.py

import flet as ft
from database import create_database
from screens.home_screen import HomeScreen
from screens.registro_screen import RegistroScreen
from screens.conductores_screen import ConductoresScreen
from screens.vehiculos_screen import VehiculosScreen
from screens.configuracion_screen import ConfiguracionScreen
from screens.estadisticas_screen import EstadisticasScreen
from screens.buscar_screen import BuscarScreen
from components.theme_manager import get_theme_mode, set_theme_mode
from styles import AppTheme
from components.theme_switch import ThemeSwitch  # Importar el interruptor de tema

def main(page: ft.Page):
    # Inicializar base de datos
    create_database()

    # Configurar el tema inicial
    theme_mode = get_theme_mode()  # Obtener el tema desde alguna fuente (ej. base de datos o archivo de configuración)
    theme = AppTheme(is_dark=theme_mode == 'dark')  # Crear el objeto de tema de la aplicación

    # Configurar la página
    page.title = "Taxi App"
    set_theme_mode(page, theme_mode == 'dark')  # Establecer el tema según el modo
    page.bgcolor = theme.BACKGROUND_COLOR
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.window_width = 1000
    page.window_height = 800
    page.window_resizable = True
    page.window_maximizable = True
    page.theme = theme.get_theme()  # Aplicar el tema

    # Función de navegación
    def navigate_to(route_name):
        page.controls.clear()  # Limpiar la pantalla
        routes = {
            "inicio": lambda: HomeScreen(page, navigate_to, theme),
            "registro": lambda: RegistroScreen(page, navigate_to, theme),
            "conductores": lambda: ConductoresScreen(page, navigate_to, theme),
            "vehiculos": lambda: VehiculosScreen(page, navigate_to, theme),
            "configuracion": lambda: ConfiguracionScreen(page, navigate_to, theme),
            "estadisticas": lambda: EstadisticasScreen(page, navigate_to, theme),
            "buscar": lambda: BuscarScreen(page, navigate_to, theme),
        }
        if route_name in routes:
            page.controls.append(routes[route_name]())
        page.update()

    # Mostrar la pantalla inicial
    navigate_to("inicio")

    # Agregar el interruptor de tema
    page.add(ThemeSwitch(page))

if __name__ == "__main__":
    ft.app(target=main)
