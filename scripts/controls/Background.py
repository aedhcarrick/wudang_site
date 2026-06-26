# Background.py


# imports

import flet as ft


# class definitions

class Background(ft.ShaderMask):
    def __init__(self, *args, **kwargs):
        super().__init__(
            blend_mode = ft.BlendMode.DST_IN,
            shader = ft.RadialGradient(
                center = ft.Alignment.CENTER,
                radius = 1.0,
                colors = [ft.Colors.BLACK, ft.Colors.TRANSPARENT],
                stops = [0.5, 0.75],
            ),
            content = ft.Container(
                padding = 0,
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
                    duration = ft.Duration(seconds=3),
                ),
                expand = True,
            ),
            *args,
            **kwargs,
        )

    def fade_in(self):
        self.content.opacity = 0.5
        self.content.update()

