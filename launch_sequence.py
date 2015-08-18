import pibrella, time
global state
state = 0

def abort():
	print "abort"
	pibrella.light.red.pulse(0, 0, 1, 1)
	pibrella.buzzer.fail()
	time.sleep(3)
	quit()

def button_handler(pin):
	global state
	if state == 0:
		state = state + 1
		start()
	elif state == 2:
		state = state + 1
		launch()
	elif state == 3:
		state = state + 1
		abort()

def launch():
	print "launch"
	pibrella.light.green.off()
	pibrella.light.red.pulse(0, 0, 1, 1)
	pibrella.buzzer.success()
	time.sleep(3)
	quit()


def start():
	global state
	time.sleep(2)
	pibrella.light.red.off()
	time.sleep(2)
	pibrella.light.yellow.off()
	time.sleep(2)
	pibrella.buzzer.pulse()
	pibrella.light.green.off()
	pibrella.light.green.blink(0.1)
	time.sleep(4)
	state = state + 1

pibrella.buzzer.pulse(1)
pibrella.light.pulse()
pibrella.button.pressed(button_handler)

pibrella.pause()

