# layout.py

import flet as ft
from scripts.appbar import Appbar


with open('assets/text/HomePageText.md', 'r') as txt:
    readme = txt.read()

class Display(ft.Container):
    def __init__(self):
        super().__init__(
            expand = True,
            padding = 20,
            content = ft.Markdown(
                value = readme,
                selectable = True,
                extension_set = ft.MarkdownExtensionSet.GITHUB_WEB,
                on_tap_link = self.open_link,
            ),
        )

    def open_link(self, e):
        self.page.launch_url(e.data)

class Layout(ft.SafeArea):
    def __init__(self):
        super().__init__(
            expand = True,
            content = ft.Column(
                expand = True,
                controls = [
                    Appbar(),
                    Display(),
                ],
            ),
        )

    def did_mount(self):
        self.content.controls[0].fade_in()

