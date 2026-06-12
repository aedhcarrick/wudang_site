# controls.py

import flet as ft


with open('assets/text/HomePageText.md', 'r') as txt:
    home_page = txt.read()

with open('assets/text/ClassesPageText.md', 'r') as txt:
    classes_page = txt.read()

with open('assets/text/InstructorsPageText.md', 'r') as txt:
    instructors_page = txt.read()

with open('assets/text/ResourcesPageText.md', 'r') as txt:
    resources_page = txt.read()

pages = {
    "Home": home_page,
    "Classes": classes_page,
    "Instructors" : instructors_page,
    "Resources" : resources_page,
}

TextStyle = ft.TextStyle(
    bgcolor = ft.Colors.TRANSPARENT,
    color = ft.Colors.BLACK,
)

MDStyleSheet = ft.MarkdownStyleSheet(
    a_text_style = TextStyle.copy(color=ft.Colors.RED),
    blockquote_decoration = None,
    blockquote_text_style = TextStyle,
    h1_alignment = ft.MainAxisAlignment.START,
    h1_padding = 0,
    h1_text_style = TextStyle.copy(),
    h2_alignment = ft.MainAxisAlignment.START,
    h2_padding = 0,
    h2_text_style = TextStyle.copy(),
    h3_alignment = ft.MainAxisAlignment.START,
    h3_padding = 0,
    h3_text_style = TextStyle.copy(),
    h4_alignment = ft.MainAxisAlignment.START,
    h4_padding = 0,
    h4_text_style = TextStyle.copy(),
    h5_alignment = ft.MainAxisAlignment.START,
    h5_padding = 0,
    h5_text_style = TextStyle.copy(),
    h6_alignment = ft.MainAxisAlignment.START,
    h6_padding = 0,
    h6_text_style = TextStyle.copy(),
    p_text_style = TextStyle.copy(color=ft.Colors.WHITE),
)


class Background(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.expand = True
        self.bgcolor = ft.Colors.TRANSPARENT
        self.content = ft.Image(
            src = "images/Main-Background.png",
            height = 2400,
            width = 3600,
            fit = ft.BoxFit.COVER,
            expand = True,
        )
        self.opacity = 0
        self.animate_opacity = ft.Animation(
            curve = ft.AnimationCurve.EASE_IN,
            duration = ft.Duration(seconds=5),
        )
        self.on_animation_end = FadeInAppbar

    def fade_in(self):
        self.opacity = 1
        self.update()

    def did_mount(self):
        self.fade_in()


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
            items = [DropdownMenuItem(x) for x in pages.keys()],
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
                value = "Wudang Gongfu of New Orleans",
                color = ft.Colors.BLACK,
                font_family = "Heading_Bold",
                theme_style = ft.TextThemeStyle.DISPLAY_LARGE,
            ),
            bgcolor = ft.Colors.TRANSPARENT,
            center_title = True,
            clip_behavior = ft.ClipBehavior.NONE,
            actions = [
                DropdownMenu(),
            ],
        )
        self.opacity = 0
        self.animate_opacity = ft.Animation(
            curve = ft.AnimationCurve.EASE_IN,
            duration = ft.Duration(seconds=5),
        )
        self.on_animation_end = FadeInPageContent

    def fade_in(self):
        self.opacity = 1
        self.update()


class PageContent(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.margin = 10
        self.padding = 20
        self.bgcolor = ft.Colors.BLACK_12
        self.content = ft.Markdown(
            value = home_page,
            selectable = True,
            on_tap_link = self.open_link,
            extension_set = ft.MarkdownExtensionSet.COMMON_MARK,
            md_style_sheet = MDStyleSheet,
        )
        self.border = ft.Border.all(width=2, color=ft.Colors.BLACK)
        self.border_radius = 10
        self.expand = 4
        self.opacity = 0
        self.animate_opacity = ft.Animation(
            curve = ft.AnimationCurve.EASE_IN,
            duration = ft.Duration(seconds=5),
        )

    def fade_in(self):
        self.opacity = 1
        self.update()

    def open_link(self, e):
        self.page.launch_url(e.data)

    def update_content(self):
        content = self.page.route.lstrip("/")
        self.content.value = pages[content]
        self.opacity = 0
        self.update()
        self.fade_in()


class Margin(ft.Container):
    def __init__(self):
        super().__init__(
            margin = 0,
            padding = 0,
            content = ft.Column(
                controls = None,
            ),
            expand = 1,
        )


## references
appbar = ft.Ref[Appbar]()
page_content = ft.Ref[PageContent]()


def FadeInAppbar():
    appbar.current.fade_in()

def FadeInPageContent():
    page_content.current.fade_in()


## Layout

class Layout(ft.Container):
    def __init__(self):
        super().__init__(
            expand = True,
            content = ft.Column(
                alignment = ft.MainAxisAlignment.START,
                controls = [
                    Appbar(ref=appbar),
                    ft.Row(
                        alignment = ft.MainAxisAlignment.CENTER,
                        controls = [
                            Margin(),
                            PageContent(ref=page_content),
                            Margin(),
                        ],
                        tight = False,
                        expand = True,
                    ),
                ],
                expand = True,
            ),
            animate_opacity = ft.Animation(
                curve = ft.AnimationCurve.EASE_IN,
                duration = ft.Duration(seconds=5),
            ),
        )

    def fade_in(self):
        self.opacity = 1
        self.update()

    def did_mount(self):
        self.fade_in()

    def update_content(self):
        self.content.controls[1].controls[1].update_content()


