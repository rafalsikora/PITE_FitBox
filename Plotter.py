# Plotter class containing methods drawing data and fit results

import matplotlib.pyplot as plt
import math

class Plotter:

    def __init__(self, name):
        assert isinstance(name, str)
        self.outputFileName = name
        self.listOfDataToPlot = []

    def addDataToPlot(self, dataset, fitResult, statAnalysisOutput, noiseSigma):
        assert callable(fitResult[0])
        self.listOfDataToPlot.append([dataset, fitResult, statAnalysisOutput, noiseSigma])

    def plot(self):
        padCounter = 0
        nCols = 2
        nRows = math.ceil(float(len(self.listOfDataToPlot))/2)
        plt.figure(num=None, figsize=(nCols*8, nRows*6), dpi=80, facecolor='w', edgecolor='k')
        for data in self.listOfDataToPlot:
            padCounter += 1
            x, xSingle, y = [], [], []
            for points in data[0]:
                xSingle.append(points[0])
                for ySingle in points[1]:
                    x.append(points[0])
                    y.append(ySingle)
            plt.subplot(nRows, nCols, padCounter)
            plt.plot(x, y, 'o', ms=2, mew=0)
            function = data[1][0]
            parameters = data[1][1]
            fitQuality = data[2]
            chi2PerNdfString = "{:.1f}".format(fitQuality[0])+"/"+str(fitQuality[1])
            pValueString = "{:.3f}".format(fitQuality[2])
            sigmaNoiseString = "{:.2f}".format(data[3])
            plt.plot(xSingle, [function(i, *parameters) for i in xSingle], 'k', color='red')
            plt.annotate(r'$\chi^{2}$/NDF = ' + chi2PerNdfString, xy=(0.4, 0.6),  xycoords='axes fraction',
                         xytext=(0.15, 0.92), color='green', fontsize=20)
            plt.annotate("p-value = " + pValueString, xy=(0.4, 0.6),  xycoords='axes fraction',
                         xytext=(0.15, 0.84), color='green', fontsize=20)
            plt.annotate(r'$\sigma_{noise}$ = ' + sigmaNoiseString, xy=(0.4, 0.6),  xycoords='axes fraction',
                         xytext=(0.15, 0.76), color='green', fontsize=20)
        plt.savefig(self.outputFileName, format='pdf', bbox_inches='tight')
