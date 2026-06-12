# main_page.py

# imports
import flet as ft
import os
import time
import sys
from pydoc import locate
from pprint import pprint
from scripts.controls import Background, Layout


def WudangWebsite(page: ft.Page):
    page.padding = 0
    page.margin = 0
    page.title = "Wudang Gongfu of New Orleans"
    page.fonts = {
            "Heading_Bold": "fonts/MaShanZheng-Regular.ttf"
    }
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.RED)
    page.bgcolor = ft.Colors.TRANSPARENT
    decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src = "images/Background-Extend.png",
            fit = ft.BoxFit.COVER,
        ),
    )

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Stack(
            expand = True,
            controls = [
                Background(),
                Layout(),
            ],
        )
    )

    def route_change():
        page.controls[0].controls[1].update_content()

    page.on_route_change = route_change
    page.route = '/Home'
    page.navigate(page.route)



if __name__ == '__main__':
    ft.run(WudangWebsite, view=ft.AppView.WEB_BROWSER, port=8080, assets_dir="assets")

