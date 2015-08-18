import pibrella, time
global state
state = 0

def button_handler(pin):
	global state
	if state == 0:
		state = 1
		pibrella.buzzer.pulse(1)
		pibrella.light.pulse()
	else:
		state = 0
		pibrella.buzzer.off()
		pibrella.light.off()
		time.sleep(0.2)
		pibrella.light.green.on()

pibrella.light.green.on()
pibrella.button.pressed(button_handler)

pibrella.pause()

