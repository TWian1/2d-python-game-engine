# Commands:

Command|Input|Output|What it does
-------|-----|------|------------
eng.start()| ||starts the game engine
eng.wait(seconds)| seconds|| waits for the specified amout of seconds
eng.clearscreen()|||clears the console
eng.colorpixel(x, y, color)|X value, Y value and Color||colors the specified pixel
eng.newpixelsprite(x, y, color, name) | X Value, Y value, Color and Name||creates a new sprit that can be referenced later
eng.changepscolor(name, color)|Name Color||changes the specified sprites color
eng.moveps(name, newx, newy, offsetx, offsety)| Name, New X Value, New Y value, offset X Value and offset Y Value|| moves the position to the newx and newy values unless they are both -1 then it will offset by the offsetx and offsety
eng.clearpixelsprites()||| clears all sprites
eng.getpixeldata||Pixelsprite Data| Returns all pixelsprite data in a class
eng.textinput(Question)|Question|Answer| gives the user a text input
eng.refresh()||| prints the game board