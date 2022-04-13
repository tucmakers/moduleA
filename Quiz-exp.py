from microbit import *
import speech
import random

PITCH = 70
SPEED = 100
MOUTH = 100
THROAT = 128

questions = [
    {
        "question": "-The capital of Greece is,",
        "options": ["-Rome", "-Athens", "-Berlin", "-Paris"],
        "correct": 1,
    },
    {
        "question": "-The capital of Germany is,",
        "options": ["-Rome", "-Athens", "-Berlin", "-Paris"],
        "correct": 2,
    }
]


def make_question(question):
    speech.say(question["question"], pitch=PITCH, speed=SPEED, mouth=MOUTH, throat=THROAT)
    sleep(1000)
    while True:
        for i, opt in enumerate(question["options"]):
            speech.say(opt, pitch=PITCH, speed=SPEED, mouth=MOUTH, throat=THROAT)
            while True:
                if button_a.was_pressed():
                    break
                elif button_b.was_pressed():
                    return process(question, i)


def process(question, option):
    if question["correct"] == option:
        display.show(Image.HAPPY)
        return 1
    display.show(Image.SAD)
    return -1


score = 0
while True:
    try:
        question = random.choice(questions)
    except IndexError:
        break
    questions.remove(question)
    score += make_question(question)

display.show(score)
