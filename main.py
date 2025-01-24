import flet as ft

def main(page: ft.Page):
    page.title = "Hello App"
    page.add(ft.Text(value="Hello, Android!", size=30))

ft.app(target=main)