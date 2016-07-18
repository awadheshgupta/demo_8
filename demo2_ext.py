#! /usr/bin/python
import sys
import os
#inputNum1 = int(raw_input("Please provide first number?"))
#inputNum2 = int(raw_input("Please provide second number?"))

#total = inputNum1 + inputNum2
#print "Total of 2 number : " + str(total)

totalInput = sys.argv
print totalInput
index = 0
for localVar in totalInput:
	print "Index " + str(index) + " : " + localVar
	index = index + 1
	
	if (localVar.lower() == 'ashok'):
		print "Got user : " + localVar
		break
myNum = 1
while (myNum < 11):
	print myNum
	myNum = myNum + 1

#ls /home/awadhesh/pythonDemo | wc -l

folderPath = raw_input ("Please provide absolute path : ")
print folderPath

#commandVar = "ls " + folderPath + " | wc -l"
#print commandVar
#retVar = os.system(commandVar)
#if (retVar !=0):
#	print "Please check folder path"
#else:
#	print "Got final count"


#ls /folderpath > /tmp/myInputFile
#open open/read /tmp/myInputFile
# use for loop to get count

myCommand = "ls " + folderPath + " > /tmp/myInputFile"
print myCommand
retVal = os.system(myCommand)
if (retVal != 0):
       print "Please check folder path"
       exit()


myContent = open('/tmp/myInputFile')
count = 0
for mylocalVar in myContent:
	count = count + 1


print "Total Count", count


