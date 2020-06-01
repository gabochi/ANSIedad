from editme import *
from sys import stdout
from time import sleep
from os.path import getmtime

SOURCE_FILE = "editme.py"

t = 0
MOD_TIME = 0
BG = "0"
FG = "0"
CH = "0"

WIDTH = 64
LINES = 16
SLEEP = 0

stdout.write("\033[2J")

while True:	

	if t%WIDTH == 0:
		stdout.write("\n")
		sleep(SLEEP)

	if t%(WIDTH*LINES) == 0:
		print ("\033[0;0f")

	if MOD_TIME != getmtime(SOURCE_FILE):
		exec(open(SOURCE_FILE).read())
		MOD_TIME = getmtime(SOURCE_FILE)

	try:
		BG_EXPR = eval(BG)%256
		BG_OUT = "\033[48;5;%dm" % BG_EXPR
		stdout.write(BG_OUT)

		FG_EXPR = eval(FG)%256
		FG_OUT = "\033[38;5;%dm" % FG_EXPR
		stdout.write(FG_OUT)

		CH_EXPR = eval(CH)%64+32
		CH_OUT = chr(CH_EXPR)
		stdout.write(CH_OUT)

	except:
		pass
	
	t+=1