# utils/theme_manager.py

import flet as ft

def get_theme_mode():
    """
    Obtiene el modo de tema actual de la aplicación (oscuro o claro).
    :return: 'dark' o 'light'
    """
    # Aquí podrías agregar lógica para obtener el modo de tema desde la base de datos o configuración
    return "dark"  # Cambiar a 'light' o 'dark' según la preferencia guardada

def set_theme_mode(page: ft.Page, is_dark: bool):
    """
    Establece el modo de tema en la página.
    :param page: La página de Flet donde se cambiará el tema.
    :param is_dark: Si es True, establece el tema oscuro. Si es False, establece el tema claro.
    """
    if is_dark:
        page.theme_mode = ft.ThemeMode.DARK
    else:
        page.theme_mode = ft.ThemeMode.LIGHT

    # Actualiza la página para reflejar los cambios de tema
    page.update()
