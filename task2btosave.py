import Oslo_model as om
import numpy as np
import pickle

objdict = om.create_oslo_obj(6,1)
time_ax_list = {}
h_list = {}
t_c_list = {}


def h_at_t(time, Oslo_obj):
    time_axis = np.arange(time + 1, dtype=int)
    height = np.zeros(time_axis.size)
    t = np.ones(time_axis.size)
    t[0] = 0
    for i in range(1, len(height)):
        Oslo_obj.add_grain(1)
        height[i] = Oslo_obj.height_1
    return time_axis, height, Oslo_obj.t_c

for key in objdict.keys():
    t_ax, h, t_c = h_at_t(75000, objdict[key])
    time_ax_list[key] = t_ax
    h_list[key] = h
    t_c_list[key] = t_c

with open('task2bdata.pickle', 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([objdict, time_ax_list, h_list, t_c_list], f)
