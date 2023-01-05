class Car:
    def __init__(self, make: str, model: str, color: str, miles: float):
        self.make = make
        self.model = model
        self.color = color
        self.miles = miles

    def __str__(self):
        return "{} {} {} ({} miles)".format(self.color, self.make, self.model, round(self.miles, 2))

    def honk(self):
        print("beep!")


c1 = Car("Nissan", "Leaf", "blue", 1730)
c2 = Car("Toyota", "Prius", "silver", 45068)
c3 = Car("Tesla", "Model Y", "black", 2450)

for c in [c1, c2, c3]:
    c.honk()
    print(c)