import numpy
import matplotlib.pyplot as plot
pi = numpy.pi

axes = plot.axes(projection="polar")
axes.set_ylim(0, 2)

for i in numpy.arange(0, 1.2, 0.2):
    def f(x: float) -> float:
        return numpy.sin(-x) + i

    # lists to hold all the points being plotted
    angles = numpy.arange(0, 2*pi, 0.0001)
    radii = [f(theta) for theta in angles]
    # print(angles, radii) # see numbers that are being drawn

    plot.plot(angles, radii, color=(1, i * 0.5, i)) # actually draw it
plot.show()