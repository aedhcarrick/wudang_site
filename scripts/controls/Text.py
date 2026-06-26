# Text.py


# imports

import flet as ft


# class definitions

class Text(ft.Container):
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = ft.Text(
            style = ft.TextStyle(
                color = '#000',
            ),
            theme_style = ft.TextThemeStyle.BODY_MEDIUM,
            value = text,
        )
        self.expand = True
        

