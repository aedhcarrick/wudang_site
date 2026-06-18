# Home.py


# imports

import flet as ft
from scripts.quotes import fetch_random_quote


# class definitions

class Quote(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = 0
        self.bottom = 0
        self.width = 400
        self.content = ft.Column(
            alignment = ft.MainAxisAlignment.END,
            horizontal_alignment = ft.CrossAxisAlignment.END,
            controls = [
                ft.Text(
                    color = '#908E7B',
                    theme_style = ft.TextThemeStyle.HEADLINE_MEDIUM,
                    value = fetch_random_quote(),
                    expand = True,
                ),
                ft.Text(
                    color = "#000",
                    theme_style = ft.TextThemeStyle.HEADLINE_SMALL,
                    value = "-- Zuangzi",
                    expand = True,
                ),
            ],
            expand = True,
        )
        self.expand = True
        self.padding = 20
        self.opacity = 0
        self.animate_opacity = ft.Animation(
            curve = ft.AnimationCurve.EASE_IN,
            duration = ft.Duration(seconds=5),
        )

    def fade_in(self):
        self.opacity = 1
        self.update()

    def fade_out(self):
        self.opacity = 0
        self.update()

    def did_mount(self):
        self.fade_in()

    def new_quote(self):
        self.content.controls[0].value = fetch_random_quote()
        self.update()


# page content

class Home_Content(ft.Stack):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = [
            Quote(),
        ]
        self.expand = True


