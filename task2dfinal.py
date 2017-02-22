import Oslo_model as om
import numpy as np
import copy
from matplotlib import pyplot as plt
from scipy import stats
import pickle
import bisect
from scipy import optimize as so

plt.style.use('ggplot')
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 16


# These are the "Tableau 20" colors as RGB.
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

#############################################################

with open('final_task2c_all_data.pickle') as f:  # Python 3: open(..., 'wb')
    objdict, sorted_L, runtime_t_c_list, av_list, std_list, h_dict_list = pickle.load(f)

av_heights = []
P_h_list = []
for i in h_dict_list:
    av_heights.append(sorted(i.keys()))
    P_h_list.append(om.generate_P(i))

plt.figure(7)
for i in range(len(av_heights)):
    plt.plot(av_heights[i], P_h_list[i], label="L = %s" % sorted_L[i], c=tableau20[i*2])

plt.xlabel(r"$h(t;L)$")
plt.ylabel(r"$P(h;L)$")
plt.legend()
plt.show()
# data collapse
scaled_P = []
scaled_av_heights = []

for i in range(len(P_h_list)):
    scaled_P.append(np.array(P_h_list[i]) * std_list[i])
    scaled_av_heights.append((np.array(av_heights[i]) - av_list[i]) / std_list[i])

plt.figure(8)
for i in range(len(scaled_av_heights)):
    plt.plot(scaled_av_heights[i], scaled_P[i], "o", label="L = %s" % sorted_L[i], c=tableau20[i*2], alpha=0.7)

plt.xlabel(r"$\frac{h(t;L) - <h(t; L)>}{\sigma_h(L)}$")
plt.ylabel(r"$P(h;L) \sigma_h(L)$")
plt.legend(numpoints=1)

plt.figure(9)
for i in range(len(scaled_av_heights)):
    plt.semilogy(scaled_av_heights[i], scaled_P[i], "o", label="L = %s" % sorted_L[i], c=tableau20[i*2],alpha=0.7)
plt.xlabel(r"$\frac{h(t; L) - <h(t; L)>}{\sigma_h(L)}$")
plt.ylabel(r"$P(h; L) \sigma_h(L)$")
plt.legend(numpoints=1)
plt.show()