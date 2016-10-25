import json
import requests
import stage1


def needInHay(needle, haystack):
	for i in range(0, len(haystack)):
		if haystack[i] == needle:
			return i

req = requests.post(stage1.s3ret, data = {'token':stage1.token})
retrieve = json.loads(req.text)

needle = retrieve['needle']
haystack = retrieve['haystack']
index = needInHay(needle, haystack)
answer = {'token':stage1.token, 'needle':index}

post = requests.post(stage1.s3val, data = answer )
print(post.text)