import flet as ft

class AppTheme:
    def __init__(self, is_dark: bool = False):
        self.is_dark = is_dark
        self.set_colors()

    def set_colors(self):
        if self.is_dark:
            self.PRIMARY_COLOR = "#2196F3"
            self.SECONDARY_COLOR = "#1976D2"
            self.BACKGROUND_COLOR = "#121212"
            self.CARD_COLOR = "#1E1E1E"
            self.TEXT_COLOR = "#FFFFFF"
            self.ERROR_COLOR = "#CF6679"
        else:
            self.PRIMARY_COLOR = "#1565C0"
            self.SECONDARY_COLOR = "#1976D2"
            self.BACKGROUND_COLOR = "#F5F5F5"
            self.CARD_COLOR = "#FFFFFF"
            self.TEXT_COLOR = "#212121"
            self.ERROR_COLOR = "#D32F2F"

    def get_theme(self) -> ft.Theme:
        return ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=self.PRIMARY_COLOR,
                secondary=self.SECONDARY_COLOR,
            )
        )

    def get_styles(self):
        return {
            "header": ft.TextStyle(
                size=30,
                weight=ft.FontWeight.BOLD,
                color=self.TEXT_COLOR,
            ),
            "subheader": ft.TextStyle(
                size=20,
                weight=ft.FontWeight.W_400,
                color=self.TEXT_COLOR,
            ),
            "button": ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: self.CARD_COLOR,
                    ft.MaterialState.HOVERED: self.PRIMARY_COLOR,
                },
                bgcolor={
                    ft.MaterialState.DEFAULT: self.PRIMARY_COLOR,
                    ft.MaterialState.HOVERED: self.SECONDARY_COLOR,
                },
                padding=20,
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
            "card": {
                "padding": ft.padding.all(20),
                "bgcolor": self.CARD_COLOR,
                "border_radius": 10,
                "shadow": ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.colors.with_opacity(0.2, "000000"),
                ),
            },
            "input": {
                "cursor_height": 20,
                "content_padding": 10,
                "border_radius": 8,
                "focused_border_color": self.PRIMARY_COLOR,
                "border_color": self.SECONDARY_COLOR,
            }
        }