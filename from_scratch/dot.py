import numpy as np
from activation import sigmoid, relu

a = np.array([[1,2],[3,4],[5,6]])
b = np.array([[9,10,9],[11,12,11]])

print(a.shape)
print(b.shape)
print(np.dot(a,b))


x = np.array([1,2])
w = np.array([[1,3,5],[2,4,6]])

print(f"x.shape = {x.shape}, w's shape = {w.shape}")

print(np.dot(x,w))

x = np.array([1.0, 0.5])
w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])


a1 = np.dot(x,w1) + b1
s1 = sigmoid(a1)

print(s1)

w2 = np.array([[0.1,0.4], [0.2,0.5], [0.3,0.6]])
b2 = np.array([0.1,0.2])

a2 = np.dot(s1,w2)+b2

s2 = sigmoid(a2)
print(s2)

def identity_function(x):
    return x

w3 = np.array([[0.1,0.3], [0.2,0.4]])
b3 = np.array([0.1,0.2])

a3 = np.dot(s2, w3)+b3
y = identity_function(a3)

print(f" {y}")