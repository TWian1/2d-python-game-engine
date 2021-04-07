# Commands:
### General Commands:

Command|Input|Output|What it does
-------|-----|------|------------
start()| ||starts the game engine
wait(seconds)| seconds|| waits for the specified amout of seconds
clearscreen()|||clears the console
colorpixel(x, y, color)|X value, Y value and Color||colors the specified pixel
textinput(Question)|Question|Answer| gives the user a text input
refresh()||| prints the game board

### PixelSprite Commands:

Command|Input|Output|What it does
-------|-----|------|------------
ps.new(x, y, color, name) | X Value, Y value, Color and Name||creates a new sprit that can be referenced later
ps.move(name, newx, newy, offsetx, offsety)| Name, New X Value, New Y value, offset X Value and offset Y Value|| moves the position to the newx and newy values unless they are both -1 then it will offset by the offsetx and offsety
ps.changecolor(name, color)|Name, Color||changes the specified sprites color
ps.getdata||Pixelsprite Data| Returns all pixelsprite data in a class
ps.clear()||| clears all sprites