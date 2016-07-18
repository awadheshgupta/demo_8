#! /usr/bin/python

import sys
import os

def myLenAndPrint(localInput):
	print localInput
	print len(localInput)


userAllInput = sys.argv
#print userAllInput
#print len(userAllInput)
myLenAndPrint(userAllInput)

myOwnList = ['hello', 'world']

#print myOwnList
#print len(myOwnList)
myLenAndPrint(myOwnList)

myOwnList[0] = 'Hi'
myOwnList[1] = "Awadhesh"
print myOwnList

myOwnTupple = ('Hello', 'Ashok')

#print myOwnTupple

#print len(myOwnTupple)
myLenAndPrint(myOwnTupple)

mydict = {}

mydict = {23 : "Awadhesh Gupta", 25: "Devops"}

print mydict[23]
print mydict[25]
mydict[25] = "India abc cde fgh"
print mydict

print localInput



