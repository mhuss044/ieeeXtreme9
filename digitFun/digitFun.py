# Digit Fun
'''
Problem Statement

Recurrence relations are an important tool for the computer scientist. Many algorithms, particularly those that use divide and conquer, have time complexities best modeled by recurrence relations. A recurrence relation allows us to recursively define a sequence of values by defining the nth value in terms of certain of its predecessors.

Many natural functions, such as factorials and the Fibonacci sequence, can easily be expressed as recurrences. The function of interest for this problem is described below.

Let |An| denote the number of digits in the decimal representation of An. Given any number A0, we define a sequence using the following recurrence:

Ai = |Ai-1| for i > 0

The goal of this problem is to determine the smallest positive i such that Ai = Ai-1.

Input Format

Input consists of multiple lines, each terminated by an end-of-line character. Each line (except the last) contains a value for A0, where each value is non-negative and no more than a million digits. The last line of input contains the word END.

Output Format

For each value of A0 given in the input, the program should output one line containing the smallest positive i such that Ai = Ai-1.

Explanation

The first input value is A0 = 9999, resulting in A1 = |9999| = 4. Because 4 does not equal 9999, we find A2 = |A1| = |4| = 1. Since 1 is not equal to 4, we find A3 = |A2| = |1| = 1. A3 is equal to A2, making 3 the smallest positive i such that Ai = Ai-1.

The second input value is A0 = 0, resulting in A1 = |0| = 1. Because 0 does not equal 1, we find A2 = |A1| = |1| = 1. A2 is equal to A1, making 2 the smallest positive i such that Ai = Ai-1.

The third input value is A0 = 1, resulting in A1 = |1| = 1. A1 is equal to A0, making 1 the smallest positive i such that Ai = Ai-1.

The last input value is A0 = 9999999999, resulting in A1 = |9999999999| = 10. Because 10 does not equal 9999999999, we find A2 = |A1| = |10| = 2. Since 2 is not equal to 10, we find A3 = |A2| = |2| = 1. Since 1 is not equal to 2, we find A4 = |A3| = |1| = 1. A4 is equal to A3, making 4 the smallest positive i such that Ai = Ai-1.
print "ge"
print "gg:%d, %s, %s" % (n+2, v, var)

from sys import argv

for i in argv:
	print "%r\n" % i

cat input.in | python digitFun.py
'''

while True:
	v = raw_input()
	if v.isdigit() == False: # isdigit true if string is only digits, or can if v == "END":
		break	
	 
	x = 0
	while True:
#	i != int(v):
		i = len(v)
		if i == int(v):
			break
		v = str(i)
		x += 1
	
	print x+1


