#!/usr/bin/python

# ANSIedad
# gabochi.github.io

from os.path import getmtime
import sys

# setup width and expressions source file
WIDTH = 128
EXPR_FILE = "file.exp"

# init other variables
BG_EXPR = " "
FG_EXPR = " "
CH_EXPR = " "
MOD_TIME = 0

# init bytebeat counter
t = 0

# define update expressions function
def updateExpressions():

	global EXPR_FILE, BG_EXPR, FG_EXPR, CH_EXPR, MOD_TIME
	# dont do that at home

	with open(EXPR_FILE,"r") as FILE:
		BG_EXPR = FILE.readline()
		FG_EXPR = FILE.readline()
		CH_EXPR = FILE.readline()
		MOD_TIME = getmtime(EXPR_FILE)
	return

updateExpressions()

while True:

	# update expressions if the file change
	if getmtime(EXPR_FILE) != MOD_TIME: updateExpressions()

	t=t+1

	try:
		CH = chr(eval(CH_EXPR)%94+32)
		# set character
		BG = "\x1b[48;5;%dm" % (eval(BG_EXPR)%256)
		# set escape code for 8-bit bg color
		FG = "\x1b[38;5;%dm" % (eval(FG_EXPR)%256)
		# set escape code for 8-big fg color

	except:
		pass

	# carriage return
	if t%WIDTH==0: print("")

	# print bg escape code
	sys.stdout.write(BG)
	# print fg escape code
	sys.stdout.write(FG)
	# print character
	sys.stdout.write(CH)
