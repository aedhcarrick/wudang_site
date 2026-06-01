# main_page.py

# imports
import flet as ft
import os
import time
import sys
from scripts.home import Home
from assets.theme.colors import *


def WudangWebsite(page: ft.Page):
    page.padding = 0
    page.margin = 0
    page.title = "Wudang Gongfu of New Orleans"
    page.fonts = {
            "Heading_Bold": "theme/fonts/MaShanZheng-Regular.ttf"
    }
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLACK
    
    def route_change():
        page.views.clear()
        page.route = "/home"
        print("going home")
        page.views.append(Home())
        page.update()

    page.on_route_change = route_change

    route_change()
#    page.navigate("/home")
    

if __name__ == '__main__':
    ft.run(WudangWebsite, view=ft.AppView.WEB_BROWSER, port=8080, assets_dir="assets")

