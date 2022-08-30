import numpy

def area(mat: numpy.ndarray) -> float:
    return abs(numpy.linalg.det(mat) / 2)

tri = numpy.array([[1, 2, 1], [6, 2, 1], [4, 0, 1]])

print(area(tri))