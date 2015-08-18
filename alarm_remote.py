import lirc
import pibrella

sockid = lirc.init("alarm_remote", blocking=False)
print "Started remote!"

running = True
while running:
	codeIR = lirc.nextcode()
	if codeIR:
		code = codeIR[0]
		if code == "quit":
			running = False
		elif code == "0":
			pibrella.light.blink(0.2)
		elif code == "1":
			pibrella.light.green.blink(0.04)
		elif code == "4":
			pibrella.light.green.blink(0.5)
		elif code == "7":
			pibrella.light.green.off()
		elif code == "2":
			pibrella.light.yellow.blink(0.04)
		elif code == "5":
			pibrella.light.yellow.blink(0.5)
		elif code == "8":
			pibrella.light.yellow.off()
		elif code == "3":
			pibrella.light.red.blink(0.04)
		elif code == "6":
			pibrella.light.red.blink(0.5)
		elif code == "9":
			pibrella.light.red.off()
print "Bye!"
