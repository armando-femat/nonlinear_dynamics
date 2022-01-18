import numpy as np


def mesh_creation(x_min=-10.0, x_max=10.0, nx=50):
    nx, ny = nx, 1
    x = np.linspace(x_min, x_max, num=nx)
    y = np.linspace(0, 0, num=ny)
    xv, yv = np.meshgrid(x, y)
    return xv, yv


def sin_x(nx=50):
    """
    x_prime = sin(x)
    Equilibrium positions : x_prime = (1+k*2)*Pi locally stable; x_prime = k*2*Pi unstable
    with k equal to any integer value (positive or negative).
    :param nx:
    :return:
    """
    xv, yv = mesh_creation(x_min=-2*np.pi, x_max=2*np.pi, nx=nx)

    x_prime = np.sin(xv)
    y_prime = yv
    return xv, yv, x_prime, y_prime


def x_square_minus_one(nx=50):
    """
    x_prime = x^2 - 1
    Equilibrium positions : x_prime=-1 locally stable; x_prime=1 unstable
    :param nx:
    :return:
    """
    xv, yv = mesh_creation(x_min=-1.5, x_max=1.5, nx=nx)

    x_prime = xv**2 - 1
    y_prime = yv
    return xv, yv, x_prime, y_prime


def electrical_circuit(nx=50):
    """
    x_prime = v_0/r - x/(r*c)
    The flow always towards Q* no matter the initial conditions, it is a globally stable fixed point.
    :param nx:
    :return:
    """
    xv, yv = mesh_creation(x_min=-2, x_max=4, nx=nx)
    v_0 = 1
    r = 1
    c = 1

    x_prime = v_0/r - xv/(r*c)
    y_prime = yv
    return xv, yv, x_prime, y_prime
