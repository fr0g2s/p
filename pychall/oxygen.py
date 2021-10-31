from PIL import Image
import numpy
import requests as req



# 각 칸 RGB의 값은 R==G==B 임. 그래서 각 칸의 R값을 들고와 아스키 코드로 바꿔보는게 아이디어임.
# 사진을 그림판에 올린 후, 확대해서 보면 한 칸의 가로가 7픽셀임.
# https://tutoreducto.tistory.com/122

chall_file = 'http://www.pythonchallenge.com/pc/def/oxygen.png'

res = req.get(chall_file).content
with open('oxygen.png', 'wb') as f:
	f.write(res)

with Image.open('oxygen.png', 'r') as img:
    pix = numpy.array(img)
    y = img.height//2
    ans = ''
    
    for x in range(0, img.width, 7):
        ans += chr(pix[y][x][1])
    print(ans)

# [chr(x) for x in [105, 110, 116, 101, 103, 114, 105, 116, 121]]

    