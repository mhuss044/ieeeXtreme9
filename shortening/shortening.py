# Shortening 
'''
Problem Statement
	Shorten url

print "ge"
print "gg:%d, %s, %s" % (n+2, v, var)

from sys import argv

for i in argv:
	print "%r\n" % i

cat input.in | python digitFun.py
'''

import sys
'''
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]

#s = "0x0a470c00025f424a"
#i = int(s)
i = 740573857905066570
base62Num = numberToBase(i, 62)

print base62Num
print ord('Z')-29
print ord('z')-87

s=""

for i in range(0, len(base62Num)):
	if base62Num[i] >= 10 and base62Num[i] <= 35:
		s += str(unichr(base62Num[i]+87))
	elif base62Num[i] >= 36 and base62Num[i] <= 61:
		s += str(unichr(base62Num[i]+29))
	else:
		s += str(base62Num[i])

print s
'''

# Read base url:
baseURL = raw_input()
# utf-8 of base;
uBaseURL = unicode(baseURL, "utf-8")
# Read num urls to shorten
numURLs = int(raw_input())

# Shorten URL:
while numURLs > 0:
	# Read url to shorten:
	targetURL = raw_input()
	# convert to unicode
	uTargetURL = unicode(targetURL, "utf-8")
	# ensure that both strings are the same length before xor:
	if len(uTargetURL > uBaseURL):
		dif = len(uTargetURL) - len(uBaseURL)
		uBaseURL += uBaseURL[0:dif]
	elif len(uBaseURL) > len(uTargetURL):
		uBaseURL = uBaseURL[0:len(uTargetURL)]
	# XOR base and target unicode strings:
	for i in range(0, len(uBaseURL)):
		xored += str(int(uBaseURL[i]) ^ int(uTargetURL[i]))
	# take last 8 bytes:
	shortURL = xored[-8:len(xored)]	
	# convert to unsigned int:
	unInt = int(shortURL)


	sys.stdout.write(shortURL + '\n')
	numURLs -= 1
'''
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

	print charDict,"\n"
	print chList,"\n"
	print chDefList,"\n"
	print phrase,"\n"

	for r in range(0, numChar):
		sys.stdout.write(str(len(chDefList[r].charDefR))+':'+chDefList[r].charDefR+'\n')
	sys.stdout.write('\n')

	# Zoom in:
	for r in range(0, numRow):
		for n in range(0, len(phrase)): 	
			charDict[phrase[n]].printRow(numCol*r, (numCol*r)+numCol)
		sys.stdout.write('\n')
	numLines -= 1;

'''
