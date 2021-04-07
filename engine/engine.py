import os
import json
import time
def inititializeboard(height, width, startcolor):
  boardcopy = []
  for a in range(height):
    for b in range(width):
      boardcopy.append(startcolor + "\n")
    boardcopy.append("line\n")
  board = open("engine/ImageProcessing/image.txt", 'w')
  board.writelines(boardcopy)

def start():
  ps.clear()
  settings = json.loads(open('engine/settings.json', 'r').read())
  clearmsg = ['cls', 'clear'][int(input("Linux(1) or Microsoft(0)?"))]
  change = open('engine/settings.json', 'r').readlines()
  change[4] = " \"OS\": \"" + clearmsg + "\"\n"
  open('engine/settings.json', 'w').writelines(change)
  inititializeboard(int(settings["GameHeight"]), int(settings["GameWidth"]), settings["BoardStartColor"])

def refresh():
  import engine.ImageProcessing.render as prcs
  data = ps.getdata()
  for a in range(len(data.names)):
    colorpixel(data.xs[a], data.ys[a], data.colors[a])
  prcs.main()

def update(newboard):
  board = open("engine/ImageProcessing/image.txt", 'w')
  board.writelines(newboard)


def colorpixel(x, y, color):
  settings = json.loads(open('engine/settings.json', 'r').read())
  imagefilecopy = open('engine/ImageProcessing/image.txt', 'r').readlines()
  index = x + (y*int(settings["GameWidth"])) + y
  imagefilecopy[index] = color + "\n"
  update(imagefilecopy)

def clearscreen():
  settings = json.loads(open('engine/settings.json', 'r').read())
  os.system(settings["OS"])


def wait(seconds):
  time.sleep(seconds)

def textinput(Question):
  a = input("\n" + Question)
  print("\n")
  return a

class ps:
  def move(name, x, y, ofx, ofy):
    if ps.check(name):
      pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
      index = 0
      data = ps.getdata()
      indexsprte = ps.index(name)
      oldposx = data.xs[indexsprte]
      oldposy = data.ys[indexsprte]
      if x == -1 and y == -1:
        index = data.xs[indexsprte] + ofx
        indey = data.ys[indexsprte] + ofy
      else:
        index = x
        indey = y
      pixelsprites[indexsprte] = name + " " + data.colors[indexsprte] + " " + str(index) + " " + str(indey)
      open('engine/data/pixelsprites.txt', 'w').writelines(pixelsprites)
      colorpixel(oldposx, oldposy, "0 0 0")

  def changecolor(name, color):
    pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
    if ps.check(name):
      spaces = 0
      tempx = ""
      tempy = ""
      for a in pixelsprites[ps.index(name)]:
        if a == " ":
          spaces+=1
        else:
          if spaces == 4:
            tempx += a
          if spaces == 5:
            tempy += a
      pixelsprites[ps.index(name)] = name + " "+ color + " " + tempx + " " + tempy
      open('engine/data/pixelsprites.txt', 'w').writelines(pixelsprites)

  def new(x, y, color, name):
    data = ps.getdata()
    pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
    if name in data.names: return
    pixelspriteswrite = open('engine/data/pixelsprites.txt', 'w')
    pixelsprites.append(name + " " + color + " " + str(x) + " " + str(y) + "\n")
    pixelspriteswrite.writelines(pixelsprites)

  def getdata():
    pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
    class data:
      colors = []
      names = []
      xs = []
      ys = []
    for a in pixelsprites:
      color = ""
      tempx = ""
      tempy = ""
      name = ""
      spaces = 0
      for b in a:
        if b == " ": 
          spaces += 1
          if spaces in [2, 3]: color += " "
        else:
          if spaces in [1, 2, 3]: color += b
          if spaces == 4: tempx += b
          if spaces == 5: tempy += b
          if spaces == 0: name += b
      data.colors.append(color)
      data.names.append(name)
      data.xs.append(int(tempx))
      data.ys.append(int(tempy))
    return data

  def clear(): 
    data = ps.getdata()
    for a in range(len(data.names)):
      colorpixel(data.xs[a], data.ys[a], "0 0 0")
    open('engine/data/pixelsprites.txt', 'w')

  def check(inpname):
    data = ps.getdata()
    if inpname in data.names: return True
    else: return False

  def index(inpname):
    pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
    counter = -1
    for a in pixelsprites:
      counter +=1
      name = ""
      space = True
      for b in a:
        if b == " ": space = False
        if space: name += b
      if name == inpname: return counter