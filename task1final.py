import Oslo_model as om
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 14

plt.figure(1)
L = 10
model = om.Oslo(L, 1)
model.add_grain(300)
print model.height_1
print model.t_c
plt.plot(range(300), model.avalanches, label="L = 10, p = 1")
model_2 = om.Oslo(L, 0)
model_2.add_grain(300)
print model_2.height_1
print model_2.t_c
plt.plot(range(300), model_2.avalanches, label="L = 10, p = 0")
plt.xlabel("t [number of grains added]")
plt.axis([0,200,0,12])
plt.ylabel("Avalanche size s")
plt.legend(loc=4)

model_3 = om.Oslo(L, 0.5)
model_3.add_grain(3000)
startpt = int(L**2+L)
print np.mean(model_3.avalanches[startpt:])
plt.show()
