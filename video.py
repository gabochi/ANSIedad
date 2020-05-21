# ANSIedad
# gabochi.github.io

from os.path import getmtime
import sys

# setup

EXPR_FILE = "expr.py" 
WIDTH = 128
EXPR = "t>>8&t"

t = 0

MOD_TIME = getmtime(EXPR_FILE)	# get file modification time

while True:

	if getmtime(EXPR_FILE) != MOD_TIME:		# update expression if the file is modified
		with open(EXPR_FILE,"r") as FILE:
			EXPR = FILE.readline()
			MOD_TIME = getmtime(EXPR_FILE)
	
	t+=1	# increase time in 1

	try:
		CHAR = chr(eval(EXPR)%64+32)			# set character

# these escape codes work on xfce4-terminal 0.8.7.4, you'll probably need to replace ':' for ';'

		ESCAPE="\x1b[48:5:%dm" % (eval(EXPR)%256)	# set escape code for 8-bit bg color
#		ESCAPE="\x1b[38:5:%dm" % (eval(EXPR)%256)	# set escape code for 8-big fg color

	except:
		pass

	if t%WIDTH==0: print("")	# CR

	sys.stdout.write(ESCAPE)	# print escape code
#	sys.stdout.write(" ")		# print blank space
	sys.stdout.write(CHAR)		# print character
