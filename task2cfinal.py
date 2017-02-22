import numpy as np
import copy
from matplotlib import pyplot as plt
from scipy import stats
import pickle
import bisect
from scipy import optimize as so

plt.style.use('ggplot')
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 14


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


# plt.figure(5)
# plt.plot(sorted_L, av_list, "o", label=r"$<h(t;L)>$")
# plt.axis([0,520,0,1000])
# plt.legend(loc=2)
# plt.xlabel(r"$L$")
# plt.ylabel(r"$<h(t;L)>$")


slope_h, intercept_h, r_value_h, p_value_h, std_err_h = stats.linregress(sorted_L, av_list)
print slope_h
a0 = copy.copy(slope_h)
h_over_L = np.array(copy.copy(av_list))/sorted_L

plt.figure(6)
plt.plot(sorted_L, h_over_L, "ro", label="<h>/L")
plt.axhline(a0, label=r"estimated $a_0 = %.2f$" % a0)
plt.xlabel("L")
plt.ylabel("<h>/L")
# plt.axis([0,600,1.4,1.76])
plt.legend(loc=4, numpoints=1)
slope_h2, intercept_h2, r_value_h2, p_value_h2, std_err_h2 = stats.linregress(sorted_L[3:], av_list[3:])
print slope_h2





trial_h_data = []
logged_data = []
a0_try = np.arange(a0-0.03, a0+0.03, 0.0001)
for i in a0_try:
    trial = i - h_over_L
    trial_h_data.append(trial)
    logged_data.append(np.log(trial))

logged_L = np.log(sorted_L)

slope_list = []
intercept_list = []

lin_fit = {}
for i in range(len(logged_data)):
#     m11, b11 = np.polyfit(logged_L, data,1)
#     print np.polyfit(logged_L, data,1,full=True)[1],m11
    slope, intercept, r_value, p_value, std_err = stats.linregress(logged_L, logged_data[i])
    lin_fit[r_value**2] = (slope,a0_try[i])
    slope_list.append(slope)
    intercept_list.append(intercept)

for key in lin_fit.keys():
    if np.isnan(key):
        del lin_fit[key]

print "largest r-squared is ", max(lin_fit.keys())
print "best fit w1 is ", lin_fit[max(lin_fit.keys())][0]
print "best fit a0 is ", lin_fit[max(lin_fit.keys())][1]
print "a0 ", a0
print "average hight list ", av_list


def linear(x, a, b):
    return a*x + b

#####FIT AGAIN TO GET ERROR
target = lin_fit[max(lin_fit.keys())][1] - h_over_L
popt, pcov = so.curve_fit(linear, logged_L, np.log(target))
print popt[0]
print np.sqrt(np.diag(pcov))[0]

###CREAT A FIGURE
plt.figure(7)
plt.loglog(np.exp(logged_L), np.exp(logged_data[300]), "o", label=r"$a_0 = 1.727$", c=tableau20[0], alpha=0.5)
plt.loglog(np.exp(logged_L), target, "o", label=r"$a_0 = 1.735$",c=tableau20[2], alpha=0.5)
plt.loglog(np.exp(logged_L), np.exp(logged_data[-1]), "o", label=r"$a_0 = 1.757$",c=tableau20[8], alpha=0.5)
plt.loglog(np.exp(logged_L), np.exp(logged_L*slope_list[300] + intercept_list[300]), "--", c=tableau20[0])
plt.loglog(np.exp(logged_L), np.exp(logged_L*slope_list[-1] + intercept_list[-1]),"--", c=tableau20[8])
plt.loglog(np.exp(logged_L), np.exp(logged_L*popt[0] + popt[1]),"--", c=tableau20[2])
plt.legend(loc=3, numpoints=1)
plt.axis([5,715,0.001,0.16])
plt.xlabel(r"$L$")
plt.ylabel(r"$a_0$- <h>\L")

popt_sig, pcov_sig = so.curve_fit(linear, np.log(sorted_L[3:]), np.log(std_list[3:]))
plt.figure(8)
plt.loglog(sorted_L, std_list, "o", label=r"$\sigma(L)$")
plt.loglog(sorted_L, np.exp(np.log(sorted_L)*popt_sig[0]+popt_sig[1]),"--", label="Linear fit")
plt.text(32, 1.2, r'$ \ln{\sigma} = %.2f \ln{L} %.2f $' % (popt_sig[0], popt_sig[1]), fontsize=16)
plt.xlabel(r"$L$")
plt.ylabel(r"$\sigma(L)$")
plt.axis([5,650,0.6,3.5])
plt.legend(loc=2, numpoints=1)

print "slope_sig", popt_sig[0], np.sqrt(np.diag(pcov))[0]

plt.figure(9)
std_list = np.array(std_list)
plt.plot(sorted_L, std_list*sorted_L**-0.23, "o", label=r"$\sigma/L^{0.23}$")
plt.xlabel("L")
plt.ylabel(r"$\sigma/L^{0.23}$")
plt.legend(loc=4, numpoints=1)

plt.show()