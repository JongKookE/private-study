from perceptron import AND,OR, NAND , XOR
import numpy as np

x = np.array([0,1])
w = np.array([0.5,0.5])
b = -0.7
#print(np.sum(w*x)+b)
print("this is AND\n")
AND(0,0)
AND(0,1)
AND(1,0)
AND(1,1)
print("-"*50)

print("this is OR\n")
OR(0,0)
OR(0,1)
OR(1,0)
OR(1,1)
print("-"*50)
print("this is NAND\n")
NAND(0,0)
NAND(0,1)
NAND(1,0)
NAND(1,1)



print("-"*50)
print("this is XOR\n")
XOR(0,0)
XOR(0,1)
XOR(1,0)
XOR(1,1)
