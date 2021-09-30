import requests as req
import zipfile
import sys

chall_file = 'http://www.pythonchallenge.com/pc/def/channel.zip'
res = req.get(chall_file).content



zipfile_path = './channel.zip'
zipextract_path = './channel'
zf = None
with open(zipfile_path, 'wb') as f:
	f.write(res)

	zf = zipfile.ZipFile(zipfile_path, 'r')
	zf.extractall(zipextract_path) 
	

data = b''
next_nothing = '90052'
while True:
	next_file = zipextract_path + '/' + f'{next_nothing}.txt'
	with open(next_file, 'r') as f:
		content = f.read()
		if 'Next nothing is' in content:
			data += zf.getinfo(next_nothing+'.txt').comment
			next_nothing = content.split(' ')[-1]
		else:
			print(content)
			break
print(data.decode('utf-8'))

