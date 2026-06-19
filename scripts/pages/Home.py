# Home.py


# imports

import flet as ft
from time import sleep
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
                    value = "",
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
            curve = ft.AnimationCurve.EASE_IN_OUT,
            duration = ft.Duration(seconds=3),
        )
        self.on_animation_end = self.fade_in
        self.on_click = self.new_quote

    def fade_in(self):
        if (self.opacity != 1):
            self.content.controls[0].value = fetch_random_quote()
            self.opacity = 1
            self.update()

    def new_quote(self):
        self.opacity = 0
        self.update()
        

# page content

class Home_Content(ft.Stack):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = [
            Quote(),
        ]
        self.expand = True

    def fade_in(self):
        for control in self.controls:
            control.fade_in()

