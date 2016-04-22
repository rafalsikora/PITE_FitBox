# Module which evaluates quality of the fit done by Fitter

import numpy
from scipy import stats

def evaluate(fitOutput):
    chi2 = getChi2(fitOutput)
    ndf = getNDF(fitOutput)
    pVal = getPValue(chi2, ndf)
    return [chi2, ndf, pVal]

def getChi2(fitOutput):
    function = fitOutput[0]
    parameters = fitOutput[1]
    x = fitOutput[2][0]
    y = fitOutput[2][1]
    err = fitOutput[2][2]
    chi2 = 0.0
    for i in xrange(len(x)):
        chi2 += numpy.power((function(x[i], *parameters) - y[i])/err[i], 2)
    return chi2

def getNDF(fitOutput):
    parameters = fitOutput[1]
    x = fitOutput[2][0]
    ndf = len(x) - len(parameters)
    return ndf

def getPValue(chi2, ndf):
    return 1 - stats.chi2.cdf(chi2, ndf)
