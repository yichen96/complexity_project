import Oslo_model as om
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

objdict = om.create_oslo_obj(7)

av1, std1, h_dict1 = om.stats_on_height(objdict["8"], num_grains_stdy_state=200)
av2, std2, h_dict2 = om.stats_on_height(objdict["16"], num_grains_stdy_state=500)
av3, std3, h_dict3 = om.stats_on_height(objdict["32"], num_grains_stdy_state=1200)
av4, std4, h_dict4 = om.stats_on_height(objdict["64"], num_grains_stdy_state=5000)
av5, std5, h_dict5 = om.stats_on_height(objdict["128"], num_grains_stdy_state=16000)
av6, std6, h_dict6 = om.stats_on_height(objdict["256"], num_grains_stdy_state=58000)
# av7, std7, h_dict7 = om.stats_on_height(objdict["512"], num_grains_stdy_state=228000)

avlist = np.array([av1, av2, av3, av4, av5, av6])
L_list = np.array([8, 16, 32, 64, 128, 256])
stdlist = np.array([std1, std2, std3, std4, std5, std6])
print avlist
print L_list
slope_h, intercept_h, r_value_h, p_value_h, std_err_h = stats.linregress(L_list, avlist)
print intercept_h

loglistav = np.log(avlist/L_list)
loglistL = np.log(L_list)
slope_w, intercept_w, r_value_w, p_value_w, std_err_w = stats.linregress(loglistL,loglistav)
print slope_w
# # fitline = slope_h*L_list + intercept_h
# plt.figure(1)
# plt.plot(L_list, avlist)
# # plt.plot(L_list, fitline)
# plt.show()
