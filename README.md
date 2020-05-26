# ANSIedad

ANSIedad uses bytebeat technique -first developed by [viznut](http://viznut.fi/en/)- to generate ASCII visuals through a terminal emulator using ANSI escape codes for color. Therefore, the visual effects are similar to [IBNIZ](https://github.com/viznut/IBNIZ) and, in this case, the expressions use *infix* notation by default.

<img src="https://raw.githubusercontent.com/gabochi/ANSIedad/master/screenshots/mux.png?raw=true">

## Install

Clone or download this repo. You'll need, at least, **Python** and a **terminal emulator** to run the program. Although there are many ways in almost any OS to play with it, there are two simple script files (*new.sh* and *mux.sh*) that you can run right away in Linux to get the idea (this assuming you have *tmux* and *nano* also installed). If not, keep reading.

## Usage

The program takes a source file with bytebeat expressions to generate the visuals. Any time that the source file is modified (when saving the changes), the output will update accordingly. You must specify *width* and *source file* as arguments when runing the program. This is an example, try this in your terminal:

`python video.py 128 new.ansiedad`

This runs the program with *new.ansiedad* as source file in 128 *width*. Width is the length of the string before the carriage return, this will crucially affect the output and the speed. For optimal results try, of course, powers of two: 64, 128, 256, 512, etc. Lines in the source file are evaluated as follows:

line|evaluated as...
---|---
1|background color
2|foreground color
3|character number

## Examples

There are many examples in */examples*, don't hesitate to experiment with them since there are backups in */backup*.

## ¿What is bytebeat? ¿How can I understand all these rare expressions?

Bytebeat takes *time* (`t`) as a variable and apply basic logic and math in a single expression to generate an aesthetic output. You must know that a *byte* is 'made of' *8 bits*, eight binary digits, each one being 0 or 1:

`0000 0000` This is a byte,
`1001 1101` here's another.
`0000 0001` This = decimal ONE
`0000 0010` TWO
`0000 0011` THREE

You're ready!

### Modulo

`t % 16`
Think of *modulo* (`%`) as a 'looper'. This expression will truncate *time* on the first 16 values. You can try different lenghts and see what happens. In fact, there is an implicit `%256` for the entire expression. Try just `t` and you'll notice that, although *time* keeps growing and values above the byte (`1111 1111` = decimal 255) are not valid, there is no error because the result is always confined to the byte (a decimal 256 result will be truncated to 0, 257 to 1 and so on and so on).

*Exercise: Combine two or more loops with basic math operators...*

```
t%16 + 240
t%16 + t%6
t%2 * t%17
t%2 * t%17 + 7
t%255 + t
```

### Shifting

`t>>8`
`t<<2`
Shift moves bits *X* possitions to the right `>>` or left `<<`. This is like dividing or multiplying by powers of two.

|expression|binary|decimal
|:---:|:---:|:---:
`t`|0100|4
`t>>1`|0010|2
`t<<1`|1000|8

Practically speaking, shifting will 'accelerate/skip' or 'delay/hold' *time*. There are more advanced uses like *sequencing* but let's keep it simple for now.

*Exercise: Combine with modulo and math...*

```
(t<<1) + (t>>10)
(t>>3) %3
(t%10) + (t>>10)
```

### Logic

`t & 101`
`t ^ t+1`
`t | 179`

This three basic bitwise operators will spice up your expression. [Here](https://en.wikipedia.org/wiki/Bitwise_operation#Bitwise_operators) you have an exhaustive and very useful explanation with graphic representation. But, for the spirit of computation, let's brief anyway:

##### **AND** 
###### = 1 if *both* compared bits are 1:

1010
0110
&
0010

`10 & 6 = 2`

Note that *AND will never give a value above the lower operand*.

##### **OR**
###### = 1 if *any* of the compared bits is 1:

1010
0110
|
1110

`10 | 6 = 14`

Note that *OR will return 1 in any case but the zero/zero case*.

##### **XOR**
###### = 1 when *just one* of the compared bits is 1:

1010
0110
^
1100

`10 ^ 6 = 12`

*Exercise: put all this together and take a look at the examples!*

```
( t<<7 ) % 257 | 2020 - (t<<3) %36
( t>>6 & 68 ) *t **3 + (t>>9)
( t*(t>>9) | 191 ) * (t>>16)

```

