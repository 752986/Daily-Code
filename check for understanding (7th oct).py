print("What are yout top 3 musicians?")
out = ()
for i in range(3):
	out = out + (input("> "),)

print(out[1]) #type: ignore
#############

print("What are your top 5 foods?")
out = []
for i in range(5):
	out += input("> ")

print(out[-1])
##############

print("What are your 6 favorite video game villians and heroes?")
out = {}
for i in range(3):
	hero = input("hero: \n> ")
	villian = input("villian: \n> ")
	out[hero] = villian

print(out)
key = input("type a key to get its value: \n> ")
if key in out.keys():
	print(out[key])
else:
	print("that's not a valid key!")
##############