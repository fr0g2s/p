import requests as req
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
res = req.get(url).text
with open('banner.p','w') as f:
	f.write(res)

with open('banner.p','rb') as f:
	data = pickle.load(f)
	for line in data:
		for c in line:
			print(c[0]*c[1], end='')
		print('')
