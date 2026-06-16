# main_page.py

# imports
import flet as ft
import os
import time
import sys
from pydoc import locate
from pprint import pprint
from scripts.controls import Layout


def WudangWebsite(page: ft.Page):
    page.padding = 0
    page.margin = 0
    page.expand = True

    page.title = "Wudang Gongfu of New Orleans"
    page.fonts = {
            "Chinese": "fonts/MaShanZheng-Regular.ttf",
            "Heading_Bold": "fonts/ProtestRevolution-Regular.ttf"
    }

    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src = "images/Background-Extend.png",
            fit = ft.BoxFit.COVER,
        ),
    )

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    def route_change():
        page.update()

    page.on_route_change = route_change


    def connect():
        page.controls.clear()
        page.add(
            Layout(),
        )
        page.navigate(page.route)

    page.on_connect = connect

    page.route = '/Home'
    connect()


if __name__ == '__main__':
    ft.run(WudangWebsite, view=ft.AppView.WEB_BROWSER, port=8080, assets_dir="assets")

