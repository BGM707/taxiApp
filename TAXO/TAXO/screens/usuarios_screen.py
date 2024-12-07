import flet as ft

class UsuariosScreen:
    def __init__(self, page, navigate_to, theme):
        self.page = page
        self.navigate_to = navigate_to
        self.theme = theme
        self.build()

    def build(self):
        self.page.add(
            ft.Text("Pantalla de Usuarios", style="headlineLarge"),
            ft.Text("Aquí se gestionarán los usuarios de la aplicación.")
        )
        # Botón de navegación
        self.page.add(ft.ElevatedButton("Volver", on_click=lambda e: self.navigate_to("inicio")))
