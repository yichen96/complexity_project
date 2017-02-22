import Oslo_model as om
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
import pickle
from scipy import optimize as so

plt.style.use('ggplot')
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 14

with open('task2bdata.pickle') as f:  # Python 3: open(..., 'wb')
    objdict, time_ax_list, h_list, t_c_list = pickle.load(f)

plt.figure(1)
for key in objdict.keys():
    plt.plot(time_ax_list[key], h_list[key], label="L = %s" % key)


plt.legend(loc=2)
plt.xlabel("time [number of grains added]")
plt.ylabel(r"$h(t;L)$")
plt.axis([0,70000,0,450])


def av_h(height_list, sum_over=3000):
    return np.sum(height_list[::-1][:int(sum_over)] / int(sum_over))


sorted_t_c = []
sorted_av_h = []
sorted_L = np.array(sorted(objdict.keys()))
for i in sorted_L:
    sorted_t_c.append(objdict[i].t_c)
    sorted_av_h.append(av_h(h_list[i]))

slope_t_c, intercept_t_c, r_value_t_c, p_value_t_c, std_err_t_c = stats.linregress(np.log(sorted_L), np.log(sorted_t_c))
slope_h, intercept_h, r_value_h, p_value_h, std_err_h = stats.linregress(sorted_L, sorted_av_h)
slope_hlog, intercept_hlog, r_value_hlog, p_value_hlog, std_err_hlog = stats.linregress(np.log10(sorted_L),
                                                                                        np.log10(sorted_av_h))

print "slope_t_c = ", slope_t_c
print "slope_h = ", slope_h
print "slope_hlog = ", slope_hlog

plt.figure(2)
plt.loglog(sorted_L, sorted_t_c, "ko", label="t_c", alpha=0.5)
plt.loglog(sorted_L, np.exp(np.log(sorted_L) * slope_t_c + intercept_t_c),
           label="Linear fit")  ##What should the equation be???
plt.text(50, 1000, r'$\ln{t_c} = %.1f \ln{L} %.2f $' % (slope_t_c, intercept_t_c), fontsize=16)
plt.xlabel("$L$") #system size
plt.ylabel(r"$t_c$")#cross-over time
plt.legend(loc=2)

plt.figure(3)
plt.plot(sorted_L, sorted_av_h, "bo", label="< h >", alpha=0.5)
plt.plot(sorted_L, sorted_L * slope_h + intercept_h, label="Linear fit")
plt.text(110, 150, r'$h = %.2f L %.2f $' % (slope_h, intercept_h), fontsize=16)
plt.xlabel(r"$L$")
plt.ylabel(r"$<h(t;L)>$")
plt.legend(loc=2)



plt.show()