from microbit import *
import radio
ships = Image("00090:99090:00090:00000:00990")
hits = Image("00000:00000:00000:00000:00000")
pointx = 0
pointy = 0

def select_hit_point():
	global pointx, pointy# your own code
	while not button_a.was_pressed():
		if accelerometer.get_x() > 300 and pointx < 4:
			pointx = pointx + 1
		elif accelerometer.get_x() < -300 and pointx > 0:
			pointx = pointx - 1
		if accelerometer.get_y() > 300 and pointy < 4:
			pointy = pointy + 1
		elif accelerometer.get_y() < -300 and pointy > 0:
			pointy = pointy - 1
		display.clear()
		display.show(hits)
		display.set_pixel(pointx,pointy,int(9))
		sleep(200)

def wait_for_response():
	incoming = radio.receive()
	while incoming == None:
		incoming = radio.receive()
	return incoming

def attacker():
	global pointx, pointy# your own code
	select_hit_point()
	radio.send(str(pointx)+str(pointy))
	incoming = wait_for_response()
	if incoming == "hit":
		hits.set_pixel(pointx,pointy,int(9))
	elif incoming == "miss":
		hits.set_pixel(pointx,pointy,int(3))
	display.show(hits)
def defender():
	incoming = wait_for_response()
	if ships.get_pixel(int(incoming[0]), int(incoming[1])) == 9:
		radio.send("hit")
		ships.set_pixel(int(incoming[0]), int(incoming[1]),3)
	else:
		radio.send("miss")
	display.show(ships)

play = defender
radio.on()
incoming = radio.receive()
while incoming == None:
	incoming = radio.receive()
	if button_a.was_pressed():
		radio.send("attacker")
		play = attacker
		break

while True:
	play()
	play = attacker if play==defender else defender
	sleep(3000)
	if not '9' in str(ships):
		break

display.show("L")
