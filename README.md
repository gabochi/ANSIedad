# ANSIedad
Terminal-based vjing/livecoding program

## About
ANSIedad uses bytebeat expressions to generate visuals through the terminal.

<img src="https://raw.githubusercontent.com/gabochi/ANSIedad/master/screenshots/loom.png?raw=true">

## Requirements
* Python (tested on 2.7.17 and 3.6.9)
* Terminal emulator (so far it worked on most, Linux and Windows, *not cmd.exe*)
* Text editor

## Install
Clone or download this repo. Open your terminal and try this command:

`python video.py 128 examples/test.ansiedad`

That should work.

## Usage
The first argument of the program (`128`) is the width. The second (`examples/test.ansiedad`) is the source file that the program will evaluate to generate the visuals. The visuals will update accordingly if the file is modified.

## Examples
Mess with the examples and don't worry, there is a backup of them in the *backup* folder.

## Bytebeat
ANSIedad uses bytebeat expressions. Lines of the source file are evaluated as follows:

line|evaluated as...
---|---
1|background color
2|foreground color
3|character number

