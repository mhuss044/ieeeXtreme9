# Zoom In 
'''
Problem Statement
Some years ago, we had terminals that were capable of supporting only ASCII characters. We would like your help to construct a program, which given an input string and specific printing rules, produces the same text in a bigger layout.

Input Format

On the first line of input is an integer n, 1 <= n <= 100, representing how many columns each character will use when printed "zoomed-in".

The next line contains an integer m, 1 <= m <= 100, representing how many rows each character will use when printed "zoomed-in". Note that n and m are not necessarily equal.

The third line contains an integer k, 3 <= k <= 95, which indicates how many characters may need to be translated.

Following these first lines, are k descriptions of the "zoomed-in" characters, formatted as follows:

    On a line by itself, a single character, which has an ASCII value of between 32 and 126, inclusive

    m lines, each containing n characters, that give the "zoomed-in" representation of the character on the previous line

Following the descriptions of the zoomed in characters, is an integer number x, 1 <= x <= 500.

Finally there are x lines, each containing a string of up to 2,000 characters, and ending with a new line. The characters in this string will be chosen from the set of k characters previously specified.

Notes:

    We don't know if k sets (i.e. the descriptions of the k "zoomed-in" characters) are given in a sorted or random order.

    The "zoomed-in" version of an empty string is m blank lines (i.e. lines with only a newline character).


print "ge"
print "gg:%d, %s, %s" % (n+2, v, var)

from sys import argv

for i in argv:
	print "%r\n" % i

cat input.in | python digitFun.py
'''

import sys

# character class; contains definition of zoomed in character
class chDef(object):
	def __init__(self, dR):
		self.charDefR = dR	# rows of char, storage of string
	def printRow(self, beg, end):	# Print row of char def
		sys.stdout.write(self.charDefR[beg:end])
#print self.charDefR[beg:end],
	def add(self, s):	# add to char def
		self.charDefR += s.rstrip('\r\n')
	
charDict = {}  
chList = []
chDefList = []

numCol = int(raw_input())	# num cols a char will take when zoomed in
numRow = int(raw_input())	# num row a char will take when zoomed in
numChar = int(raw_input())	# num chars to zoom in

# read char descs
x = 0
while x < numChar:
	chList.append(raw_input())	# char def for ch char
	chDefList.append(chDef(""))	# add new chDef, fill it:	
	for i in range(0, numRow):
		chDefList[x].add((raw_input()).rstrip('\r\n'))
	charDict[chList[x]] = chDefList[x]	# setup dict
	x+=1

# Get num lines to zoom:
numLines = int(raw_input())

while numLines > 0:
	# Read phrase to zoom in:
	phrase = raw_input()	

	'''
	print charDict,"\n"
	print chList,"\n"
	print chDefList,"\n"
	print phrase,"\n"

	for r in range(0, numChar):
		sys.stdout.write(str(len(chDefList[r].charDefR))+':'+chDefList[r].charDefR+'\n')
	sys.stdout.write('\n')
	'''

	# Zoom in:
	for r in range(0, numRow):
		for n in range(0, len(phrase)): 	
			charDict[phrase[n]].printRow(numCol*r, (numCol*r)+numCol)
		sys.stdout.write('\n')
	numLines -= 1;


