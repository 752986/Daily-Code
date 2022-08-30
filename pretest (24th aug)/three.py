import random

def midpoint(x1, y1, x2, y2):
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    return (mx, my)

# driver code:
point_range = 10
for i in range(10):
    x1 = (random.random() - 0.5) * point_range
    y1 = (random.random() - 0.5) * point_range
    x2 = (random.random() - 0.5) * point_range
    y2 = (random.random() - 0.5) * point_range

    result = midpoint(x1, y1, x2, y2)

    print("midpoint of ({}, {}) and ({}, {}) = ({}, {})".format(x1, y1, x2, y2, result[0], result[1]))