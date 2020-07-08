# Hi there, welcome to ANSIedad by gabochi!
# I will give you the basics to have some ANSI fun...

# To try the examples just comment/uncomment the lines with assignations and save the file

#b="1";c="31";f="7"	# These are the three main expressions: background, character and foreground.
			# You can use ; optionally to concatenate them in a single line.

# 't' is for time, an always increasing counter that you'll operate to generate the visual effects.

#b = "t >> 11"; f="0"; c="0" # Bitshifts speed up or down time by powers of two

#c = "t % 8"; b="0"; f="15" # Modulo 'loops' time n steps

# Nice, but the magic ingredient for expressions are bitwise logic operators, see:

#b="t & 10"; c ="t ^ t-1"; f = "t | 127"
#b="t<<5 & t>>1"; c="0"
#b="t<<5 | t>>1"; c="0"
#b="t<<5 ^ t>>1"; c="0"

# Let's dance!

#b="t%257 & t<<5" ; c = "0"
#b="t%255 | t<<5" ; c = "0"
#b="t%257 ^ t<<5" ; c = "0"

# If you need some curves try 't*t' style expressions:

#b= "(t*t>>17)%16+240" ; c="10" ; f="(t*t>>16)%16+240"
#b="2"; c="144"; f="t * t>>13 &20"
#b="t*(t+(t>>9)) >>10 & 1";CH="0"; FG="0"

#b="t >> 0xE"; c= "144+t % 0b110"; f = "t<< 0b11" # Binary (0b) and hex (0x) notation are allowed

# Choose the characters wisely

#b="7";f="0";c="t|222"
#c="222*((t*t>>(9+t%2))%2)+(188+(t>>(t>>10)%15)%4)"
#c="144+(t^(t>>8))%4"
#BAR="/\\"; b="7";f="0";c="ord(BAR[(t*t>>9)%2])-32"

# Bitmap and text bonus track

# 0001 0011 0101 0101
# 0001 0010 0101 0111
# 0000 0001 0101 0101
# 0001 0011 0110 0010

#BYE = "ANSIedad...."; BITMAP = 0b0001001101010101000100100101011100000001010101010001001101100010
#b ="BITMAP >> ((t>>1)+(t>>10))%16 + (t>>7)%4*16 & 1 ^ (t>>9)%2 * t<<2" ; f = "t&1"; c = "(t%512<64)*(ord(BYE[t%12])-32)"

# Remember you can change dimensions (w/l) and mode (m) too... Have fun ;)
