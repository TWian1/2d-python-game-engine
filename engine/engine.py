import os
import json
def inititializeboard(height, width, startcolor):
  boardcopy = []
  for a in range(height):
    for b in range(width):
      boardcopy.append(startcolor + "\n")
    boardcopy.append("line\n")
  board = open("engine/ImageProcessing/image.txt", 'w')
  board.writelines(boardcopy)

def start():
  clearpixelsprites()
  settings = json.loads(open('engine/settings.json', 'r').read())
  clearmsg = ['cls', 'clear'][int(input("Linux(1) or Microsoft(0)?"))]
  change = open('engine/settings.json', 'r').readlines()
  change[4] = " \"OS\": \"" + clearmsg + "\"\n"
  open('engine/settings.json', 'w').writelines(change)
  inititializeboard(int(settings["GameHeight"]), int(settings["GameWidth"]), settings["BoardStartColor"])

def refresh():
  import engine.ImageProcessing.render as prcs
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

def clearpixelsprites(): open('engine/data/pixelsprites.txt', 'w')

def newpixelsprite(x, y, color, name):
  pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
  for a in pixelsprites:
    name2 = ""
    space = True
    for b in a:
      if b == " ": space = False
      if space: name2 += b
    if name2 == name: return
  pixelspriteswrite = open('engine/data/pixelsprites.txt', 'w')
  pixelsprites.append(name + " " + color + " " + str(x) + " " + str(y) + "\n")
  pixelspriteswrite.writelines(pixelsprites)
  colorpixel(x, y, color)

def checkforsprites(inpname):
  pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
  names = []
  for a in pixelsprites:
    name = ""
    space = True
    for b in a:
      if b == " ": space = False
      if space: name += b
    names.append(name)
  if inpname in names: return True
  else: return False

def indexsprite(inpname):
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
    

def changepscolor(name, color):
  pixelsprites = open('engine/data/pixelsprites.txt', 'r').readlines()
  if checkforsprites(name):
    spaces = 0
    tempx = ""
    tempy = ""
    for a in pixelsprites[indexsprite(name)]:
      if a == " ":
        spaces+=1
      else:
        if spaces == 4:
          tempx += a
        if spaces == 5:
          tempy += a
    pixelsprites[indexsprite(name)] = name + " "+ color + " " + tempx + " " + tempy
    open('engine/data/pixelsprites.txt', 'w').writelines(pixelsprites)
    colorpixel(int(tempx), int(tempy), color)