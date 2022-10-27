# pyright: strict

cookies = int(input("how many cookies do you have? \n> "))
if cookies < 3:
	print("sorry, you don't have enough cookies!")
elif cookies < 10:
	print("y'know, that's a good amount of cookies.")
else:
	print("that's too many cookies, can  I have one?")

print()
######

response = input("are you a jedi or a sith? \n> ")
if response == "jedi":
	print("you get a green lightsaber!")
elif response == "sith":
	print("you get a red lightsaber!")
else:
	print("you get a breadstick.")

print()
######

for i in range(4, 40, 2):
	print(i)

print()
######

i = 100
while i > 50:
	print(i)
	i -= 10

print()
######

while True:
	response = input("knock, who's there?... banana! \n> ")

	if response == "orange":
		print("orange you glad I didn't say 'banana'?")
		break

print()
######

def f(x:int, y: int, z: int):
	return x * y * z

print(f(2, 3, 4))

print()	
######

def g(x: int):
	for i in range(x, 0, -1):
		print("{} bottles of beer on the wall, {} bottles of beer! \ntake one down, pass it around, {} bottles of beer on the wall! \n".format(i, i, i-1))
bottles = int(input("how many bottles of *root* beer? \n> "))
g(bottles)