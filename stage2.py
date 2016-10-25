import json
import requests
import stage1 


def reverse(theStr):
	return theStr[::-1]

req = requests.post(stage1.s2ret, data = {'token':stage1.token})
string = req.text

rev = reverse(string)

answer = {'token':stage1.token, 'string':rev}

p = requests.post(stage1.s2val, data = answer)

print (p.text)