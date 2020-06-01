# ANSIedad

ANSIedad uses bytebeat technique -first developed by [viznut](http://viznut.fi/en/)- to generate aesthetic visuals through a terminal emulator using ANSI escape codes. Therefore, the visual effects are similar to [IBNIZ](https://github.com/viznut/IBNIZ).

<img src="https://raw.githubusercontent.com/gabochi/ANSIedad/master/demo.gif?raw=true">

You can try [ansiedad-editor](https://github.com/coolantleak/ansiedad-editor), a web based version made by coolantleak.

## Install

Clone or download this repo. You'll need, at least, **Python** and a **terminal emulator** to run the program. Although there are many ways in almost any OS to play with it, there is a simple `script.sh` file you can run immediately assuming you are on Linux and have *tmux* and *nano* editor. If not, keep reading...

## Usage

The program is `runme.py` and takes `editme.py` as source file for bytebeat expressions. When saving the changes in the source file, the visual output will update accordingly. To start the program run:

`python3 runme.py`

Then, you can edit `editme.py` on your favorite text editor and follow the instructions.
To change the visual effects and configure the program there are some reserved variables:

Variable|Action
:---:|:---:
BG|background color
CH|character code
FG|foreground color
LINES|rows (default 16)
WIDTH|columns (default 64)
SLEEP|delay time (default 0)

## Examples

There are further instructions and examples in the source file. Experiment freely, there is a backup: `editme.backup`.

## What is bytebeat? How can I understand all these rare expressions?

Bytebeat takes *time* (`t`) as a variable and applies basic logic and math in a single expression to generate an aesthetic output. You must know that a *byte* is 'made of' *8 bits*, eight binary digits, each one being 0 or 1:

```
0000 0000 => a byte
1001 1101 => another
0000 0001 => decimal ONE
0000 0010 => decimal TWO
0000 0011 => decimal THREE
```

You're ready!

### Modulo

```
t % 16
```

Think of *modulo* (`%`) as a 'looper'. This expression will truncate *time* on the first 16 values. You can try different lengths and see what happens. In fact, there is an implicit `%256` for the entire expression. Try just `t` and you'll notice that, although *time* keeps growing and values above the byte (`1111 1111` = decimal 255) are not valid, there is no error because the result is always confined to one byte (a decimal 256 result will be truncated to 0, 257 to 1 and so on and so on).

*Exercise: Combine two or more, add, multiply...*

```
t%16 + 240
t%16 + t%6
t%2 * t%17
t%2 * t%17 + 7
t%255 + t
```

### Shifting

```
t>>8
t<<2
```

Shift moves bits *X* possitions to the right `>>` or left `<<`. This is like dividing or multiplying by powers of two.

|expression|binary|decimal
|:---:|:---:|:---:
`t`|0100|4
`t>>1`|0010|2
`t<<1`|1000|8

Practically speaking, shifting will 'accelerate/skip' or 'delay/hold' *time*. There are more advanced uses like *sequencing* but let's keep it simple for now.

*Exercise: Combine with math...*

```
(t<<1) + (t>>10)
(t>>3) %3
(t%10) + (t>>10)
```

### Logic

```
t & 101
t ^ t+1
t | 179
```

These three basic bitwise operators will spice up your expression. [Here](https://en.wikipedia.org/wiki/Bitwise_operation#Bitwise_operators) you have an exhaustive and very useful explanation with graphic representation. But, for the spirit of computation, let's brief anyway:

##### **AND** 
###### = 1 if *both* compared bits are 1:


|||
:---:|:---:
||1010
&|0110
=|0010

`10 & 6 = 2`

Note that *AND will never give a value above the lower operand*.

##### **OR**
###### = 1 if *any* of the compared bits is 1:

|||
:---:|:---:
||1010
\||0110
=|1110

`10 | 6 = 14`

Note that *OR will return 1 in any case but the zero/zero case*.

##### **XOR**
###### = 1 when *just one* of the compared bits is 1:

|||
:---:|:---:
||1010
^|0110
=|1100

`10 ^ 6 = 12`

*Exercise: put all this together and take a look at the examples!*

```
t<<1 | t>>5
t>>1 ^ t<<6
t<<1 ^ t>>4
t<<3 ^ t>>1
(t<<3 ^ t>>2) & 1000
( t<<7 ) % 257 | 2020 - (t<<3) %36
( t>>6 & 68 ) *t **3 + (t>>9)
( t*(t>>9) | 191 ) * (t>>16)

```

