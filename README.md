# Physics Golf

I used to love playing Flash golf games. Now that Flash is gone, I wanted to make my own from scratch!  
This is a golf game with an editor and terminal, but no campaign or menus (getting this far took a long time!).

## Installation & Execution
### bash/zsh: 
Run `git clone https://github.com/epicary22/physics_golf.git <directory>`, where `<directory>` is the directory you 
want to clone this repository into.  
Make sure you have pygame installed by running `python3 -m pip install pygame` in the `<directory>`.  
Then, run `python3 main.py` from the `<directory>` to run the golf game!

## Tutorial


## Controls
To putt the ball, press the Space key. It will putt in the direction of the line coming out of it.  
To change the putt direction, hold the Left and Right arrow keys.  
To change the putt strength, hold the Up and Down arrow keys.  
You can view the game's grid and cursor coordinates by holding down the `g` key.

## Terminal
Press the `4` key to access the terminal. This is where you can start actually playing around with the game.
### Commands
* `zoomies [on | off]` - enter or exit "zoomies mode". See the "Zoomies Mode" section for more information.
* `color <colorset>` - sets the color of the level to the given `<colorset>`. See the "Colorsets" section for more
information.
* `grid [on | off]` - turns the grid overlay onor off depending on if you typed `grid on` or `grid off`.
* `edit [on | off]` - enters or exits editor mode, depending on if you typed `edit on` or `edit off`. See the "Editor" 
section for more information.
* `play` - enters play mode (the default mode with the ball on screen).
* `new` - loads a new empty level.
* `load <name>` - loads the level with the provided `<name>` from the `levels_json/` directory. See the "Saving and 
Loading" section for more information.
* `save <name>` - saves the current level to the `levels_json/` directory. See the "Saving and Loading" section for more
information.
* `exit` - exits the terminal.
* `quit` - closes out of the game (same as pressing the X button on the window).

### Zoomies Mode
This is the "debug movement" mode. You zoom around, hence the name.  

It can be turned on with `zoomies on`, and turned off with `zoomies off`.  

If it's turned on, hold down Space to zoom!

### Colorsets
Using the `color <colorset>` command, you can change the color of the current level.  
Here are the possible values for `<colorset>`:
* `bubblegum`
* `grayscale` (default)
* `neon_city`
* `neon_sewers`

For instance, `color bubblegum` will make the level have nice shades of pink.

This colorset is saved along with the rest of your level when you run the `save` command.

### Saving and Loading
You can use the `load <name>` command to load a level from the `levels_json/` directory.
It will load from the `.json` file with the given name.  

For instance, `load empty` loads the level at `levels_json/empty.json`.

The `save <name>` command allows you to save the current level to the `levels_json/` directory. If no name is provided, 
the current level name will be used instead. The level is saved to a `.json` file with the given/current level name.  

For example, if the current level is named `block`, `save` will save the current level to `levels_json/block.json`.  
As well, `save square` will save the current level to `levels_json/square.json`.

## Editor
The `edit [on | off]` command allows you to enter or exit editor mode.  
`edit` or `edit on` enters edit mode, while `play` or `edit off` exits editor mode.

### Tools
The editor has various tools to edit levels:
* `pointer` - turned on by pressing `v`. The default mode, does nothing yet.
* `rect` - turned on by pressing `r`. See more information in the `Rect Tool` section.

### Rect Tool
Pressing `r` while in `edit` mode allows you to place down rectangles that the ball can collide with.  

To start placing a rectangle, click where you wish to put one of the corners. A transparent rectangle will show up, and
you can move the cursor around to change where the rectangle's opposite corner will be.  

Once you're happy with the rectangle's opposite corner is, click again. A transparent box with two ends having thick
lines will show up. This is the rectangle you are about to place. You can edit it, though:  
* Press the space key to change the box's rotation.  
* Press the arrow keys to turn off individual sides of the box. This should only be used for aesthetic purposes, because
the box's collision won't work properly if you do this. This can, however, be used to create one-way gates.

Click once more, and the box will actually be in the level!  

To undo the creation of past boxes, hit the `u` key.

## Unfinished State of the Game
I built this in my free time during July and August 2023. This project wasn't meant to be stressful, and I could add to
it whenever I felt like it. So, the features added were the ones I had time for. While I could continue to add more
features, I've become more interested in robotics and other programming projects.

That being said, I had started to implement:
* Buttons that could trigger events
* Holes so that you could actually finish levels
* Decals that you could use to decorate levels

And I wanted to add:
* A menu
* More color palettes
* An easier-to-use way of editing, saving and loading levels
* A campaign mode

Even without these features, I hope you enjoy my little passion project!
