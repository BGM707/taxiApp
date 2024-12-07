import flet as ft
import sqlite3

def get_theme_mode():
    conn = sqlite3.connect("taxi_app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT theme_mode FROM settings WHERE id = 1")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 'light'

def toggle_theme_mode(page: ft.Page):
    current_mode = get_theme_mode()
    new_mode = 'dark' if current_mode == 'light' else 'light'
    
    conn = sqlite3.connect("taxi_app.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE settings SET theme_mode = ? WHERE id = 1", (new_mode,))
    conn.commit()
    conn.close()
    
    page.theme_mode = ft.ThemeMode.DARK if new_mode == 'dark' else ft.ThemeMode.LIGHT
    page.update()