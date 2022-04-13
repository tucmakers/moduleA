from microbit import *
import speech
import random

PITCH = 70
SPEED = 100
MOUTH = 100
THROAT = 128

questions = [
    {"question": "-The capital of Greece is, Athens.", "correct": True},
    {"question": "-The capital of Germany is, London.", "correct": False},
    {"question": "-The capital of Italy is, Rome.", "correct": True},
    {"question": "-The capital of Poland is, Moscow.", "correct": False},
    {"question": "-The capital of Germany is, Berlin.", "correct": True},
    {"question": "-The capital of Russia is, Moscow.", "correct": True},
]


def announce_question(question):
    speech.say(question["question"], pitch=PITCH, speed=SPEED, mouth=MOUTH, throat=THROAT)


def process(question, option):
    if question["correct"] == option:
        display.show(Image.HAPPY)
        return 1
    display.show(Image.SAD)
    return -1


score = 0
while True:
    question = random.choice(questions)
    questions.remove(question)
    announce_question(question)
    while True:
        if button_a.was_pressed():
            score += process(question, True)
            break
        elif button_b.was_pressed():
            score += process(question, False)
            break
    if len(questions) == 0:
        break
display.show(score)
