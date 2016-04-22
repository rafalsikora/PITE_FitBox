# Class representing random number generator
# following gaussian distribution of given width (sigma).
# Can be easily extended to draw numbers from any other distribution.

import random


class NoiseGenerator:

    def __init__(self, sigma):
        self.sigma = 1
        self.setSigma(sigma)

    def __call__(self):
        return random.gauss(0, self.sigma)

    def setSigma(self, sigma):
        assert sigma > 0
        self.sigma = sigma
