# home.py

import flet as ft
from scripts.background import Background
from scripts.layout import Layout


class Home(ft.View):
    def __init__(self):
        super().__init__(
            route = "/home",
            padding = 0,
            expand = True,
            bgcolor = ft.Colors.TRANSPARENT,
            decoration = ft.BoxDecoration(
                image = ft.DecorationImage(
                    src = "images/Background-Extend.png",
                    fit = ft.BoxFit.COVER,
                ),
            ),
            controls = [
                ft.Stack(
                    expand = True,
                    controls = [
                        Background(),
                        Layout(),
                    ],
                ),
            ],
        )


    def did_mount(self):
        self.controls[0].controls[0].fade_in()

