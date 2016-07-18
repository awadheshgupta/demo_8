#! /usr/bin/python
import os
import sys
myFirstVariable =  "Hello world"
myFirstNum = str(10)
mySecondNum = str(20)
myThirdNum = 20
myFourthNum = 20
print "Print my first value : " + myFirstVariable
print "print my first num", myFirstNum
total = myThirdNum * myFourthNum
print "Total of my numbers : " + str(total)
totalStr = myFirstNum + mySecondNum
print totalStr
myNewStr1 = "Hi"
myNewStr2 = "Ashok"
concatenationStr = myNewStr1 + myNewStr2
print concatenationStr
print "Hello" * 3
commandVariable = 'abc'
output = os.system(commandVariable)
print "Command " + commandVariable + " output : " + str(output)
if (output == 0):
	print "Successful command"
elif (output == 256):
	print "Unsccessful mkdir command"
else:  
	print "Unsccessful command"

myString1 = "HeLllo"

if (myString1.lower() == 'hello'):
        print "right word"
else:
        print "Unmatched string"

inputVariable = raw_input("Please provide your number?")
print "my number : " , inputVariable

inputCommandline = sys.argv[0]
print inputCommandline
