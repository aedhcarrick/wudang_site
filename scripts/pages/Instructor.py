# Instructor.py


# imports

import flet as ft
from scripts.controls.Text import Text
from scripts.controls.Image import Image


# variables

p_0 = '''
    Instructor: Aedh Carrick
'''

p_1 = '''
    \tMy introduction to the internal arts began with Zheng Man-Qing's 37-posture Taijiquan form, studied under David Blake, a direct student of Professor Cheng. For five years we trained together, exploring the principles of relaxation, structure, sensitivity, and partner work that distinguish the classical internal arts. Afterward, the practice continued as a daily discipline for another six years, allowing the lessons of the form to deepen beyond choreography and become part of everyday life.
'''

p_2 = '''
    \tSeeking a broader understanding of the tradition from which these arts emerged, I traveled to Wudangshan, China, where I studied Wudang Quan under Master Chen Shixing. There I was immersed not only in Taijiquan, but in the wider curriculum of Wudang internal martial arts, qigong, and the culture that has preserved these practices for generations. Living and training in the mountains offered a perspective that cannot be gained from occasional seminars or short visits. It revealed the internal arts as a way of approaching movement, learning, and life.
'''

p_3 = '''
    \tAfter returning to New Orleans, I began teaching Shi San Shi (Thirteen Postures) in Washington Square Park. While the class draws upon the broader Wudang tradition, its foundation remains Taijiquan and the principles that first inspired my practice. Rather than emphasizing the accumulation of techniques, the instruction focuses on developing fangsong (relaxed integration), tingjin (listening skill), and the ability to move with balance, connection, and natural responsiveness.
'''

p_4 = '''
    \tThe goal of every class is to create an environment where students can investigate these principles for themselves. Progress is measured less by outward performance than by increasing clarity, sensitivity, and ease. Whether a student comes seeking martial skill, health, or simply a more grounded way of moving through the world, the practice begins in the same place: patient attention to the body, an open mind, and a willingness to learn.
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
                        ft.Text(
                            style = ft.TextStyle(
                                color = '#000',
                            ),
                            theme_style = ft.TextThemeStyle.BODY_LARGE,
                            value = p_0,
                        ),
                    ],
                ),
                ft.Row(
                    controls = [
                        Text(p_1),
                    ],
                ),
                ft.Row(
                    controls = [
                        Text(p_2),
                        Image("images/A01.png"),
                    ],
                ),
                ft.Row(
                    controls = [
                        Image("images/A02.png"),
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

class Instructor_Content(ft.Container):
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
        self.on_animation_end = self.show_menu

    def fade_in(self):
        self.opacity = 1
        self.update()

    def did_mount(self):
        self.fade_in()

    def show_menu(self):
        self.page.appbar.show_menu()

