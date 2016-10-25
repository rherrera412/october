import json
import requests

token = "a80f562a806780b6fc8503064d5e3a45"

s2ret = 'http://challenge.code2040.org/api/reverse'
s2val = 'http://challenge.code2040.org/api/reverse/validate'

s3ret = 'http://challenge.code2040.org/api/haystack'
s3val = 'http://challenge.code2040.org/api/haystack/validate'

s4ret = 'http://challenge.code2040.org/api/prefix'
s4val = 'http://challenge.code2040.org/api/prefix/validate'

s5ret = 'http://challenge.code2040.org/api/dating'
s5val = 'http://challenge.code2040.org/api/dating/validate'


def registration():
	
	github = "https://github.com/rherrera412/october"

	payload = {"token":token, "github" : github}
	url = "http://challenge.code2040.org/api/register"
	req = requests.post(url, data = payload)
	print(req.text)
	
registration()


