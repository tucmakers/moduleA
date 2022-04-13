from machine import Pin
from time import sleep

class Led:
    def __init__(self, pin_number, color):
        self.color = color
        self.pin = Pin(pin_number, Pin.OUT)

    def on(self):
        self.pin.on()

    def off(self):
        self.pin.off()

class Button:
    def __init__(self, pin_number):
        self.pin = Pin(pin_number, Pin.IN, Pin.PULL_DOWN)
        self.pressed = False
        self.pin.irq(handler=self.handle_button_pressed, trigger=Pin.IRQ_RISING)

    def was_pressed(self):
        if (self.pressed):
            self.pressed = False
            return True
        return False

    def handle_button_pressed(self, pin):
        self.pressed = True
        
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
        
    def color(self):
        return self.leds[self.position].color
    
    def all_on(self):
        for led in self.leds:
            led.on()
    
    def all_off(self):
        for led in self.leds:
            led.off()
            
leds = [Led(0, "Blue"), Led(1, "Blue"), Led(2, "Blue"), Led(3, "Blue"), Led(4, "Red")]
button = Button(5)
display = Display(leds)

while True:
    while not button.was_pressed():
        display.next_led()
        sleep(0.1)
    if display.color() == "Blue":
        display.all_on()
        sleep(2)
        display.all_off()
    else:
        sleep(2)

