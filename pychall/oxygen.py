import requests as req

chall_file = 'http://www.pythonchallenge.com/pc/def/oxygen.png'

res = req.get(chall_file).content
with open('oxygen.png', 'wb') as f:
	f.write(res)

