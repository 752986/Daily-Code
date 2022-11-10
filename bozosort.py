import random
import time


def bozo(l: list[float]) -> list[float]:
	while True:
		prev = l[0]
		for i in l[1:]:
			if i < prev:
				# print("L + ratio")
				swap(l, int(len(l) * random.random()), int(len(l) * random.random()))
				break
			prev = i
		else:
			return l


def swap(l: list[any], i1: int, i2: int): #type: ignore
	temp = l[i1]
	l[i1] = l[i2]
	l[i2] = temp


n = 12

test: list[float] = [random.randint(0, 10000) for _ in range(n)]
for i in range(1, n):
	use = test[:i]

	start = time.perf_counter()
	result = bozo(use)
	duration = time.perf_counter() - start

	# print("result: {}".format(test))
	print((" " * (4 - len(str(n)))) + "n={}, time: {:.10f}".format(i, duration))


	use = test[:i]

	start = time.perf_counter()
	result = use.sort()
	duration = time.perf_counter() - start

	print("builtin time: {:.10f}".format(duration))

	print()




# test: list[float] = [random.randint(0, 10000) for _ in range(n)]
# start = time.perf_counter()
# result = bozo(test)
# duration = time.perf_counter() - start

# print("result: {}".format(test))
# print("n={}, time: {}".format(n, duration))