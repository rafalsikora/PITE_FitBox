from DataGenerator import *
from NoiseGenerator import *
from Plotter import *
import Fitter
import StatAnalyser
import numpy

# definition of 3rd order polynomial with free parameters (required for fitting)
polynomial3 = lambda x, a, b, c, d: a+b*numpy.array(x)+c*numpy.power(numpy.array(x), 2)+d*numpy.power(numpy.array(x), 3)

# definition of the signal function (3rd order polynomial)
signalShape = lambda x: polynomial3(x, 0, 3, 0, -1)

# definition of the wrong model of measured data
wrongSignalShape = lambda x, a, b, c: a*numpy.sin(b*numpy.array(x)+c)

# create plotting object
plotter = Plotter("noiseEffectStudy")

# defining list of (absolute) noise levels -> noise RMSes
noiseList = [0.01, 0.2, 0.4, 0.6, 0.8]

# running "experiments" with different noise levels
for noiseLevel in noiseList:
    # creating a random (gaussian) noise generator
    noiseGen = NoiseGenerator(noiseLevel)

    # creating a "data factory" following the signalShape with some noise given by noiseGen
    dataGen = DataGenerator(signalShape, 10, (-2, 2), 100, noiseGen)

    # generating data
    data = dataGen.generateData()

    # fitting an appropriate data model and evaluating output
    fitOutput_A = Fitter.fit(data, polynomial3)
    statAnalysisOutput_A = StatAnalyser.evaluate(fitOutput_A)

    # fitting wrong data model and evaluating output
    fitOutput_B = Fitter.fit(data, wrongSignalShape)
    statAnalysisOutput_B = StatAnalyser.evaluate(fitOutput_B)

    # adding both fitting outcomes to printing list
    plotter.addDataToPlot(data, fitOutput_A, statAnalysisOutput_A, noiseLevel)
    plotter.addDataToPlot(data, fitOutput_B, statAnalysisOutput_B, noiseLevel)

# printing the data
plotter.plot()


