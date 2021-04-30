#!/Users/huynguyen/miniforge3/envs/math/bin/python3


"""

    NAME: HUY NGUYEN
    *Method for constructing new data points within the range of a discrete set of known data points (Wikipedia).
    *Polynomial interpolation.
    *Source:
        +http://fourier.eng.hmc.edu/e176/lectures/ch7/node4.html
        +https://en.wikipedia.org/wiki/Interpolation

"""


import numpy as np
from sympy import Symbol
from sympy.solvers import solve


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


def newton_interpolation(x, data=None, log=False):
    if data is None or len(data) <= 1:
        print('INVALID INPUT.')
        return

    n_i = 1*(x**0)
    N_n = data[0][1]*(x**0)
    c = Symbol('c')
    for i in range(1, len(data)):
        n_i *= x - data[i-1][0]
        a_i = solve(N_n.subs(x, data[i][0]) + c*(n_i.subs(x, data[i][0])) - data[i][1], c)
        N_n += a_i[0]*n_i

    if log:
        print(N_n)
    return N_n
    


''' PARAMS '''
x = Symbol('x')  # Used with sympy function
data = np.array([[-1,1.937],[0,1],[1,1.349],[2,-0.995]])

# APPLY LAGRANGE POLYNOMIAL
f = newton_interpolation(x, data, log=False)
visualize(f, x, data, x_plot_range=[-20,20], y_plot_range=[-20,20])
