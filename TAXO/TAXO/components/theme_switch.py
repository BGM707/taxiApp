# components/theme_switch.py

import flet as ft
from utils.theme_manager import toggle_theme_mode

class ThemeSwitch(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        # Comenzar con el modo de tema actual
        self.theme_switch = ft.Switch(
            value=self.page.theme_mode == ft.ThemeMode.DARK, 
            on_change=self.toggle_theme
        )

    def toggle_theme(self, e):
        # Cambiar el tema según el valor del interruptor
        toggle_theme_mode(self.page, e.control.value)  # Cambiar el tema a oscuro o claro

    def build(self):
        # Retornar un Row con el interruptor
        return ft.Row([self.theme_switch])
