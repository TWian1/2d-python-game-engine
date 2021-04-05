import engine.engine as eng
import time
eng.start()
eng.newpixelsprite(2, 2, "255 255 255", "lol")
eng.clearscreen()
eng.refresh()
for a in range(5):
  time.sleep(0.5)
  eng.changepscolor("lol", "255 0 0")
  eng.clearscreen()
  eng.refresh()
  time.sleep(0.5)
  eng.changepscolor("lol", "255 255 255")
  eng.clearscreen()
  eng.refresh()
eng.clearpixelsprites()
eng.clearscreen()
eng.refresh()