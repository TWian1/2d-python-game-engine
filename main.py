import engine.engine as eng
import time
eng.start()

eng.newpixelsprite(2, 2, "0 0 255", "ted")
eng.clearscreen()
eng.refresh()
time.sleep(5)
eng.changepscolor("ted", "255 0 0")
eng.clearscreen()
eng.refresh()