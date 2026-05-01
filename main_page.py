# main_page.py

# imports
import flet as ft
import os
import sys

def run_wudang_site():
    ft.app(
            target = HomePage,
            port = 8888,
            assets_dir = 'assets'
    )

def HomePage(page: ft.Page):
    page.padding = 0
    page.title = "Wudang Gongfu of New Orleans"


if __name__ == '__main__':
    run_wudang_site()

