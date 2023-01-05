N_DISCS = 3

class Hanoi:
	state: tuple[list[int], list[int], list[int]] = ([N_DISCS - i for i in range(N_DISCS)], [], [])

	def move(self, pole: int, dest: int):
		if len(self.state[dest]) == 0 or self.state[pole][-1] <= self.state[dest][-1]:
			self.state[dest].append(self.state[pole].pop())
		else:
			raise ValueError("Invalid move! ({} -> {})".format(self.state[pole], self.state[dest]))

	def move_disc(self, pole: int, index: int, dest: int):
		if not (index == len(self.state[pole]) - 1):
			excluded = [0, 1, 2]
			excluded.remove(pole)
			excluded.remove(dest)
			self.move_disc(pole, index + 1, excluded[0])
		
		print("state: {} -> ".format(self.state), end="")
		self.move(pole, dest)
		print("{}".format(self.state))



h = Hanoi()

h.move_disc(0, 0, 2)

print(h.state)
