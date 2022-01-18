import equations.one_dimension as od
import plotting.plot as pplot


if __name__ == '__main__':
    print('PyCharm')

    # xv, yv, x_prime, y_prime = od.sin_x()
    # xv, yv, x_prime, y_prime = od.x_square_minus_one()
    xv, yv, x_prime, y_prime = od.electrical_circuit()
    pplot.vector_plot(xv, yv, x_prime, y_prime)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
