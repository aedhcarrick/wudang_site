# Appbar.py


# imports

import flet as ft
from pathlib import Path


# get pages

page_dir = Path('./scripts/pages')
pages = [p.stem for p in page_dir.iterdir() if p.is_file()]


# class definitions

class DropdownMenuItem(ft.PopupMenuItem):
    def __init__(self, name):
        super().__init__(
            content = ft.Text(
                color = ft.Colors.BLACK,
                value = name,
                ),
            on_click = self.goto,
            visible = False
        )
        self.route_name = f'/{name.lower()}'

    def goto(self):
        self.page.route = self.route_name
        self.page.navigate(self.page.route)


class DropdownMenu(ft.PopupMenuButton):
    def __init__(self):
        super().__init__(
            items = [DropdownMenuItem(p) for p in pages],
            bgcolor = ft.Colors.WHITE_24,
            elevation = 12,
            icon_color = ft.Colors.BLACK,
            tooltip = ft.Tooltip(
                bgcolor = ft.Colors.WHITE_24,
                message = "MENU",
            ),
            menu_position = ft.PopupMenuPosition.UNDER,
            shape = ft.RoundedRectangleBorder(radius=10),
        )

    def show_hide_items(self):
        for item in self.items:
            if ((item.route_name == '/home') and (self.page.route == '/')):
                item.visible = False
            elif self.page.route == item.route_name:
                item.visible = False
            else:
                item.visible = True
        self.update()

    def did_mount(self):
        self.show_hide_items()

    def hide_menu(self):
        self.visible = False
        self.update()

    def show_menu(self):
        self.visible = True
        self.update()


class Appbar(ft.AppBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = ft.Container(
            content = ft.Text(
                style = ft.TextStyle(
                    color = '#000',  ##'#944239',
                    font_family = "Heading_Bold",
                    shadow = ft.BoxShadow(
                        color = ft.Colors.BLACK_26,
                        offset = [5,5],
                    ),
                ),
                theme_style = ft.TextThemeStyle.DISPLAY_LARGE,
                value = "Wudang Gongfu of New Orleans",
            ),
            margin = 20,
            opacity = 0,
            animate_opacity = ft.Animation(
                curve = ft.AnimationCurve.EASE_IN,
                duration = ft.Duration(seconds=5),
            )
        )
        self.bgcolor = ft.Colors.TRANSPARENT
        self.center_title = False
        self.force_material_transparency = True
        self.clip_behavior = ft.ClipBehavior.NONE
        self.actions = [
            DropdownMenu(),
        ]
    
    def fade_in(self):
        self.title.opacity = 1
        self.title.update()

    def did_mount(self):
        self.fade_in()

    def show_hide_items(self):
        self.actions[0].show_hide_items()

    def hide_menu(self):
        self.actions[0].hide_menu()

    def show_menu(self):
        self.actions[0].show_menu()


