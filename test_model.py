"""This file is for testing the Oslo model"""
import task1OOP as model

print "Kim's method: for a oslo model system of L=16, p=0.5, the average length after steady state is 26.5"
A = model.Oslo(16)
print model.average_height(A)

print "Kim's method: for a oslo model system of L=32, p=0.5, the average length after steady state is 53.9"
B = model.Oslo(32)
print model.average_height(B)

print "Checking height method: when p = 1, the height should equal to L, because at every site slope is 1"
C = model.Oslo(10, 1)
C.add_grain(10000)
print C.get_height()

print "Checking height method: when p = 0, the height should equal to 2L, because at every site slope is 2"
D = model.Oslo(10, 0)
D.add_grain(20000)
print D.get_height()
