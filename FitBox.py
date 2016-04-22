from DataGenerator import *
from NoiseGenerator import *
from Plotter import *
import Fitter
import numpy

# definition of the signal function, here 3rd order polynomial used
signalShape = lambda x: 3*x - x**3

# definition of 3rd order polynomial with free parameters (required for fitting)
polynomial3 = lambda x, a, b: a*numpy.array(x) + b*numpy.power(numpy.array(x), 3)

# definition of the function fitted to measured data
fitFunction = lambda x, a, b, c: a*numpy.sin(b*numpy.array(x)+c)

# creating a random (gaussian) noise generator
noiseGen = NoiseGenerator(0.5)

# creating a "data factory" following the signalShape with some noise
dataGen = DataGenerator(signalShape, 10, (-2, 2), 100, noiseGen)

data = dataGen.generateData()

fitOutput = Fitter.fit(data, polynomial3)

plotter = Plotter()
plotter.addDataToPlot(data, fitOutput)
plotter.plot()


