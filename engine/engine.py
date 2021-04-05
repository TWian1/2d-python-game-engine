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