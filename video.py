#!/usr/bin/python

# ANSIedad
# gabochi.github.io

from os.path import getmtime
from sys import stdout, argv
from time import sleep
								# setup width and source file from arguments
WIDTH = int(argv[1])
EXPR_FILE = argv[2]

try:								# optional argument, delay per line
	DELAY=float(argv[3])
except:
	DELAY=0
								# init other variables
BG_EXPR = " "
FG_EXPR = " "
CH_EXPR = " "
MOD_TIME = 0
CH = ""
BG = ""
FG = ""

t = 0				 				# init bytebeat counter

while True:

	t+=1							# increase bytebeat counter

	try:
		CH = chr(eval(CH_EXPR)%94+32)			# set character
		BG = "\x1b[48;5;%dm" % (eval(BG_EXPR)%256)	# set escape code for 8-bit bg color
		FG = "\x1b[38;5;%dm" % (eval(FG_EXPR)%256)	# set escape code for 8-big fg color
	except:
		pass

	stdout.write(BG)					# print bg escape code
	stdout.write(FG)					# print fg escape code
	stdout.write(CH)					# print character

	if t%WIDTH==0: 						# carriage return and check for updates
		print("")

		if getmtime(EXPR_FILE) != MOD_TIME:		# update expressions if the file change

			with open(EXPR_FILE,"r") as FILE:
				BG_EXPR = FILE.readline()
				FG_EXPR = FILE.readline()
				CH_EXPR = FILE.readline()
				MOD_TIME = getmtime(EXPR_FILE)

		sleep(DELAY)					# optional delay time per line