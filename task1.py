"""Implement oslo model

Write a computer programme (using the programme language of your choice)
to implement the algorithm of the Oslo model in which you can easily change the system size L.
Prepare the system in the empty state with zi = 0 for all i = 1,2,...,L.

Devise and perform some simple tests
(e.g. by selecting particular simple values of p)
to check whether your programme is working as intended.
"""
from __future__ import division
import numpy as np


# def calc_slope(height_list):
#     slopes_list = np.zeros(height_list.size)
#     for i in range(len(slopes_list)):
#         if i == len(slopes_list) - 1:
#             slopes_list[i] = height_list[i] # h_L+1 = 0 so zi = hi - 0
#         else:
#             slopes_list[i] = height_list[i] - height_list[i+1]
#     return slopes_list


def relax(slopes, threshold):
    while np.any(np.greater(slopes, threshold)):
        for i in range(len(slopes)-1):
            if slopes[i] > threshold[i]:
                if i == 0:
                    slopes[i] -= 2
                    slopes[i+1] += 1
                elif i == len(slopes) - 2:
                    slopes[i] -= 1
                    slopes[i-1] += 1  # DOES THE ORDER MATTERS HERE?
                else:
                    slopes[i] -= 2
                    slopes[i+1] += 1
                    slopes[i-1] += 1
                threshold[i] = np.random.randint(1, 3)
    return slopes, threshold



def oslo(size_L, itermax):
    """one dimension lattice, composed of L sites
    number of grains at each site i referred as height h_i
    local slope at site_i is z_i = h_i - h_i+1
    where h_L+1 = 0
    heights, slopes = type int
    each site_i assigned a threshold slope z_i_thresh = 1 or 2 at random

    driven by add grains to site_1
    relax z_i > z_i_thresh"""

    # initialise
    sites = np.arange(1, size_L+1, dtype=int)
    # height = np.zeros(sites.size)
    slopes = np.zeros(sites.size, dtype=int)  # z_i = 0
    threshold = np.random.randint(1, 3, sites.size)
    niter = 0

    # drive and relaxation
    while niter < itermax:
        # drive
        slopes[0] += 1
        slopes, threshold = relax(slopes, threshold)
        niter += 1
        print niter
    print slopes
    return np.sum(slopes)

print oslo(16,30000)


