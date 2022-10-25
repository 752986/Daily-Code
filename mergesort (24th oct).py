import random
import time

def mergesort(input: list[float]) -> list[float]:
	if len(input) == 1:
		return input
	a = input[0 : len(input)//2]
	b = input[len(input)//2 : ]
	sorted_a = mergesort(a)
	sorted_b = mergesort(b)

	result: list[float] = []
	a_index = 0
	b_index = 0
	while a_index < len(sorted_a) and b_index < len(sorted_b):
		if sorted_a[a_index] < sorted_b[b_index]:
			result.append(sorted_a[a_index])
			a_index += 1
		else:
			result.append(sorted_b[b_index])
			b_index += 1
	result = result + sorted_a[a_index : ] + sorted_b[b_index : ]

	return result

test: list[float] = [random.randint(0, 10000) for _ in range(1_000_000)]

start = time.perf_counter()
result = mergesort(test)
duration = time.perf_counter() - start

print("mergesort time: {}".format(duration))

start = time.perf_counter()
result = test.sort()
duration = time.perf_counter() - start

print("builtin time: {}".format(duration))
