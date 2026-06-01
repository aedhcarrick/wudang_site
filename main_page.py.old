# main_page.py

# imports
import flet as ft
import os
import time
import sys


bg_color_1 = ft.Colors.TRANSPARENT
bg_color_2 = ft.Colors.WHITE_38
text_color = ft.Colors.BLACK

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


def HomePage(page: ft.Page):
    page.padding = 0
    page.title = "Wudang Gongfu of New Orleans"
    page.fonts = {
            "Heading_Bold": "fonts/MaShanZheng-Regular.ttf"
    }
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = bg_color_1
    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src = "images/Background-Extend.png",
            fit = ft.BoxFit.COVER,
        ),
    )

    dropdown_menu = ft.PopupMenuButton(
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

    def appbar_fadein(e):
        time.sleep(3)
        appbar.opacity = 1
        appbar.update()

    def background_fadein(e):
        time.sleep(3)
        background.opacity = 1
        background.update()

    page.on_connect = background_fadein

    page.add(
        ft.SafeArea(
            content = ft.Stack(
                alignment = ft.Alignment.TOP_CENTER,
                expand = True,
                controls = [
                    background := ft.Container(
                        bgcolor = bg_color_1,
                        content = ft.Image(
                            src = "images/Main-Background.png",
                            height = 800,
                            width = 1200,
                            fit = ft.BoxFit.COVER,
                            expand = True,
                        ),
                        expand = True,
                        opacity = 0,
                        animate_opacity = ft.Animation(
                            curve = ft.AnimationCurve.EASE_IN,
                            duration = ft.Duration(seconds=5),
                        ),
                        on_animation_end = appbar_fadein,
                    ),
                    appbar := ft.Container(
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
                                dropdown_menu,
                            ],
                        ),
                        opacity = 0,
                        animate_opacity = ft.Animation(
                            curve = ft.AnimationCurve.EASE_IN,
                            duration = ft.Duration(seconds=5),
                        ),
                    ),
                ],
            ),
        )
    )
    page.update()

if __name__ == '__main__':
    ft.run(HomePage, view=ft.AppView.WEB_BROWSER, port=8080, assets_dir="assets")

