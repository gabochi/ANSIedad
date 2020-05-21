# ANSIedad
Terminal-based vjing/livecoding program

## About
ANSIedad uses bytebeat expressions to generate visuals through the terminal. Please note that this is in a very primitive state of developing so you need some knowledge in order to make it work on your system.

![asd](sreenshots/cassic.jpg)

## Requirements
* Python (tested on 2.7.17)
* Terminal (tested on Xfce 0.8.7.4)
* Text editor

## Run
Run `python video.py` on your terminal. If it doesn't work change the escape codes in *video.py*, you'll probably need to replace `:` with `;`. The code is pretty documented.
### Setup
You can set the width and other things at the begining of *video.py*. Notice that you have the possibility of working with characters and front color too, just comment or uncomment the proper lines in the code.
### Usage
The program reads modifications in *expr.py* (the source file can be changed too) and updates the bytebeat expression which generates the visuals accordingly. There are some bytebeat expression examples in *video.txt* but please remember that **carry returns in *expr.py* tend to give an error**, so avoid them until I fix it. Also, if an expression does not update as expected, try saving the file several times (see *try/except* in the code).
