# quotes.py

import flet as ft
import random


ZHUANGZI_QUOTES = [
    "If water derives lucidity from stillness, how much more the faculties of the mind.",
    "The perfect man uses his mind as a mirror. It grasps nothing; it refuses nothing. It receives, but does not keep.",
    "To a mind that is still, the whole universe surrenders.",
    "The supreme man uses his mind like a mirror; it does not move with things, yet it responds to them.",
    "When the water is still, it reflects the true nature of things.",
    "The man of virtue remains still in the face of change.",
    "Flow like water, reflect like a mirror, respond like an echo, be calm like still water.",
    "To the mind of a sage, everything is reflected in the mirror of heaven and earth.",
    "The torch of chaos and doubt — this is what the sage steers by.",
    "The person of character is like a mirror, which does not go to meet things, nor does it follow them.",
    "Flow with whatever may happen and let your mind be free.",
    "Do not struggle. Go with the flow of things, and you will find yourself at one with the mysterious unity of the Universe.",
    "To yield is to be preserved whole. To be bent is to become straight.",
    "The softest things in the world overcome the hardest things in the world.",
    "Easy is right. Begin right and you are easy. Continue easy and you are right.",
    "By lack of holding on, a person can never be lost.",
    "Happiness is the absence of the striving for happiness.",
    "Great wisdom is generous; petty wisdom is contentious.",
    "Great speech is impassioned; petty speech is cantankerous.",
    "Those who divide things are missing something. Those who judge things are missing something.",
    "Concentrate your will. Hear not with your ears, but with your mind. Hear not with your mind, but with your breath.",
    "Hearing stops with the ear; the mind stops with signs. But breath is empty and waits on all things.",
    "The Way gathers in emptiness alone. Emptiness is the fasting of the mind.",
    "Do not listen with your ears, listen with your mind. Do not listen with your mind, listen with your spirit.",
    "The baby howls all day, yet its throat never gets hoarse — harmony at its height!",
    "If you have insight, you use your inner eye, your inner ear, to pierce to the heart of things.",
    "You have to fast your mind. It is not difficult to stop walking; the hard thing is to walk without touching the ground.",
    "Embody to the full what has no end and wander where there is no path.",
    "The right path to go by is the right way to forget.",
    "Forget the years; forget distinctions. Leap into the boundless and make it your home.",
    "When the shoe fits, the foot is forgotten; when the belt fits, the belly is forgotten.",
    "When the heart is right, 'for' and 'against' are forgotten.",
    "The fish trap exists for the fish. Once you've gotten the fish, you can forget the trap.",
    "Words exist because of meaning. Once you've gotten the meaning, you can forget the words.",
    "Look at this window; it is nothing but a hole in the wall, but because of it, the whole room is full of light.",
    "The point is to use the useless. Then you can understand the useful.",
    "Do not be an embodies of fame; do not be a storehouse of schemes; do not be an undertaker of projects; do not be a proprietor of wisdom.",
    "He who binds himself to a joy does the winged life destroy; he who kisses the joy as it flies lives in eternity's sunrise.",
    "Heaven and earth were born at the same time I was, and the ten thousand things are one with me.",
    "All things come from a common source, and all return to it.",
    "A frog in a well cannot discuss the ocean, because he is limited by the size of his well.",
    "The summer insect cannot discourse of ice, because it is confused by the constraints of its season.",
    "There is a limit to our life, but to knowledge there is no limit.",
    "Your life has a limit, but knowledge has none. If you use what is limited to pursue what has no limit, you will be in danger.",
    "The multi-talented person is easily fatigued; the clever person is easily worried.",
    "He who knows that he is a fool is not the biggest fool.",
    "He who knows he is mistaken is not utterly mistaken.",
    "The great Way has no gates, a thousand roads enter it.",
    "Birth is not a beginning; death is not an end.",
    "The newborn calf doesn't fear the tiger."
]


def fetch_random_quote():
    return random.choice(ZHUANGZI_QUOTES)


