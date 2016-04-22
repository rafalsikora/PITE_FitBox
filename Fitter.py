# Fitter module

import scipy.optimize
import numpy


def fit(dataset, function):
    x, y, errors = [], [], []
    for points in dataset:
        x.append(points[0])
        average = numpy.mean(points[1])
        std = numpy.std(points[1])
        y.append(average)
        errors.append(std/average)
    popt, pcov = scipy.optimize.curve_fit(function, x, y)
    return [function, popt]
