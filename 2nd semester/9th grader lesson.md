# 1. Hello World
- printing
- strings
```py
print("Hello, world!")
```

# 2. Input
- variables
- input
- string concatenation
```py
name = input("what's your name?")
print("Hello, " + name)
```

# 3. Numbers
- type conversion
- math
```py
year = int(input("When were you born?"))
age = 2023 - year
print("You're " + str(age) + "years old!")
```

# 4. If statements
- if, elif, else
- comparison
```py
age = int(input("how old are you?"))
if age >= 18:
    print("You can vote!")
elif age >= 16:
    print("you can drive!")
else: 
    print("You're not old enough!")
```

# 5. Loops
- for and while loops
- equality operators
```py
for i in range(10):
    print(i)
```
```py
while int(input("pick a number")) != 3:
    print("you didn't guess the number")
```

# 6. Randomness
- random numbers
- libraries
```py
import random

random_number = random.randint(1, 100)

while int(input("pick a number between 1 and 100!")) != 3:
    print("you didn't guess the number")

print("congrats!!")
```