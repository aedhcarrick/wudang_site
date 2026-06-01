# background.py

import flet as ft
import time
from assets.theme.colors import *


class Background(ft.Container):
    def __init__(self):
        super().__init__(
            expand = True,
            bgcolor = ft.Colors.TRANSPARENT,
            content = ft.Image(
                src = "images/Main-Background.png",
                height = 2400,
                width = 3600,
                fit = ft.BoxFit.COVER,
                expand = True,
            ),
            opacity = 0,
            animate_opacity = ft.Animation(
                curve = ft.AnimationCurve.EASE_IN,
                duration = ft.Duration(seconds=10),
            )
        )

    def fade_in(self):
        time.sleep(2)
        self.opacity = 1
        self.update()

    
