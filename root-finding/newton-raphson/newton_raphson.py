#!/Users/huynguyen/miniforge3/envs/math/bin/python3

"""

    NAME: HUY NGUYEN
    *IMPLEMENTATION OF NEWTON-RAPHSON METHOD.
    *ROOT-FINDING ALGORITHM.
    *This method might fail for bad initial x0.

"""


import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(f=None, df=None, x0=0, error_rate=10e-3, num_steps=10, plot=True, plot_range=[-10,10]):
    if f is None or df is None:
        print('INVALID INPUT.')
        return

    history = [x0]
    x = x0

    for step in range(num_steps):
        if f(x) == 0:
            print(f'Exact solution: {x}')
            break

        x = x-(f(x)/df(x))
        history.append(x)

        if np.abs(f(x)) <= error_rate:
            print(f'x = {x} with error rate = {error_rate}')
            break

    if plot:
        pts = np.arange(plot_range[0], plot_range[1]+1, 0.1)
        history = np.array(history)
        plt.plot(pts, f(pts), c='b')
        plt.grid()
        plt.axis('equal')
        plt.plot(history, f(history), 'r+')
        plt.show()

    return x


""" INPUT FUNCTIONS """
f = lambda x : x**3 - x**2 + x + 0.5
df = lambda x : 3*(x**2) - 2*x + 1

#f = lambda x : 2*(x**2) - x**3 - 2
#df = lambda x : 4*x - 3*(x**2)
error_rate = 10e-5

root = newton_raphson(
    f,
    df,
    x0=5,
    error_rate=error_rate,
    num_steps=40,
    plot=True,  # This plot does not work well..
    plot_range=[-15,15]
)

print(f'ROOT = {root}')
if np.abs(f(root)) > error_rate:
    print('=> WRONG ROOT!')
else:
    print('=> CORRECT ROOT!')
