#!/usr/bin/python

import json

def find_Daily_Programmer(data):
	returnString = ""

	if isinstance(data, unicode):
		if data == u"dailyprogrammer":
			return " "
		else:
			return returnString

	elif isinstance(data, dict):
		data = data.items()
		for i,k in data:
			try:
				iter(k)
				returnString = returnString + find_Daily_Programmer(k)
				if returnString != "":
					if returnString == " ":
						return i
					else:
						return i + " -> " + returnString
			except TypeError, te:
				pass
		return returnString

	elif isinstance(data, list):
		index = 0
		for i in data:
			try:
				iter(i)
				returnString = returnString + find_Daily_Programmer(i)
				if returnString != "":
					if returnString == " ":
						return str(index)
					else:
						return str(index) + " -> " + returnString
			except TypeError, te:
				pass
			index = index + 1
		return returnString

fileInput = raw_input()
data = json.loads(fileInput)
print find_Daily_Programmer(data)
