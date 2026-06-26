# Image.py


# imports

import flet as ft


# class definitions

class Image(ft.Container):
    def __init__(self, src, link=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = ft.Image(
            src = src,
            width = 400,
            fit = ft.BoxFit.COVER,
            expand = True,
        )
        self.link = link
        if (self.link != None):
            self.on_click = self.gotolink

    async def gotolink(self):
        await ft.UrlLauncher().launch_url(self.link)

