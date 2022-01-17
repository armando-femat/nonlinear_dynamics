import matplotlib.pyplot as plt


def vector_plot(xv,yv,x_prime, y_prime):
    fig, ax = plt.subplots()
    ax.plot(xv[0], x_prime[0])
    ax.quiver(xv, yv, x_prime, y_prime, x_prime, scale=25)
    plt.show()