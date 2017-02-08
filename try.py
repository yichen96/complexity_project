import numpy as np
from matplotlib import pyplot as plt
import Oslo_model as om

avlist = np.array([12.91333333, 26.53333333, 53.87666667, 108.42,218.96333333, 439.22, 882.65333333])
L_list = np.array([8,16, 32,64,128,256, 512])
stdlist= np.array([0.96565464265900136, 1.1323525167641555, 1.2469117406172365, 1.5864845833900298, 1.3742836517830721,
                   1.6886681142146911, 1.8438606840499965])

h_dict1 = {10: 2, 11: 16, 12: 79, 13: 126, 14: 64, 15: 12, 16: 1}
h_dict2 = {23: 1, 24: 7, 25: 42, 26: 97, 27: 103, 28: 38, 29: 8, 30: 4}
h_dict3 = {50: 1, 51: 10, 52: 25, 53: 77, 54: 93, 55: 66, 56: 26, 57: 2}
h_dict4 = {104: 1, 105: 4, 106: 30, 107: 46, 108: 81, 109: 72, 110: 37, 111: 16, 112: 11, 113: 2}
h_dict5 = {215: 1, 216: 9, 217: 36, 218: 64, 219: 81, 220: 68, 221: 35, 222: 6}
h_dict6 = {435: 1, 436: 10, 437: 39, 438: 59, 439: 60, 440: 61, 441: 44, 442: 19, 443: 5, 444: 1, 445: 1}
h_dict7 = {878: 1, 879: 9, 880: 22, 881: 46, 882: 72, 883: 63, 884: 42, 885: 23, 886: 13, 887: 6, 888: 2, 889: 1}


def generate_P(h_dict):
    P = []
    for key in h_dict.keys():
        P.append(om.proba_height(h_dict,key))
    return np.array(P)

P1 = generate_P(h_dict1)
P2 = generate_P(h_dict2)
P3 = generate_P(h_dict3)
P4 = generate_P(h_dict4)
P5 = generate_P(h_dict5)
P6 = generate_P(h_dict6)
P7 = generate_P(h_dict7)
h_list1 = h_dict1.keys()
h_list2 = h_dict2.keys()
h_list3 = h_dict3.keys()
h_list4 = h_dict4.keys()
h_list5 = h_dict5.keys()
h_list6 = h_dict6.keys()
h_list7 = h_dict7.keys()

print P5
print h_list5

#scaled
S1 = P1*stdlist[0]
S2 = P2*stdlist[1]
S3 = P3*stdlist[2]
S4 = P4*stdlist[3]
S5 = P5*stdlist[4]
S6 = P6*stdlist[5]
S7 = P7*stdlist[6]
H_list1 = (h_list1 - avlist[0])/stdlist[0]
H_list2 = (h_list2 - avlist[1])/stdlist[1]
H_list3 = (h_list3 - avlist[2])/stdlist[2]
H_list4 = (h_list4 - avlist[3])/stdlist[3]
H_list5 = (h_list5 - avlist[4])/stdlist[4]
H_list6 = (h_list6 - avlist[5])/stdlist[5]
H_list7 = (h_list7 - avlist[6])/stdlist[6]
print len(S1)
print len(H_list1)



# plt.plot(h_list1, P1)
# plt.plot(h_list2, P2)
# plt.plot(h_list3, P3)
# plt.plot(h_list4, P4)
# plt.plot(h_list5, P5)
# plt.plot(h_list6, P6)
# plt.plot(h_list7, P7)
plt.plot(H_list1, S1)
plt.plot(H_list2, S2)
plt.plot(H_list3, S3)
plt.plot(H_list4, S4)
plt.plot(H_list5, S5)
plt.plot(H_list6, S6)
plt.plot(H_list7, S7)

plt.show()
