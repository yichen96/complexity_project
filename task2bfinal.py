import numpy as np
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
plt.rcParams['legend.fontsize'] = 14

with open('task2bdata.pickle') as f:  # Python 3: open(..., 'wb')
    objdict, time_ax_list, h_list, t_c_list = pickle.load(f)

def moving_average(W, height_list):
    h_moving = np.zeros(height_list.size-2*W)
    for i in range(len(h_moving)):
            h_moving[i] = np.sum(height_list[i:2*W+1+i])/(2.*W+1)
    return h_moving

sorted_L = np.array(sorted(objdict.keys()))
W = 50
moving_h_list = []
time_ed = time_ax_list[256][W:len(time_ax_list[256]) - W]
for key in sorted_L:
    moving_h_list.append(moving_average(W, h_list[key]))

scaled_t = []
scaled_h = []
for i in range(len(moving_h_list)):
    scaled_h.append(np.array(moving_h_list[i]) / sorted_L[i])
    scaled_t.append(np.array(time_ed) / (sorted_L[i] ** 2.))

plt.figure(1)
for i in range(len(moving_h_list)):
    plt.plot(scaled_t[i], scaled_h[i], label="L = %s" % sorted_L[i])

plt.legend(loc=4)
plt.axis([0, 1.5, 0, 1.8])
plt.xlabel(r"$t/t_c$")
plt.ylabel(r"$h/L$")


def powerlaw(L, a, w):
    return a*L**w

turning_pt = (objdict[256].t_c - W)/(sorted_L[-1]**2.)

t_windowed256 = np.array(scaled_t[-1])
h_tilda256 = np.array(scaled_h[-1])

index = bisect.bisect(t_windowed256, turning_pt)
print index
popt, pcov = so.curve_fit(powerlaw, t_windowed256[:index], h_tilda256[:index])
print popt
fitted_x = np.arange(0, 2, 0.01)
fitted_y = popt[0] * fitted_x ** popt[1]

plt.figure(2)
for i in range(len(moving_h_list)):
    plt.plot(scaled_t[i], scaled_h[i], label="L = %s" % sorted_L[i])

plt.plot(fitted_x, fitted_y, "k--", label="fitted line")
plt.legend(loc=4)
plt.text(0.1, 1.4, r'$\frac{\~{h}}{L} = %.1f (t/tc)^{%.1f} $' % (popt[0], popt[1]), fontsize=19)
plt.axis([0, 1.5, 0, 1.8])
plt.xlabel(r"$t/t_c$")
plt.ylabel(r"$h/L$")

print np.sqrt(np.diag(pcov))

plt.show()