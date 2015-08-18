import pibrella
import time

pibrella.output.h.on();
print "Wait for it!"
time.sleep(0.5)

def ping():
	time.sleep(0.2)
	pibrella.output.g.on()
	time.sleep(0.00001)
	pibrella.output.g.off()
	#print "Fired!"
	#time.sleep(1)
	#pibrella.light.green.on()
	while (pibrella.input.d.read() == 0):
		pulse_start = time.time()

	while (pibrella.input.d.read() == 1):
		pulse_end = time.time()

	pibrella.light.off()
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 34000 / 2
	#17150
	print "Distance: %.1f cm" % distance

pibrella.loop(ping)
pibrella.pause()
