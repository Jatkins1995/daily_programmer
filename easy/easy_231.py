#!/usr/bin/python

def printer(inputList):
	for i in range (0,10000):
		toPrint = "".join(inputList)
		print toPrint.replace('1', 'x').replace('0', ' ')
		inputList = modify(inputList)

def modify(inputList):
	oldinputList = list(inputList)
	count = len(inputList)
	for i in range(0,count):
		#  The operation here is (A^B) ^ (A^C) where BAC is a sequence in the inputList. ^ <- is XOR
		if i == count-1:
			inputList[i] = chr( (int(oldinputList[i])^( int(oldinputList[i-1]))) ^ (int(oldinputList[i])^(int(oldinputList[0]))) + 48 )
		else:
			inputList[i] = chr( (int(oldinputList[i])^( int(oldinputList[i-1]))) ^ (int(oldinputList[i])^(int(oldinputList[i+1]))) + 48 )
	return inputList

#inputList = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
inputString = "00000000001000000000010000000000100000000001000000000010000000000"
inputList = list(inputString)
printer(inputList)