#!/usr/bin/python

# ANSIedad
# gabochi.github.io

from os.path import getmtime
import sys

				# setup width and expressions source file from arguments
WIDTH = int(sys.argv[1])
EXPR_FILE = sys.argv[2]

				# init other variables
BG_EXPR = " "
FG_EXPR = " "
CH_EXPR = " "
MOD_TIME = 0

t = 0 				# init bytebeat counter

def updateExpressions():	# define update expressions function

	global EXPR_FILE, BG_EXPR, FG_EXPR, CH_EXPR, MOD_TIME	# dont do this at home

	with open(EXPR_FILE,"r") as FILE:
		BG_EXPR = FILE.readline()
		FG_EXPR = FILE.readline()
		CH_EXPR = FILE.readline()
		MOD_TIME = getmtime(EXPR_FILE)
	return

updateExpressions()

while True:

	if getmtime(EXPR_FILE) != MOD_TIME: updateExpressions() # update expressions if the file change

	t+=1							# increase bytebeat counter

	try:
		CH = chr(eval(CH_EXPR)%94+32)			# set character
		BG = "\x1b[48;5;%dm" % (eval(BG_EXPR)%256)	# set escape code for 8-bit bg color
		FG = "\x1b[38;5;%dm" % (eval(FG_EXPR)%256)	# set escape code for 8-big fg color

	except:
		pass

	if t%WIDTH==0: print("")				# carriage return

	sys.stdout.write(BG)					# print bg escape code
	sys.stdout.write(FG)					# print fg escape code
	sys.stdout.write(CH)					# print character
