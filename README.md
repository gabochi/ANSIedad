# ANSIedad
Terminal-based vjing/livecoding program

## About
ANSIedad uses bytebeat expressions to generate visuals through the terminal.

<img src="https://raw.githubusercontent.com/gabochi/ANSIedad/master/screenshots/mux.png?raw=true">

## Requirements
* Python (tested on 2.7.17 and 3.6.9)
* Terminal emulator (so far it worked on most, Linux and Windows, *not cmd.exe*)
* Text editor

## Install
Clone or download this repo. If you're on Linux, open your terminal and try this command:

`./new.sh`

If not, read the following section or change the script (it assumes that you have *nano* and *tmux* on your system).

## Usage
You can always run the program manually like this:

`python video.py 128 examples/test.ansiedad`

The first argument of the program (`128`) is the width. The second (`examples/test.ansiedad`) is the source file that the program will evaluate to generate the visuals. The visuals will update accordingly if the file is modified (that means, each time you *save* the file).

## Examples
Mess with the examples, don't worry about breaking something... that's why there is a *backup* folder.

## Bytebeat
ANSIedad uses bytebeat expressions. Lines in the source file are evaluated as follows:

line|evaluated as...
---|---
1|background color
2|foreground color
3|character number

## mux
There is a simple *mux.sh* script file just to give you some ideas, improove it, customize, make your own script according to your system and preferences and share!

`tmux new-session python video.py 128 examples/awesome.ansiedad \; split-window -h python video.py 128 examples/odiseo.ansiedad \; split-window nano examples/awesome.ansiedad \; split-window nano examples/odiseo.ansiedad`

---

Thanks for trying ANSIedad, I'll upload more documentation soon.
