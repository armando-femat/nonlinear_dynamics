import matplotlib.pyplot as plt
import numpy as np


def cosec(x):
    csc = 1 / np.sin(x)
    return csc


def cotan(x):
    cot = 1 / np.tan(x)
    return cot


nx = 100
x = np.linspace(-1.5*np.pi, 1.5*np.pi, num=nx)
# x_prime = np.sin(x)
# plt.plot(x, x_prime)
# plt.show()

x_0 = np.pi/4
x_1 = 0
x_2 = -np.pi/2


def time(x, x_0):
    t = np.log(np.abs((cosec(x_0)+cotan(x_0))/(cosec(x)+cotan(x))))
    return t


t_0 = time(x, x_0)
t_1 = time(x, x_1)
t_2 = time(x, x_2)

plt.plot(t_0, x, 'b')
plt.plot(t_1, x, 'r')
plt.plot(t_2, x, 'g')
plt.xlim(left=0)
plt.show()
