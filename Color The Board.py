from microbit import *
import radio
image = Image("00000:00000:00000:00000:00000")
def fillPixel():
	x = 0
	y = 0
	while not button_a.was_pressed():
		if accelerometer.get_x() > 200 and x < 4:
			x += 1
		elif accelerometer.get_x() < -200 and x > 0:
			x -= 1
		if accelerometer.get_y() > 200 and y < 4:
			y += 1
		elif accelerometer.get_y() < -200 and y > 0:
			y -= 1
		display.clear()
		display.show(image)
		display.set_pixel(x,y,int(9))
		sleep(200)
	image.set_pixel(x,y,int(6))
radio.on()
incoming = radio.receive()
while incoming == None and "0" in str(image):
	fillPixel()
	incoming = radio.receive()
if incoming == None:
	radio.send("I WON")
	display.show('W')
else:
	display.show('L')
