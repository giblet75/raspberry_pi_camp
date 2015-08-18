import pibrella
import time


time.sleep(0.1)
pibrella.buzzer.melody([3,5,7,3,3,5,7,3,7,8,10,10,7,8,10,10,10,0,10,8,7,3,3,10,0,10,8,7,3,3], 0.5, False)
pibrella.pause()
