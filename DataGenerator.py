# Class representing "data factory". Generates data-points
# following given distribution. Contains feature of random noise simulation.

from NoiseGenerator import *
import numpy


class DataGenerator:
    def __init__(self, func=None, nPointsPerBin=1, xRange=(), nBins=1, noiseGen=None):
        self.function = None
        self.nPointsPerBin = 0
        self.xRange = []
        self.nBins = 1
        self.noiseGen = None
        self.setNPointsPerBin(nPointsPerBin)
        self.setNBins(nBins)
        self.setXRange(xRange)
        self.setFunction(func)
        self.setNoiseGenerator(noiseGen)

    def setNPointsPerBin(self, nPointsPerBin):
        assert isinstance(nPointsPerBin, int)
        self.nPointsPerBin = nPointsPerBin

    def setNBins(self, nBins):
        assert isinstance(nBins, int)
        self.nBins = nBins

    def setXRange(self, xRange):
        assert isinstance(xRange, (list, tuple))
        assert len(xRange) is 2
        assert xRange[0] < xRange[1]
        self.xRange = xRange

    def setFunction(self, func):
        if(func is None):
            self.function = None
        else:
            assert callable(func)
            self.function = func

    def setNoiseGenerator(self, noiseGen):
        if(noiseGen is None):
            self.noiseGenerator = None
        else:
            assert isinstance(noiseGen, NoiseGenerator)
            self.noiseGenerator = noiseGen

    def generateData(self):
        binWidth = float(self.xRange[1]-self.xRange[0])/self.nBins
        x = numpy.arange(binWidth/2+self.xRange[0], binWidth/2+self.xRange[1], binWidth)
        data = []
        for xval in x:
            data.append([xval, [self.function(xval) + self.noiseGenerator() for i in xrange(self.nPointsPerBin)]])
        return data
