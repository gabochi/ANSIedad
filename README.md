# ANSIedad
Terminal-based vjing/livecoding program

## About
ANSIedad uses bytebeat expressions to generate visuals through the terminal. Please note that this is in a very primitive state of developing so you need some knowledge in order to make it work on your system.

<img src="https://raw.githubusercontent.com/gabochi/ANSIedad/master/screenshots/classic2.jpg?raw=true" height="250" width="250"><img src="https://raw.githubusercontent.com/gabochi/ANSIedad/master/screenshots/bitmap.jpg?raw=true" height="250" width="250"><img src="https://raw.githubusercontent.com/gabochi/ANSIedad/master/screenshots/odiseo.jpg?raw=true" height="250" width="250"><img src="https://raw.githubusercontent.com/gabochi/ANSIedad/master/screenshots/kob.jpg?raw=true" height="250" width="250"><img src="https://raw.githubusercontent.com/gabochi/ANSIedad/master/screenshots/odiseo2.jpg?raw=true" height="250" width="250"><img src="https://raw.githubusercontent.com/gabochi/ANSIedad/master/screenshots/all.jpg?raw=true" height="250" width="250">

## Requirements
* Python (tested on 2.7.17)
* Terminal (tested on *Xfce* and *Xterm*)
* Text editor (tested on *nano*)

## Run
Run `python video.py` on your terminal. The code is pretty documented in case you want to change something.
### Setup
You can set the width (*128* default) and the expressions source file (*file.exp* default) at the begining of *video.py*.
### Usage
The program reads modifications in the expressions source file and updates the visuals accordingly, so the output should change everytime you save the file. There are some bytebeat expression examples in *video.txt* you can copy and paste. *There is also a hidden message for the chosen one*.
### The expressions source file structure
The expression source file lines are evaluated as follows:
```
background color expression
foreground color expression
character number expression
```
