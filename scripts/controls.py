# controls.py

#   imports

import flet as ft
from pathlib import Path

# get pages

page_dir = Path('./scripts/pages')
pages = [p.stem for p in page_dir.iterdir() if p.is_file()]


# class definitions

class Background(ft.ShaderMask):
    def __init__(self, *args, **kwargs):
        super().__init__(
            blend_mode = ft.BlendMode.DST_IN,
            shader = ft.LinearGradient(
                begin = ft.Alignment.CENTER_LEFT,
                end = ft.Alignment.CENTER_RIGHT,
                colors = [ft.Colors.TRANSPARENT, ft.Colors.BLACK, ft.Colors.TRANSPARENT],
                stops = [0.1, 0.5, 0.9],
            ),
            content = ft.Image(
                src = "images/Main-Background.png",
                height = 2400,
                width = 3600,
                fit = ft.BoxFit.COVER,
                expand = True,
            ),
            *args,
            **kwargs,
        )

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
        self.route_name = f'/{name}'

    def goto(self):
        self.page.route = self.route_name
        self.page.navigate(self.page.route)
        self.parent.show_hide_items()


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
            if self.page.route == item.route_name:
                item.visible = False
            else:
                item.visible = True
        self.update()

    def did_mount(self):
        self.show_hide_items()


class Appbar(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = ft.AppBar(
            title = ft.Text(
                style = ft.TextStyle(
                    color = '#944239',
                    font_family = "Heading_Bold",
                    shadow = ft.BoxShadow(
                        color = ft.Colors.BLACK_26,
                        offset = [5,5],
                    ),
                ),
                theme_style = ft.TextThemeStyle.DISPLAY_LARGE,
                value = "Wudang Gongfu of New Orleans",
            ),
            bgcolor = ft.Colors.TRANSPARENT,
            center_title = False,
            clip_behavior = ft.ClipBehavior.NONE,
            actions = [
                DropdownMenu(),
            ],
        )
        self.elevation = 12
        self.margin = 20
        self.opacity = 0
        self.animate_opacity = ft.Animation(
            curve = ft.AnimationCurve.EASE_IN,
            duration = ft.Duration(seconds=3),
        )
 #       self.on_animation_end = FadeInPageContent

    def fade_in(self):
        self.opacity = 1
        self.update()

    def did_mount(self):
        self.fade_in()


quote = "Motion in stillness...\n   Stillness in motion."

class Quote(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = 0
        self.bottom = 0
        self.content = ft.Text(
            color = '#908E7B',
            expand = 4,
            theme_style = ft.TextThemeStyle.HEADLINE_MEDIUM,
            value = quote,
        )
        self.padding = 20
        self.animate_opacity = ft.Animation(
            curve = ft.AnimationCurve.EASE_IN,
            duration = ft.Duration(seconds=5),
        )

    def fade_in(self):
        self.opacity = 1
        self.update()

    def did_mount(self):
        self.fade_in()
    

class Layout(ft.Stack):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = [
            Background(),
            ft.Column(
                alignment = ft.MainAxisAlignment.START,
                controls = [
                    Appbar(),
                ],
                expand = True,
            ),
            Quote(),
        ]
        self.expand = True
        
