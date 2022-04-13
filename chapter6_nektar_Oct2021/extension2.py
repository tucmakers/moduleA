from machine import Pin, ADC, PWM
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
            
class Potentiometer:
	def __init__(self, pin_number):
		self.pin = ADC(Pin(pin_number))

	def value(self):
		return self.pin.read_u16()
	
class Servo:
    def __init__(self, pin_number):
        self.pin = PWM(Pin(pin_number))
        self.pin.freq(50)
        self.angle(0)
    
    def angle(self, angle):
        if angle<0:
            angle = 0
        elif angle>180:
            angle = 180
        self.pin.duty_u16((angle*38)+1311)
        
class Points:
    def __init__(self, servo):
        self.points = 0
        self.servo = servo
        
    def won(self):
        self.points += 10
        self.servo.angle(self.points)
        
    def lost(self):
        self.points -= 10
        self.servo.angle(self.points)

leds = [Led(0, "Blue"), Led(1, "Blue"), Led(2, "Blue"), Led(3, "Blue"), Led(4, "Red")]
button = Button(5)
display = Display(leds)
pot = Potentiometer(26)
servo = Servo(6)
points = Points(servo)

while True:
    while not button.was_pressed():
        display.next_led()
        sleep(pot.value()/100000)
    if display.color() == "Blue":
        points.lost()
        display.all_on()
        sleep(2)
        display.all_off()
    else:
        points.won()
        sleep(2)
