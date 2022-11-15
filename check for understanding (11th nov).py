# pyright: strict


import winsound
import random
from typing import Callable, Literal


class TrainCar:
	car_id: int
	is_full: bool

	front: "TrainCar | None"
	back: "TrainCar | None"

	def __init__(self, is_full: bool = False) -> None:
		self.car_id = random.randint(100, 999)
		self.is_full = is_full
		self.front = None
		self.back = None

	def __str__(self) -> str:
		return "Train car with ID {} ({}full)".format(str(type(self)).split("'")[1], self.car_id, "" if self.is_full else "not ")

class Locomotive(TrainCar):
	horn_frequency: int # maybe should eb float depending on pygame sound
	horn_duration: float

	def __init__(self, horn_duration: float, is_full: bool = False) -> None:
		super().__init__(is_full)
		self.horn_frequency = random.randint(100, 400)
		self.horn_duration = horn_duration

	def beep(self):
		winsound.Beep(self.horn_frequency, int(self.horn_duration * 1000))

	def __str__(self) -> str:
		return "Locomotive with ID {} ({}full)".format(self.car_id, "" if self.is_full else "not ")

class CargoCar(TrainCar):
	car_type: Literal["coal", "oil", "automobile", "shipping"]

	def __init__(self, car_type: Literal["coal", "oil", "automobile", "shipping"], is_full: bool = False) -> None:
		super().__init__(is_full)
		self.car_type = car_type

	def __str__(self) -> str:
		return "{} cargo car carrying with ID {} ({}full)".format(self.car_type, self.car_id, "" if self.is_full else "not ")


class Train:
	start: TrainCar| None
	end: TrainCar| None

	def __init__(self, start: TrainCar | None = None) -> None:
		self.start = start
		self.end = start

	def append(self, car: TrainCar):
		if self.end:
			car.front = self.end
			self.end.back = car
		else:
			self.start = car
		self.end = car

	def find(self, condition: Callable[[TrainCar], bool]) -> int | None:
		index = 0
		current = self.start
		while current:
			if condition(current):
				return index
			index += 1
			current = current.back
		return None

	def honk(self):
		current = self.start
		while current:
			if type(current) is Locomotive:
				current.beep()
			current = current.back

	def __getitem__(self, index: int) -> TrainCar:
		current = self.start
		for _ in range(index):
			if current == None:
				raise IndexError
			current = current.back
		if current == None:
			raise IndexError
		return current

	def __str__(self) -> str:
		result = "["
		current = self.start
		while current:
			result += str(current)
			if current.back:
				result += ", "
			current = current.back
		result += "]"
		return result


def add_car(train: Train):
	car: TrainCar
	rand = random.randint(0, 4)
	if rand == 0:
		car = Locomotive(3)
	else:
		car = CargoCar(random.choice(["coal", "oil", "automobile", "shipping"]))
	train.append(car)

def create_train() -> Train:
	return Train(Locomotive(3))
	

######


train = create_train()

print("\n\x1b[35mTrain simulator 2020!!!!\x1b[0m")
print("valid commands: \n  add\n  print \n  search_id <id> \n  count_cargo <type> \n  honk \n")

while True:
	user_in = input("> ").lower().split(" ")
	command = user_in[0]

	if command in ["quit", "exit"]:
		break
	elif command == "help":
		print("valid commands: \n  add\n  print \n  search_id <id> \n  count_cargo <type> \n  honk")
	elif command == "print":
		print(train)
	elif command == "honk":
		train.honk()
	elif command == "add":
		add_car(train)

	if len(user_in) > 1:
		arg = user_in[1]

		if command == "search_id":
			index = train.find(lambda car: car.car_id == int(arg))
			if index == None:
				print("ID not found")
				continue
			car = train[index]
			print(car)
		elif command == "count_cargo":
			count: dict[Literal["coal", "oil", "automobile", "shipping"], int] = {}
			for t in ["coal", "oil", "automobile", "shipping"]:
				count[t] = 0 # type: ignore
			current = train.start
			while current:
				if type(current) is CargoCar:
						count[current.car_type] += 1
				current = current.back
			
			result = count[arg] # type: ignore  # otherwise it yells because it can't guarantee that the str is a valid car type
			print(result)
