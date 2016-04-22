# Plotter class containing methods drawing data and fit results

import matplotlib.pyplot as plt


class Plotter:

    def __init__(self):
        self.listOfDataToPlot = []

    def addDataToPlot(self, dataset, fitResult):
        assert callable(fitResult[0])
        self.listOfDataToPlot.append([dataset, fitResult])

    def plot(self):
        for data in self.listOfDataToPlot:
            x, y = [], []
            xSingle = []
            for points in data[0]:
                xSingle.append(points[0])
                for ySingle in points[1]:
                    x.append(points[0])
                    y.append(ySingle)
            plt.plot(x, y, 'o', ms=2)
            function = data[1][0]
            parameters = data[1][1]
            plt.plot(xSingle, [function(i, *parameters) for i in xSingle], 'k')
        plt.show()
