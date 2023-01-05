class Animal:
    def __init__(self, type: str, name: str, color: str, hunger: float):
        self.type = type
        self.name = name
        self.color = color
        self.hunger = hunger
    
    def declare(self):
        print(f"I am {self.name}, a {self.type}. I am {self.color}" + (", and hungry." if self.hunger > 50 else "."))

    def speak(self):
        if self.type.lower() == "cat":
            print("meow!")
        elif self.type.lower() == "dog":
            print("woof!")
        elif self.type.lower() == "mouse":
            print("squeak!")


cat = Animal("cat", "Carl", "blue", 35)
dog = Animal("dog", "Doug", "grey", 58)
mouse = Animal("mouse", "Mitch", "white", 12)

cat.declare()
cat.speak()

dog.declare()
dog.speak()

mouse.declare()
mouse.speak()