import Oslo_model as om
import numpy as np
import copy
from matplotlib import pyplot as plt
import log_bin_CN_2016 as lb
from scipy import stats
import pickle
import bisect
from scipy.signal import find_peaks_cwt
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

def linear(x, a, b):
    return a*x + b


def generate_avalanche(obj, N):
    start = obj.L**2 + obj.L
    avalanches = obj.avalanches[int(start):int(start+N)]
    return avalanches

S_list = []
for key in sorted_L:
    S_list.append(generate_avalanche(objdict[key], 1e6))

def moment(array, k):
    kth_s = array**k
    return np.mean(kth_s)

moment_1 = []
moment_2 = []
moment_3 = []
moment_4 = []
moment_5 = []
for i in S_list:
    moment_1.append(moment(i, 1))
    moment_2.append(moment(i, 2))
    moment_3.append(moment(i, 3))
    moment_4.append(moment(i, 4))
    moment_5.append(moment(i, 5))

moment_list = np.array([moment_1,
moment_2,
moment_3,
moment_4,
moment_5])
moment_dict = {}
for i in np.arange(1,6):
    moment_dict[i] = moment_list[i-1]


fitk1 = stats.linregress(np.log(sorted_L[4:]), np.log(moment_list[0][4:]))
fitk2 = stats.linregress(np.log(sorted_L[4:]), np.log(moment_list[1][4:]))
fitk3 = stats.linregress(np.log(sorted_L[4:]), np.log(moment_list[2][4:]))
fitk4 = stats.linregress(np.log(sorted_L[4:]), np.log(moment_list[3][4:]))
fitk5 = stats.linregress(np.log(sorted_L[4:]), np.log(moment_list[4][4:]))

k_moment_slope = np.array([fitk1[0],fitk2[0],fitk3[0],fitk4[0],fitk5[0]])

k1 = np.log(sorted_L)*fitk1[0] +fitk1[1]
k2 = np.log(sorted_L)*fitk2[0] +fitk2[1]
k3 = np.log(sorted_L)*fitk3[0] +fitk3[1]
k4 = np.log(sorted_L)*fitk4[0] +fitk4[1]
k5 = np.log(sorted_L)*fitk5[0] +fitk5[1]

for i in range(len(moment_list)):
    plt.loglog(sorted_L, moment_list[i],"o",c=tableau20[i*2], label="k=%s"%(i+1))
plt.loglog(sorted_L, np.exp(k1), "--", c=tableau20[0])
plt.loglog(sorted_L, np.exp(k2), "--", c=tableau20[2])
plt.loglog(sorted_L, np.exp(k3), "--", c=tableau20[4])
plt.loglog(sorted_L, np.exp(k4), "--", c=tableau20[6])
plt.loglog(sorted_L, np.exp(k5), "--", c=tableau20[8])
plt.legend(loc=3, numpoints=1)
plt.xlabel("L")
plt.ylabel(r"$<s^k>$")

popt, pcov = so.curve_fit(linear, np.arange(1,6),k_moment_slope)
print popt
print np.sqrt(np.diag(pcov))
plt.figure(2)
plt.plot(np.arange(1,6),k_moment_slope, "ro")
plt.plot(np.arange(1,6), popt[0]*np.arange(1,6)+popt[1], "k--")
plt.legend(loc=4)
plt.xlabel("k")
plt.ylabel(r"$D(1+k-\tau_s)$")
plt.axis([0.5,5.5,0.5,10.5])

taus2 = -popt[1]/popt[0] + 1
print taus2
print popt[0]*(2-taus2)

moment_1 = np.array(moment_1)
moment_2 = np.array(moment_2)
moment_3 = np.array(moment_3)
moment_4 = np.array(moment_4)
moment_5 = np.array(moment_5)

c5 = moment_5*sorted_L**(-fitk5[0])
c2 = moment_2*(sorted_L**(-fitk2[0]))
c1 = moment_1*(sorted_L**(-fitk1[0]))
c3 = moment_3*(sorted_L**(-fitk3[0]))
c4 = moment_4*(sorted_L**(-fitk4[0]))

print c5
print fitk1[0]

plt.figure(3)
plt.semilogx(sorted_L, c1,"o-",c=tableau20[0], label="k=1")
plt.semilogx(sorted_L, c2,"o-",c=tableau20[2], label="k=2")

plt.semilogx(sorted_L, c3,"o-",c=tableau20[4], label="k=3")
plt.semilogx(sorted_L, c4,"o-",c=tableau20[6], label="k=4")
plt.semilogx(sorted_L, c5,"o-",c=tableau20[8], label="k=5")
plt.legend(loc=3)
plt.xlabel("L")
plt.ylabel(r"$<s^k> L^{-D(1+k-\tau_s)}$")
plt.show()