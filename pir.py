import pibrella
import time

pibrella.output.h.on()

while True:
	if pibrella.input.d.read():
		print "Detected movement"
	else:
		print "All clear"
	time.sleep(0.25)
