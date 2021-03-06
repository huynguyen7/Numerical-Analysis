#!/Users/huynguyen/miniforge3/envs/math/bin/python3


"""

    NAME: HUY NGUYEN
    *Method for constructing new data points within the range of a discrete set of known data points (Wikipedia).
    *Polynomial interpolation.
    *Source:
        +http://fourier.eng.hmc.edu/e176/lectures/ch7/node3.html
        +https://en.wikipedia.org/wiki/Interpolation

"""


import numpy as np
from sympy import Symbol


def visualize(f=None, x=None, data=None, x_plot_range=[-10,10], y_plot_range=[-10,10]):
    if f is None or data is None:
        print('INVALID INPUT.')
        return
    x_pts = np.arange(x_plot_range[0], x_plot_range[1], 0.1)
    y_pts = np.array([f.subs(x, X) for X in x_pts])
    import matplotlib.pyplot as plt
    plt.grid()
    plt.title('Lagrange polynomial')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x_pts, y_pts, c='Blue')
    plt.scatter(data[:,0], data[:,1])
    plt.xlim(x_plot_range)
    plt.ylim(y_plot_range)
    plt.show()


def lagrange_basis(x ,i, data):
    l_i = 1
    for j in range(len(data)):
        if j == i:
            continue
        else:
            l_i *= (x-data[j][0])/(data[i][0]-data[j][0])
    return l_i


def lagrange_interpolation(x, data=None, log=False):
    if data is None or len(data) == 0:
        print('INVALID INPUT.')
        return

    L_n = 0
    for i in range(len(data)):
        L_n += data[i][1] * lagrange_basis(x, i, data)

    if log:
        print(L_n.expand())
    return L_n


''' PARAMS '''
x = Symbol('x')  # Used with sympy function
data = np.array([[-1,1.937],[0,1],[-0.5,0.1],[1,1.349],[2,-0.995]])

# APPLY LAGRANGE POLYNOMIAL
f = lagrange_interpolation(x, data, log=True)
visualize(f, x, data, x_plot_range=[-20,20], y_plot_range=[-20,20])
