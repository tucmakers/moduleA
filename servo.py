from machine import Pin, PWM
from time import sleep

# (on the internet) SG90 has 2 per cent duty cycle for 0 degrees and 12.5 per cent for 180 (probably tested)
# my calculations say that for 50Hz we should use 5% to 10% for 1ms and 2ms respectively (didn't measure output)
# so for the duty_u16 we have to use 1311 to 8192
# to find the value we use this formula angle*38+1311
# first we enlarge the range by a factor of 18.2 and then we slide it up by 3277 to match exactly the range (3277, 6554)

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

servo = Servo(6)
while True:
    servo.angle(0)
    sleep(2)
    servo.angle(180)
    sleep(2)
