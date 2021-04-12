
# 2d Game Engine
‎simple to use game engine that uses the console to display the result with ascii.
‎
‎‎
‎
# Commands:

‎
‎
## General Commands:



Command|Input|What it does
-------|-----|------------
general.start()| |starts the game engine
general.clearscreen()||clears the console
general.printbrd()|| prints the game board

## Time Commands:
Command|Input|Output|What it does
-------|-----|------|------------
time.sleep(seconds)|seconds||waits for the specified amount of time
time.time()||current time|returns the curren time in seconds since 1970




## Pixel Commands:



Command|Input|Output|What it does
-------|-----|------|------------
pixel.colorfill|starting X pos, starting Y pos, width, length, color||Fills the selected area
pixel.color(x, y, color)|X value, Y value and Color||colors the specified pixel
pixel.data.a()||All pixel colors|Returns a list of all color values for each pixel
pixel.data.p(x, y)|X Value, Y Value|Color|Returns the color of the selected pixel



## Input Commands:



Command|Input|Output|What it does
-------|-----|------|------------
inpt.text(Question)|Question|Answer| gives the user a text input



## PixelSprite Commands:



Command|Input|Output|What it does
-------|-----|------|------------
ps.new(x, y, color, name) | X Value, Y value, Color and Name||creates a new sprit that can be referenced later
ps.move(name, newx, newy, offsetx, offsety)| Name, New X Value, New Y value, offset X Value and offset Y Value|| moves the position to the newx and newy values unless they are both -1 then it will offset by the offsetx and offsety
ps.changecolor(name, color)|Name, Color||changes the specified sprites color
ps.getdata||Pixelsprite Data| Returns all pixelsprite data in a class
ps.getdata(name)|Name|Pixelsprite Data|Returns data for the selected Pixelsprite in a class
ps.clear()||| clears all sprites

## Settings Commands:
Command|Input|What it does
-------|-----|------------
settings.screensize(x, y)|X size, Y size|WARNING clears the board data while changing the size.
settings.startingcolor(color)|color|WARNING clears the board data while changing the background color/ starting color

# Examples:


## general.clearscreen()
```Python
print("hi")
general.wait(2)
general.clearscreen()
print("you can't see the original message)
```
clears the console/screen


## general.printbrd()
```Python
general.printbrd()
```
Output:
```
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
prints the display
```
## time.sleep(seconds)
```Python
print("hi")
time.sleep(2)
print("it's been 2 seconds)
```
does next actions after the selected amount of time

## time.time()
```Python
start = time.time()
10*100
end = time.time()
dif = end - start
print(f"It took {dif} seconds to do 10*100")
```
returns the current time in seconds since 1970

## pixel.colorfill(xpos, ypos, width, length, color)
```Python
pixel.colorfill(1, 1, 10, 10, "255 255 255")
general.printbrd()
print("it made a box that is 10 wide, 10 tall and its upper left corner is at 1, 1")
```
fills the selected area with the color selected

## pixel.color(x, y, color)
```Python
pixel.color(10, 10, "255 255 255")
general.printbrd()
print("look one of the pixels turned white!")
```
sets the specified pixel to be the spedified color using RGB.


## pixel.data.a()
```Python
pixel.color(0, 0, "0 0 255")
print(pixel.data.a())
```
returns all pixel color values in a list.


## pixel.data.p(x, y)
```Python
pixel.color(0, 1, "255 255 0")
print(pixel.data.p(0, 1))
print(pixel.data.p(0, 0))
print("I can seet that at 0, 0 the pixel is black while at 0, 1 it is yellow")
```
returns the pixel color at the loaction selected.


## inpt.text(Question)
```Python
if inpt.text("Do you like coding?") == "yes":
    print("NEEERD")
```
Creates a text input in the console


## ps.new(x, y, color, name)
```Python
ps.new(2, 2, "0 255 0", "Dog")
general.printbrd()
```
Creates a Pixel sprite which can be referenced later


## ps.move(name, newx, newy, offsetx, offsety)
```Python
ps.new(2, 2, "0 255 0", "Dog")
general.printbrd()
general.wait(5)
ps.move("Dog", 9, 9, 0, 0)
general.clearscreen()
general.printbrd()
print("The Pixelsprite moved from the upper left to the middle!")
```
OR
```Python
ps.new(2, 2, "0 255 0", "Dog")
general.printbrd()
general.wait(5)
ps.move("Dog", -1, -1, 3, 0)
general.clearscreen()
general.printbrd()
print("The Pixelsprite moved to the right 3!")
```
Moves the specified Pixelsprite

## ps.changecolor(name, color)
```Python
ps.new(2, 2, "0 255 0", "Dog")
general.printbrd()
general.wait(5)
ps.changecolor("Dog", "255 255 255")
general.clearscreen()
general.printbrd()
print("The Pixel sprite changed color!")
```


## ps.getdata(x, y)
```Python
ps.new(3, 3, "0 255 255", "person")
print(ps.getdata("person"))
```
Pixelsprite data for the selected Pixelsprite in a class

Or

```Python
ps.new(3, 3, "0 255 255", "person")
ps.new(6, 5, "0 255 255", "person2")
ps.new(9, 4, "0 255 255", "person3")
print(ps.getdata())
```
Pixelsprited data for all Pixelsprites


## ps.clear(name)

```Python
ps.new(3, 3, "0 255 255", "person")
ps.new(6, 5, "0 255 255", "person2")
ps.new(9, 4, "0 255 255", "person3")
general.printbrd()
general.wait(5)
ps.clear()
general.clearscreen()
general.printbrd()
print("all Pixelsprites have been deleted")
```
Or
```Python
ps.new(3, 3, "0 255 255", "person")
ps.new(6, 5, "0 255 255", "person2")
ps.new(9, 4, "0 255 255", "person3")
general.printbrd()
general.wait(5)
ps.clear("person2")
general.clearscreen()
general.printbrd()
print("The person2 sprite has been deleted")
```
Deletes the selected sprite or if none are listed it deletes all.

## settings.screensize(x, y)
```Python
settings.screensize(3, 3)
general.printbrd()
print("the screen is now a 3x3")
```
Changes the screensize WHILE CLEARING THE BOARD DATA

## settings.startingcolor(color)
```Python
settings.startingcolor("255 255 255")
general.printbrd()
print("the background/default color is now white")
```
Changes the starting/default/background color WHILE CLEARING THE BOARD DATA