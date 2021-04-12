#Dont touch
from engine.engine import ps, general, inpt, pixel, time, settings
general.start()
# Type Code Here ↓↓↓↓↓

'''
framerate = 0.5
fallspeed = 1
settings.screensize(20, 40)
general.clearscreen()
general.printbrd()
ps.new(10, 0, "255 255 255", "sprite")
while True:
  if ps.getdata("sprite").y < 39:
    if fallspeed + ps.getdata("sprite").y > 39:
      ps.move("sprite", ps.getdata("sprite").x, 39, 0, 0)
    else:
      ps.move("sprite", -1, -1, 0, fallspeed)
  general.printbrd()
  time.sleep(framerate)
  general.clearscreen()
  fallspeed += 2
'''