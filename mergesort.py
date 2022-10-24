import random
import time

def mergesort(a: list[float]):
	a = a.copy()
	if not len(a) == 1:
		a1 = a[0 : len(a)//2]
		a1 = mergesort(a1)

		a2 = a[len(a)//2 : len(a)]
		a2 = mergesort(a2)

		a.clear()
		a.extend(a1)
		a.extend(a2)
		a.sort()
		return a
	else:
		return a

test: list[float] = [random.randint(0, 10000) for _ in range(10_000_000)]

start = time.perf_counter()
result = mergesort(test)
duration = time.perf_counter() - start

print("time: {}".format(duration))
