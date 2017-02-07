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


def _relax(slopes, threshold, p, height):
    avalanche_counter = 0
    while np.any(np.greater(slopes, threshold)):
        for i in range(len(slopes)):
            if slopes[i] > threshold[i]:
                if i == 0:
                    slopes[i] -= 2
                    height -= 1
                    slopes[i + 1] += 1
                    avalanche_counter += 1
                elif i == len(slopes) - 1:
                    slopes[i] -= 1
                    slopes[i - 1] += 1  # DOES THE ORDER MATTERS HERE?
                    avalanche_counter += 1
                else:
                    slopes[i] -= 2
                    slopes[i + 1] += 1
                    slopes[i - 1] += 1
                    avalanche_counter += 1
                threshold[i] = random_generator(p)
    return slopes, threshold, height, avalanche_counter


class Oslo:
    def __init__(self, length, threshold_probability=0.5):
        self.L = int(length)
        self.p = float(threshold_probability)
        # initialise
        self.sites = np.arange(1, self.L + 1, dtype=int)
        self.slopes = np.zeros(self.sites.size, dtype=int)  # z_i = 0
        self.threshold = np.ones(self.slopes.size) * random_generator(self.p)
        self.height_1 = 0  # height at first site i = 1 we only keep track the change in h
        self.avalanches = 0
        self.t_c = 0
        self.grain = 0

    def get_height(self):
        return np.sum(self.slopes)

    def empty_model(self):
        self.slopes = np.zeros(self.sites.size, dtype=int)  # z_i = 0
        self.threshold = np.ones(self.slopes.size) * random_generator(self.p)
        self.height_1 = 0
        self.avalanches = 0
        self.grain = 0

    def add_grain(self, num_grains):
        avalanche = np.zeros(num_grains)
        n_iter = 0
        while n_iter < num_grains:
            # drive
            self.slopes[0] += 1
            self.height_1 += 1
            # self.slopes, self.threshold, self.height_1, s = _relax(self.slopes, self.threshold, self.p, self.height_1)
            avalanche_counter = 0
            while np.any(np.greater(self.slopes, self.threshold)):
                for i in range(len(self.slopes)):
                    if self.slopes[i] > self.threshold[i]:
                        if i == 0:
                            self.slopes[i] -= 2
                            self.height_1 -= 1
                            self.slopes[i + 1] += 1
                            avalanche_counter += 1
                        elif i == len(self.slopes) - 1:
                            self.slopes[i] -= 1
                            self.slopes[i - 1] += 1
                            avalanche_counter += 1
                            if self.t_c is 0:
                                self.t_c = self.grain + n_iter
                        else:
                            self.slopes[i] -= 2
                            self.slopes[i + 1] += 1
                            self.slopes[i - 1] += 1
                            avalanche_counter += 1
                        self.threshold[i] = random_generator(self.p)
            avalanche[n_iter] = avalanche_counter
            n_iter += 1
        if self.avalanches is 0:
            self.avalanches = avalanche
        else:
            self.avalanches = np.concatenate((self.avalanches, avalanche))
        self.grain += num_grains


def average_height(obj, num_grains_stdy_state=30000, sample_rate=1):
    obj.empty_model()
    height_list = []
    obj.add_grain(num_grains_stdy_state)
    height_list.append(obj.get_height())
    for i in range(10):
        obj.add_grain(sample_rate)
        height_list.append(obj.get_height())
    av_height = np.sum(height_list)/len(height_list)
    obj.empty_model()
    return av_height

if __name__ == "__main__":
    a = Oslo(16)
    print a.get_height()
    a.add_grain(0)
    print a.get_height()
    a.add_grain(4)
    print a.slopes
    print a.avalanches
    a.add_grain(6)
    print a.slopes
    print a.avalanches
    #a.empty_model()
    a.add_grain(2500)
    print a.avalanches
    print a.t_c
    print a.grain
# a.empty_model()
# a.add_grain(100)
# print a.get_height()

# a = Oslo(16)
# print average_height(a)
