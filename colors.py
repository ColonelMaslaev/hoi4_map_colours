import random
from PIL import Image
print('Reading image...')
img=Image.open("provinces.bmp")
print('Image read, analyzing...')
p=set()
for x in range(5632):
	for y in range(2048):
		p.add(img.getpixel((x, y)))
print('Analysis complete.')
print('What do you require me to do, modder-senpai?~')
while True:
	if len(p)==16777216:
		print("Wait, what? You used EVERY available color? Why? How? And why? And... how..? I'm afraid i can't help you, pervert-senpai... Get a less complicated map, will you?")
		break
	c=input()
	if c=='help':
		print(" >>color - generates an RGB color code for a new province (it's added to the list upon generating, so no accidental overlaps)\n >>len - prints the number of colors used\n >>exit - stop the... well, program? whatever\n >>help - prints list of avalaible commands - well, you just did that, right?\n aaaaand... that's it, i guess")
	elif c=='color':
		while True:
			r=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			if not(r in p):
				p.add(r)
				print(r[0], r[1], r[2])
				break
	elif c=='exit':
		print('(^-^)/ Hope it was useful! Until next time!')
		break
	elif c=='len':
		print(len(p))
	else:
		print("(>_<) I don't understand you, senpai!~")