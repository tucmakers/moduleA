from microbit import *
import utime
display.show(3)
sleep(1000)
display.show(2)
sleep(1000)
display.show(1)
sleep(1000)
display.show(0)
start = utime.ticks_us()
while not button_a.was_pressed():
	pass
stop = utime.ticks_us()
time = stop - start
time = int(time / 1000)
display.scroll(time)
