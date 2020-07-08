from editme import *
from unicodes import *

import sys
from time import sleep
from os.path import getmtime

SOURCE_FILE = "editme.py"

t = 0
MOD_TIME = 0

# mode
m = 0

# background
b = "0"

# foreground
f = "0"

# character
c = "0"

# width (columns)
w = 64

# lines
l = 16

# sleep
s = 0

sys.stdout.write("\033[2J")

while True:

	if t%w == 0:
		sys.stdout.write("\n")
		sleep(s)

	if ((t%(w*l) == 0) & (m ==0 )) :
		sys.stdout.write ("\033[0;0f")

	if MOD_TIME != getmtime(SOURCE_FILE):
		exec(open(SOURCE_FILE).read())
		MOD_TIME = getmtime(SOURCE_FILE)

	try:
		BG_EXPR = eval(b)%256
		BG_OUT = "\033[48;5;%dm" % BG_EXPR
		sys.stdout.write(BG_OUT)

		FG_EXPR = eval(f)%256
		FG_OUT = "\033[38;5;%dm" % FG_EXPR
		sys.stdout.write(FG_OUT)

		CH_EXPR = eval(c)%224
		CH_OUT = uni[CH_EXPR]
		sys.stdout.write(CH_OUT)

	except:
		pass

	t+=1
