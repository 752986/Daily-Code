from matplotlib import pyplot
import numpy

def a(t: float) -> tuple[float, float]:
    return (t**3 - 2*t, t**2 - t)

def b(x: float):
    return numpy.sin(x)

x = []
y = []

# pyplot.plot(numpy.arange(0.0, 1.0, .1), a[0], a[1]) #type: ignore

pyplot.show() #type: ignore