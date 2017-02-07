"""This file is for testing the Oslo model"""
import Oslo_model as om

print "Kim's method: for a oslo om system of L=16, p=0.5, the average length after steady state is 26.5"
A = om.Oslo(16)
print om.average_height(A)

print "Kim's method: for a oslo om system of L=32, p=0.5, the average length after steady state is 53.9"
B = om.Oslo(32)
print om.average_height(B)

print "Checking height method: when p = 1, the height should equal to L, because at every site slope is 1"
C = om.Oslo(10, 1)
C.add_grain(10000)
print C.get_height()

print "Checking height method: when p = 0, the height should equal to 2L, because at every site slope is 2"
D = om.Oslo(10, 0)
D.add_grain(20000)
print D.get_height()
