import pibrella
import time

pibrella.output.e.on()

while True:
	if pibrella.input.c.read():
		print "All Clear"
	else:
		print "Beam broken"
	time.sleep(0.25)
