# Classes.py


# imports

import flet as ft


# variables

img_1 = 'images/B01.png'
img_2 = 'images/B02.png'

text_1 = '''
    Classes are held Monday through Saturday at **8:00 AM** in **Washington Square Park** in the French Quarter of New Orleans. Training takes place outdoors throughout the year, allowing students to experience the practice in changing weather, seasons, and conditions.\n
    The atmosphere is relaxed and welcoming. Whether you are new to the internal arts or have years of experience, you are encouraged to work at your own pace while developing a deeper understanding of movement, balance, and awareness.
    '''

text_2 = '''
    A typical class includes stretching, qigong, foundational exercises, the study of Taijiquan's Thirteen Postures, and partner work. While techniques and methods vary from day to day, the emphasis remains the same: cultivating structure, sensitivity, coordination, and the ability to remain present under changing circumstances.\n
    Training is not separated from daily life. The same qualities developed through practice—adaptability, attentiveness, and composure—are the qualities that allow us to navigate the world beyond the park.
    '''

text_3 = '''
    Students should wear loose, comfortable clothing appropriate for the weather. Depending on conditions, you may also wish to bring water, sunscreen, insect repellent, a small towel, or other items that help you remain comfortable during outdoor training.\n
    As with any public space, conditions in the park can be unpredictable. Part of practicing outdoors is learning to remain centered amid distractions, inconveniences, and the unexpected. We train not in a controlled environment, but in the living world itself.
    '''

text_4 = '''
    Visitors are welcome to observe a class before participating. If you have questions about training, scheduling, or what to expect, please feel free to get in touch.
    '''


# class definitions

class Image(ft.Container):
    def __init__(self, src, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = ft.Image(
            src = src,
            width = 400,
            fit = ft.BoxFit.COVER,
            expand = True,
        )


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
        

class Margin(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand = 1
        self.opacity = 0
        self.animate_opacity = ft.Animation(
            curve = ft.AnimationCurve.EASE_IN,
            duration = ft.Duration(seconds=3),
        )

    def fade_in(self):
        self.opacity = 1
        self.update()


class ScrollingBox(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = ft.Column(
            scroll = ft.ScrollMode.AUTO,
            controls = [
                ft.Row(
                    controls = [
                        Text(text_1),
                        Image(img_1),
                    ],
                ),
                ft.Row(
                    controls = [
                        Text(text_2),
                    ],
                ),
                ft.Row(
                    controls = [
                        Image(img_2),
                        Text(text_3),
                    ],
                ),
                ft.Row(
                    controls = [
                        Text(text_4),
                    ],
                ),
                ft.Divider(
                    color = ft.Colors.TRANSPARENT,
                    height = 40,
                ),
            ],
        )
        self.expand = 4
        self.opacity = 0
        self.animate_opacity = ft.Animation(
            curve = ft.AnimationCurve.EASE_IN,
            duration = ft.Duration(seconds=5),
        )

    def fade_in(self):
        self.opacity = 1
        self.update()


# page content

class Classes_Content(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = ft.Row(
            controls = [
                Margin(),
                ScrollingBox(),
                Margin(),
            ],
            expand = True,
        )
        self.expand = True

    def fade_in(self):
        for control in self.content.controls:
            control.fade_in()


