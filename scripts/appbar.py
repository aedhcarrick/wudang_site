# appbar.py

import time
import flet as ft
from assets.theme.colors import *

pages = ["Home", "Classes", "Instructors", "Resources"]
current_page = "Home"

def GetPopupMenuItem(name):
    item = ft.PopupMenuItem(
            content = ft.Text(
                value = name,
                color = text_color,
            ),
    )
    return item

class DropdownMenu(ft.PopupMenuButton):
    def __init__(self):
        super().__init__(
            items = [GetPopupMenuItem(x) for x in pages if x != current_page],
            bgcolor = bg_color_2,
            elevation = 12,
            icon_color = text_color,
            tooltip = ft.Tooltip(
                bgcolor = bg_color_2,
                message = "MENU",
            ),
            menu_position = ft.PopupMenuPosition.UNDER,
            shape = ft.RoundedRectangleBorder(radius=10),
        )

class Appbar(ft.Container):
    def __init__(self):
        super().__init__(
            content = ft.AppBar(
                title = ft.Text(
                    value = "Wudang Gongfu of New Orleans",
                    color = text_color,
                    font_family = "Heading_Bold",
                    theme_style = ft.TextThemeStyle.DISPLAY_LARGE,
                    ),
                center_title = True,
                bgcolor = bg_color_1,
                clip_behavior = ft.ClipBehavior.NONE,
                actions = [
                    DropdownMenu(),
                ],
            ),
            opacity = 0,
            animate_opacity = ft.Animation(
                curve = ft.AnimationCurve.EASE_IN,
                duration = ft.Duration(seconds=15),
            ),
        )

    def fade_in(self):
        time.sleep(3)
        self.opacity = 1
        self.update()




