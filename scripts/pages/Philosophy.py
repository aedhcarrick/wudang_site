# Philosophy.py


# imports

import flet as ft
from scripts.controls.Text import Text
from scripts.controls.Image import Image


# variables

p_0 = '''
    Philosophy
    '''

p_1 = '''
    \tThe Daoist tradition begins with the recognition that life unfolds through the interplay of complementary forces. Hard and soft, full and empty, movement and stillness do not exist in isolation. Each contains the seed of the other, and each gives rise to the other. Harmony is not achieved by eliminating one side in favor of the other, but by understanding their relationship.
    '''

p_2 = '''
    \tThe philosophy of Taiji expresses this principle through the dynamic balance of apparent opposites. Rather than meeting force with force, Taiji seeks the point at which opposing tendencies can be reconciled and transformed. The familiar symbol of yin and yang illustrates this idea: every condition is in the process of becoming its complement. Stability emerges not from rigidity, but from adaptability.\
    '''

p_3 = '''
    \tTaijiquan explores these principles through the body. Instead of relying primarily on muscular strength, practitioners learn to develop awareness, alignment, and connection. The goal is not simply to perform movements, but to cultivate a quality of responsiveness that allows action to arise naturally from present conditions.
    '''

p_4 = '''
    \tTwo of the most important skills in this process are fangsong (放松) and tingjin (听劲). Although often translated as "relaxation," fangsong refers to the gradual release of unnecessary tension. As habitual effort falls away, the body becomes more integrated, efficient, and sensitive. Relaxation is not collapse; it is the removal of what interferes with natural function.
    '''

p_5 = '''
    \tTingjin, often translated as "listening energy," is the ability to perceive and understand force through direct experience. In partner practice, this means learning to feel subtle changes in balance, intention, and pressure. More broadly, it is the cultivation of attentiveness itself—the capacity to receive information before reacting to it.
    '''

p_6 = '''
    \tThese two qualities support one another. Without fangsong, excessive tension obscures perception. Without tingjin, relaxation becomes passive and directionless. Together they form the foundation of Taijiquan practice, allowing strength to emerge from sensitivity and action to emerge from understanding.
    '''

p_7 = '''
    \tIn this sense, Taijiquan is neither a collection of techniques nor a set of abstract philosophical ideas. It is an ongoing investigation into how we relate to ourselves, to others, and to the forces that shape our lives. Through practice, the principles of Taiji cease to be concepts and become lived experience.
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
                    ],
                ),
                ft.Row(
                    controls = [
                        Text(p_3),
                    ],
                ),
                ft.Row(
                    controls = [
                        Text(p_4),
                    ],
                ),
                ft.Row(
                    controls = [
                        Text(p_5),
                    ],
                ),
                ft.Row(
                    controls = [
                        Text(p_6),
                    ],
                ),
                ft.Row(
                    controls = [
                        Text(p_7),
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

class Philosophy_Content(ft.Container):
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

