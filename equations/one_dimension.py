import numpy as np


def sin_x(nx=50, x_min=-2*np.pi, x_max=2*np.pi):
    nx, ny = nx, 1
    x = np.linspace(x_min, x_max, num=nx)
    y = np.linspace(0, 0, num=ny)

    xv, yv = np.meshgrid(x, y)

    x_prime = np.sin(xv)
    y_prime = yv
    return xv, yv, x_prime, y_prime


def x_square_minus_one(nx=50, x_min=-1.5, x_max=1.55):
    nx, ny = nx, 1
    x = np.linspace(x_min, x_max, num=nx)
    y = np.linspace(0, 0, num=ny)

    xv, yv = np.meshgrid(x, y)

    x_prime = xv**2 - 1
    y_prime = yv
    return xv, yv, x_prime, y_prime
