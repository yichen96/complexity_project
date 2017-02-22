import Oslo_model as om
import numpy as np
import copy
from matplotlib import pyplot as plt
import log_bin_CN_2016 as lb
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

startpoint = 256**2+256
avalanche_try = []

avalanche_try.append(objdict[256].avalanches[int(startpoint):int(startpoint+1e4)])
avalanche_try.append(objdict[256].avalanches[int(startpoint):int(startpoint+1e5)])
avalanche_try.append(objdict[256].avalanches[int(startpoint):int(startpoint+1e6)])


def calc_freq(data):
    datadict = om.list_to_dict(data)
    values = sorted(datadict.keys())
    freqs = []
    for i in values:
        freqs.append(datadict[int(i)])
    freqs = np.array(freqs)
    normalised = freqs/np.float(np.sum(freqs))
    return values, normalised


b = []
c = []

v = []
freq = []

for i in avalanche_try:
    vals1, freq1 = calc_freq(i)
    b1, c1 = lb.log_bin(i, 1., 1., 1.4, debug_mode=False, drop_zeros=False)
    vals2, counts2 = lb.lin_bin(i, max(i))
    b.append(b1)
    c.append(c1)
    v.append(vals1)
    freq.append(freq1)

plt.figure(1)
plt.loglog(v[2], freq[2], ".", alpha=1, c=tableau20[9], label=r"$P_N, N = 10^6$")
plt.loglog(b[2], c[2], "-",c=tableau20[8],linewidth=1.9, label=r"$\~{P}_N, N = 10^6$")
plt.legend(loc=3, numpoints=1)
plt.xlabel(r"$s$")
plt.ylabel(r"$P_N(s; L)$")
plt.figure(2)
plt.loglog(v[1], freq[1], ".", alpha=1, c=tableau20[3], label=r"$P_N, N = 10^5$")
plt.loglog(b[1], c[1], "-",c=tableau20[2],linewidth=1.9, label=r"$\~{P}_N, N = 10^5$")
plt.legend(loc=3, numpoints=1)
plt.xlabel(r"$s$")
plt.ylabel(r"$P_N(s; L)$")
plt.figure(3)
plt.loglog(v[0], freq[0], ".", alpha=1, c=tableau20[1], label=r"$P_N, N = 10^4$")
plt.loglog(b[0], c[0], "-",c=tableau20[0],linewidth=1.9, label=r"$\~{P}_N, N = 10^4$")
plt.legend(loc=3, numpoints=1)
plt.xlabel(r"$s$")
plt.ylabel(r"$P_N(s; L)$")
plt.figure(4)
b1, c1 = lb.log_bin(avalanche_try[-1], 1., 1., 3, debug_mode=False, drop_zeros=False)
plt.loglog(b1, c1, "-",c=tableau20[8],linewidth=1.9, label=r"$\~{P}_N, N = 10^6$")

# plt.loglog(v[1], freq[1], ".", alpha=1, c=tableau20[3], label=r"$P_N, N = 10^5$")
# plt.loglog(v[0], freq[0], ".", alpha=1, c=tableau20[1], label=r"$P_N, N = 10^4$")

# plt.loglog(b[2], c[2], "-",c=tableau20[8],linewidth=1.9, label=r"$\~{P}_N, N = 10^6$")
# plt.loglog(b[1], c[1], "-",c=tableau20[2],linewidth=1.3, label=r"$\~{P}_N, N = 10^5$")
# plt.loglog(b[0], c[0], "-",c=tableau20[0],linewidth=1.3, label=r"$\~{P}_N, N = 10^4$")
plt.legend(loc=3, numpoints=1)
plt.xlabel(r"$s$")
plt.ylabel(r"$P_N(s; L)$")
plt.show()
