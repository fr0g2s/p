import requests as req

def digging(phase, next_nothing):
	while True:
		url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={next_nothing}'
		res = req.get(url).text.split(' ')
		next_nothing = res[-1]
		print(url)
		print(' == '+' '.join(res)+' == ')
		if not next_nothing.isnumeric():
			break
		if phase == 1:
			continue
		elif phase == 2:
			next_nothing = str(int(next_nothing)/2)
		

digging(1, str(16044/2))


