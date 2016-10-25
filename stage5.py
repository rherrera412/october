import json
import requests
import stage1
import datetime

def dateConvert(date, intrv):
	getTime = datetime.datetime.strptime(datestamp,'%Y-%m-%dT%H:%M:%SZ')\
	+ datetime.timedelta(seconds=interv)
	return getTime.strftime('%Y-%m-%dT%H:%M:%SZ')

req = requests.post(stage1.s5ret, data = {'token':stage1.token})
retrieve = json.loads(req.text)
interv = retrieve['interval']
datestamp = retrieve['datestamp']

answer = dateConvert(datestamp, interv)

anso = {'token':stage1.token, 'datestamp':answer}
post = requests.post(stage1.s5val, json = anso )
print(post.text)
