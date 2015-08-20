import pibrella, time

def button_handler(pin):
	pibrella.buzzer.alarm()
	time.sleep(1)
	pibrella.buzzer.off()

pibrella.button.pressed(button_handler)
pibrella.pause()
