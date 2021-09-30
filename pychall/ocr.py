import requests as req

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
prob = ''.join(req.get(url).text.split('\n')[38:1258])

for c in prob:
	if prob.count(c) == 1:
		print(c)
	else:
		prob.replace(c,'')
print('')
		
