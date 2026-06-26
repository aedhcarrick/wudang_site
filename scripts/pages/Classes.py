# Classes.py


# imports

import flet as ft
from scripts.controls.Text import Text
from scripts.controls.Image import Image


# variables

img_1 = 'images/B01.png'
img_2 = 'images/B02.png'

p_1 = '''
    \tClasses are held Monday through Saturday at **8:00 AM** in **Washington Square Park** in the French Quarter of New Orleans. Training takes place outdoors throughout the year, allowing students to experience the practice in changing weather, seasons, and conditions.\n
    \tThe atmosphere is relaxed and welcoming. Whether you are new to the internal arts or have years of experience, you are encouraged to work at your own pace while developing a deeper understanding of movement, balance, and awareness.
    '''

p_2 = '''
    \tA typical class includes stretching, qigong, foundational exercises, the study of Taijiquan's Thirteen Postures, and partner work. While techniques and methods vary from day to day, the emphasis remains the same: cultivating structure, sensitivity, coordination, and the ability to remain present under changing circumstances.\n
    \tTraining is not separated from daily life. The same qualities developed through practice—adaptability, attentiveness, and composure—are the qualities that allow us to navigate the world beyond the park.
    '''

p_3 = '''
    \tStudents should wear loose, comfortable clothing appropriate for the weather. Depending on conditions, you may also wish to bring water, sunscreen, insect repellent, a small towel, or other items that help you remain comfortable during outdoor training.\n
    \tAs with any public space, conditions in the park can be unpredictable. Part of practicing outdoors is learning to remain centered amid distractions, inconveniences, and the unexpected. We train not in a controlled environment, but in the living world itself.
    '''

p_4 = '''
    \tVisitors are welcome to observe a class before participating. If you have questions about training, scheduling, or what to expect, please feel free to get in touch.
    '''


# class definitions

class Margin(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand = 1
 

class ScrollingBox(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = ft.Column(
            scroll = ft.ScrollMode.AUTO,
            controls = [
                ft.Divider(
                    color = ft.Colors.TRANSPARENT,
                    height = 40,
                ),
                ft.Row(
                    controls = [
                        Text(p_1),
                        Image(img_1),
                    ],
                ),
                ft.Row(
                    controls = [
                        Text(p_2),
                    ],
                ),
                ft.Row(
                    controls = [
                        Image(img_2, link="https://maps.app.goo.gl/FCxGWmsfPnSbt6Sp8"),
                        Text(p_3),
                    ],
                ),
                ft.Row(
                    controls = [
                        Text(p_4),
                    ],
                ),
                ft.Divider(
                    color = ft.Colors.TRANSPARENT,
                    height = 40,
                ),
            ],
        )
        self.expand = 4


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
        self.opacity = 0
        self.animate_opacity = ft.Animation(
            curve = ft.AnimationCurve.FAST_OUT_SLOWIN,
            duration = ft.Duration(seconds=5),
        )

    def fade_in(self):
        self.opacity = 1
        self.update()

    def did_mount(self):
        self.fade_in()
        

