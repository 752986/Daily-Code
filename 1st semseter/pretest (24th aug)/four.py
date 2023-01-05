friends = ["Mo", "Cai", "Eli", "Sawyer", "Linus"]

nerd = False

for friend in friends:
    if friend.lower() == "mo":
        nerd = True

if nerd:
    print("nerd alert")
else:
    print("cool kids only")