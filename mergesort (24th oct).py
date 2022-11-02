import random
import time

def mergesort(to_sort: list[float]) -> list[float]:
	input_len = len(to_sort)
	if input_len == 1:
		return to_sort

	a = to_sort[0 : input_len//2]
	b = to_sort[input_len//2 : ]
	sorted_a = mergesort(a)
	sorted_b = mergesort(b)

	result: list[float] = []
	a_len = len(sorted_a)
	b_len = len(sorted_b)
	a_index = 0
	b_index = 0
	while a_index < a_len and b_index < b_len:
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

# cProfile.run("mergesort(test)", sort="time")