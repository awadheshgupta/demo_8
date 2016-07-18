#! /usr/bin/python
import sys
import os

def mylen(locallist):
	varlist = 0
	for myvar in locallist:	
		varlist = varlist + 1
	print "inside function varlist : ", varlist	
	return varlist



totalinput = sys.argv
print totalinput

lengthlist = len(totalinput)
print "built-in function value : ", lengthlist

lengthlist1 = mylen(totalinput)
print "user defined function : ", lengthlist1

while (lengthlist > 0):
	print totalinput[lengthlist-1]
	lengthlist = lengthlist -1


#mylist = []
#mylist = [1, 2 , 3 ,4]

#print mylist

#for mylocalvar in mylist:
#	print "my value : ", mylocalvar
#mylist[1] = 12


#print myList
#print len(myList)
myVar = "hello"
print list(myVar)

myVarTupple = ('awadhesh', 'ashok', 10 , 12.0)
print myVarTupple
#myVarTupple[1] = "ashokaa"
print myVarTupple[1:3]

myDict = {}
myDict = {23: "hello", 12 : "hi" }
print myDict[23]
