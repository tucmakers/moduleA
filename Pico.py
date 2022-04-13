from machine import Pin
from time import sleep

class Led:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.pin = Pin(position, Pin.OUT)

    def on(self):
        self.pin.on()

    def off(self):
        self.pin.off()

    def is_on(self):
        return self.pin.value()

def handle_button_pressed(pin):
    pin.was_pressed = True
    print("pressed")

class Button(Pin):
    def __init__(self, position):
        super().__init__(position, Pin.IN, Pin.PULL_DOWN)
        self.position = position
        self.was_pressed = False
        self.irq(handler=handle_button_pressed, trigger=Pin.IRQ_RISING)

    def was_pressed(self):
        if (self.was_pressed):
            self.was_pressed = False
            return True
        return False

class Display:
    def __init__(self, leds):
        self.leds = leds
        self.position = 0

    def next_led(self):
        self.leds[self.position].off()
        self.position += 1
        if self.position >= len(self.leds):
            self.position = 0
        self.leds[self.position].on()

leds = [Led(2, "Blue"), Led(3, "Red"), Led(4, "Green")]
button = Button(5)
display = Display(leds)

while True:
    display.next_led()
    sleep(1)
