import requests as req
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

res = req.get(url).text.split('\n')[21:1272]

rule = '[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]'
p = re.compile(rule)
it = p.finditer(' '.join(res))
for c in it:
	print(c.group()[4], end='')


