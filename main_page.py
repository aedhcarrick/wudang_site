# main_page.py

# imports
import flet as ft
import os
import sys

def HomePage(page: ft.Page):
    page.padding = 0
    page.title = "Wudang Gongfu of New Orleans"

if __name__ == '__main__':
    ft.run(HomePage, view=ft.AppView.WEB_BROWSER, port=8080)

