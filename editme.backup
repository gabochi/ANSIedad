# Hi there, welcome to ANSIedad by gabochi!
# I will give you the basics to have some ANSI fun...

# To try the examples just comment/uncomment the lines with assignations and save the file

#BG="1";CH="31";FG="7"	# These are the three main expressions: background, character and foreground.
			# You can use ; optionally to concatenate them in a single line.

# 't' is for time, an always increasing counter that you'll operate to generate the visual effects.

#BG = "t >> 11";FG="0";CH="0" # Bitshifts speed up or down time by powers of two

#CH = "t % 8";BG="0";FG="15" # Modulo 'loops' time n steps

# Nice, but the magic ingredient for expressions are bitwise logic operators, see:

#BG="t & 10"; CH ="t ^ t-1"; FG = "t | 127"
#BG="t<<5 & t>>1"; CH="0"
#BG="t<<5 | t>>1"; CH="0"
#BG="t<<5 ^ t>>1"; CH="0"

# Let's dance!

#BG="t%257 & t<<5" ; CH = "0"
#BG="t%255 | t<<5" ; CH = "0"
#BG="t%257 ^ t<<5" ; CH = "0"

# If you need some curves try 't*t' style expressions:

#BG= "(t*t>>17)%16+240" ; CH="10" ; FG="(t*t>>16)%16+240"
#BG="2";CH="144"; FG="t * t>>13 &20"
#BG="t*(t+(t>>9)) >>10 & 1";CH="0"; FG="0"

#BG="t >> 0xE"; CH= "144+t % 0b110"; FG = "t<< 0b11" # Binary (0b) and hex (0x) notation are allowed

# Choose the characters wisely

#BG="7";FG="0";CH="t|222"
#CH="222*((t*t>>(9+t%2))%2)+(188+(t>>(t>>10)%15)%4)"
#CH="144+(t^(t>>8))%4"
#BAR="/\\";BG="7";FG="0";CH="ord(BAR[(t*t>>9)%2])-32"

# Bitmap and text bonus track

# 0001 0011 0101 0101
# 0001 0010 0101 0111
# 0000 0001 0101 0101
# 0001 0011 0110 0010

#BYE = "ANSIedad...."; BITMAP = 0b0001001101010101000100100101011100000001010101010001001101100010
#BG ="BITMAP >> ((t>>1)+(t>>10))%16 + (t>>7)%4*16 & 1 ^ (t>>9)%2 * t<<2" ; FG = "t&1"; CH = "(t%512<64)*(ord(BYE[t%12])-32)"


