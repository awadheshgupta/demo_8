#! /usr/bin/python
import sys
import os

userAllInput = sys.argv
print userAllInput
#print "Number of argument ", len(sys.argv)
#print "Argument list : ", str(sys.argv)
index = 0
for localVar in sys.argv:
	print "Index" + str(index) + " :" + localVar
	if (localVar == "cow"):
		print "Length of string 'COW' : ", len(localVar)
	else:
		print "I am not in mood to do anything"
	index = index + 1

num = 1
while num < 2:
	print num
	if (num == 2):
		print "Completed my loop"
	else:
		print "Still have to go long way"
	num = num + 1

print "Done"


folderName = raw_input("Please provide folder abosulte path:")
#os.system('ls | wc -l')
cmd = 'ls ' + folderName + ' > /tmp/output'
print cmd
outputCD = os.system(cmd)
if (outputCD != 0):
        print "Path does not exists"
        exit
txt = open('/tmp/output')
myIndex = 0
for myFile in txt:
	print "FileName : ", myFile
 	myIndex = myIndex + 1


print "Total Count : ", myIndex
