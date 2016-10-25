import json
import requests
import stage1

def pref(prefixo,arrayo):
	return [word for word in arrayo if not word.startswith(prefixo)]

req = requests.post(stage1.s4ret, data = {'token':stage1.token})
result = json.loads(req.text)

prefix = result["prefix"]
array = result["array"]
update = pref(prefix, array)
answ = {'token':stage1.token, 'array':update}

post = requests.post(stage1.s4val, json = answ )
print(post.text)
