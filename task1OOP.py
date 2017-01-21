from __future__ import division
import numpy as np


def random_generator(p):
    """p is between 0 and 1, is the probability of getting a 1
    1-p is the probability of getting 2"""
    rand_number = np.random.random()
    if rand_number > float(p):
        return int(2)
    else:
        return int(1)


def _relax(slopes, threshold, p):
    while np.any(np.greater(slopes, threshold)):
        for i in range(len(slopes)):
            if slopes[i] > threshold[i]:
                if i == 0:
                        slopes[i] -= 2
                        slopes[i + 1] += 1
                elif i == len(slopes) - 1:
                        slopes[i] -= 1
                        slopes[i - 1] += 1  # DOES THE ORDER MATTERS HERE?
                else:
                        slopes[i] -= 2
                        slopes[i + 1] += 1
                        slopes[i - 1] += 1
                threshold[i] = random_generator(p)
    return slopes, threshold


class Oslo:
    def __init__(self, length, threshold_probability=0.5):
        self.L = int(length)
        self.p = float(threshold_probability)
        # initialise
        self.sites = np.arange(1, self.L + 1, dtype=int)
        self.slopes = np.zeros(self.sites.size, dtype=int)  # z_i = 0
        self.threshold = np.ones(self.slopes.size) * random_generator(self.p)

    def get_height(self):
        return np.sum(self.slopes)

    def empty_model(self):
        self.slopes = np.zeros(self.sites.size, dtype=int)  # z_i = 0
        self.threshold = np.ones(self.slopes.size) * random_generator(self.p)

    def add_grain(self, num_grains):
        n_iter = 0
        while n_iter < num_grains:
            # drive
            self.slopes[0] += 1
            self.slopes, self.threshold = _relax(self.slopes, self.threshold, self.p)
            n_iter += 1
            print n_iter

a = Oslo(16)
print a.get_height()
a.add_grain(10000)
print a.get_height()
a.empty_model()
a.add_grain(100)
print a.get_height()
