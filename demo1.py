#! /usr/bin/python
import os
import sys
varibleNum = float(10)
print varibleNum
variableNum1 = int(10)
print variableNum1
variableNum2 = 'Awadhesh'
print variableNum2

mySum = variableNum1 + varibleNum
print mySum
mySum1 = 'variableNum1' * 2
print mySum1

myString = 'Hello Awadhesh'
print len(myString)
print myString[2:9]


getPWDOutput = os.system('awadhesh')
print "My command status : " + str(getPWDOutput)
print "My command status : ", getPWDOutput

myNum = 20
if (myNum > 50):
	print "i got 50"
elif (myNum > 30 and myNum < 50):
	print "i m below 50"
else:
	print "i m below 30"

#myString1 = "Hello"

#if (myString1.lower() == 'hello'):
#	print "right word"
#else:
#	print "Unmatched string"


print "Demo purpose"
userInput = sys.argv[0]
print userInput
