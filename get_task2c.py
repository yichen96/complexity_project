import Oslo_model as om
import pickle
import numpy as np
objdict = om.create_oslo_obj(7)

sorted_L = np.array(sorted(objdict.keys()))
t_c_list = {32: 806, 128: 13788, 8: 47, 64: 3274, 256: 56131, 16: 211, 512: 228266}

av_list = []
std_list = []
h_dict_list = []
runtime_t_c_list = []
for key in sorted_L:
    av, std, h_dict = om.stats_on_height(objdict[key], num_grains_stdy_state=int(t_c_list[key]+300), averaged=1000000)
    av_list.append(av)
    std_list.append(std)
    h_dict_list.append(h_dict)
    runtime_t_c_list.append(objdict[key].t_c)

with open('newtask2c_all_data.pickle', 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([objdict, sorted_L, runtime_t_c_list, av_list, std_list, h_dict_list], f)
