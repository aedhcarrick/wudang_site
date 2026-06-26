# main_page.py


# imports
import flet as ft
from pydoc import locate
from scripts.controls.Appbar import Appbar
from scripts.controls.Background import Background


# function definitions

def get_view(route):
    route_name = '/'
    if (route == route_name):
        route = '/home'
    view_name = route.lstrip('/').capitalize()
    try:
        view = locate(f'scripts.pages.{view_name}.{view_name}_Content')
        assert(view.__name__ == f'{view_name}_Content')
    except Exception as e:
        print(f'Module {view_name} not found. Error: {e}')
        view = None
    if (route == '/home'):
        route_name = '/'
    else:
        route_name = route
    return route_name, view


# class definitions

class Layout(ft.Stack):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = [
            Background(),
            ft.Column(
                alignment = ft.MainAxisAlignment.START,
                controls = [],
                expand = True,
            ),
        ]
        self.expand = True

    def update_layout(self, view):
        self.controls[1].controls.clear()
        self.controls[1].controls.append(view())
        self.update()
        self.page.appbar.show_hide_items()

    def did_mount(self):
        self.controls[0].fade_in()


# main function

def WudangWebsite(page: ft.Page):    
    page.padding = 0
    page.margin = 0
    page.expand = True

    page.title = "Wudang Gongfu of New Orleans"
    page.fonts = {
            "Chinese": "fonts/MaShanZheng-Regular.ttf",
            "Heading_Bold": "fonts/ProtestRevolution-Regular.ttf"
    }

    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src = "images/Background-Extend.png",
            fit = ft.BoxFit.COVER,
        ),
    )

    page.appbar = Appbar()        

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        Layout()
    )

    def route_change():
        print(f'route change: {page.route}')
        route, view = get_view(page.route)
        page.route = route
        if (view == None):
            page.navigate('/')
        else:
            page.controls[0].update_layout(view)
    
    page.on_route_change = route_change

    def connect():
        print(f'reconnecting...')
        page.navigate(page.route)

    page.on_connect = connect

    page.route = '/'
    page.navigate(page.route)



if __name__ == '__main__':
    ft.run(WudangWebsite, view=ft.AppView.WEB_BROWSER, port=8080, assets_dir="assets")

