from machine import Pin

def handle_button_press(button):
    print("Button Pressed")

button = Pin(0, Pin.IN, Pin.PULL_DOWN)
button.irq(handler=handle_button_press, trigger=Pin.IRQ_RISING)