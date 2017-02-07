import Oslo_model as om
import numpy as np
from matplotlib import pyplot as plt
import string
from scipy import stats


def create_oslo_obj(num):
    Num = [16, 32, 64, 128, 256, 512]  # change this list to scale with num
    L = Num[0:int(num)]
    obj_dict = {}
    for i in range(len(L)):
        obj_dict['%s' % L[i]] = om.Oslo(L[i])
    return obj_dict

objlist = create_oslo_obj(5)
# print objlist
# print objlist['32'].slopes


def h_at_t(time, Oslo_obj):
    time_axis = np.arange(time + 1, dtype=int)
    height = np.zeros(time_axis.size)
    t = np.ones(time_axis.size)
    t[0] = 0
    for i in range(1, len(height)):
        Oslo_obj.add_grain(1)
        height[i] = Oslo_obj.height_1
    return time_axis, height, Oslo_obj.t_c

time1, height1, t_c1 = h_at_t(20000, objlist['16'])
time2, height2, t_c2 = h_at_t(20000, objlist['32'])
time3, height3, t_c3 = h_at_t(20000, objlist['64'])
time4, height4, t_c4 = h_at_t(20000, objlist['128'])


def moving_average(W, height_list):
    h_moving = np.zeros(height_list.size-2*W)
    for i in range(len(h_moving)):
            h_moving[i] = np.sum(height_list[i:2*W+1+i])/(2.*W+1)
    return h_moving


average_height1 = np.sum(height1[::-1][:100])/100
average_height2 = np.sum(height2[::-1][:100])/100
average_height3 = np.sum(height3[::-1][:100])/100
average_height4 = np.sum(height4[::-1][:100])/100

print t_c1, np.sum(height1[::-1][:100])/100
print t_c2, np.sum(height2[::-1][:100])/100
print t_c3, np.sum(height3[::-1][:100])/100
print t_c4, np.sum(height4[::-1][:100])/100


t_c_list = [t_c1, t_c2, t_c3, t_c4]
average_height_list = [average_height1, average_height2, average_height3, average_height4]
L_list = [16, 32, 64, 128]
slope_t_c, intercept_t_c, r_value_t_c, p_value_t_c, std_err_t_c = stats.linregress(np.log(L_list), np.log(t_c_list))
slope_h, intercept_h, r_value_h, p_value_h, std_err_h = stats.linregress(L_list, average_height_list)
print 'line of average height', slope_h, intercept_h
print 'line of t_c', slope_t_c, intercept_t_c

h_moving_1 = moving_average(25, height1)
h_moving_2 = moving_average(25, height2)
h_moving_3 = moving_average(25, height3)
h_moving_4 = moving_average(25, height4)
print h_moving_1

#===========================PLOTS
plt.figure(1)
plt.plot(time1, height1, label='L=16')
plt.plot(time2, height2, label='L=32')
# plt.plot(time3, height3, label='L=64')
# plt.plot(time4, height4, label='L=128')


# plt.xscale('log')
# plt.yscale('log')
plt.legend()
# the height should be independent?

plt.figure(2)
plt.plot(np.log(L_list), np.log(t_c_list), label='t_c')
# plt.plot(L_list, average_height_list, label='average height')
plt.legend()

time1changed = time1[25:len(time1)-25]
time2changed = time2[25:len(time2)-25]
time3changed = time3[25:len(time3)-25]
time4changed = time4[25:len(time4)-25]

plt.figure(3)
plt.plot(time1changed, h_moving_1, label='L=16')
plt.plot(time2changed, h_moving_2, label='L=32')
plt.plot(time3changed, h_moving_3, label='L=64')
plt.plot(time4changed, h_moving_4, label='L=128')
plt.legend()


scaledh1 = h_moving_1/(1.7 * 16)
scaledh2 = h_moving_2/(1.7 * 32)
scaledh3 = h_moving_3/(1.7 * 64)
scaledh4 = h_moving_4/(1.7 * 128)

scaledt1 = time1changed/(16**1.97)
scaledt2 = time2changed/(32**1.97)
scaledt3 = time3changed/(64**1.97)
scaledt4 = time4changed/(128**1.97)

plt.figure(4)
plt.plot(scaledt1, scaledh1, label='L=16')
plt.plot(scaledt2, scaledh2, label='L=32')
plt.plot(scaledt3, scaledh3, label='L=64')
plt.plot(scaledt4, scaledh4, label='L=128')
plt.legend()

plt.figure(5)
plt.plot(np.log(scaledt1), np.log(scaledh1), label='L=16')
plt.plot(np.log(scaledt2), np.log(scaledh2), label='L=32')
plt.plot(np.log(scaledt3), np.log(scaledh3), label='L=64')
plt.plot(np.log(scaledt4), np.log(scaledh4), label='L=128')

plt.show()
