#!/Users/huynguyen/miniforge3/envs/math/bin/python3


"""

    NAME: HUY NGUYEN
    *IMPLEMENTATION OF SECANT METHOD.
    *ROOT-FINDING ALGORITHM.
    *Better than Newton-Raphson and Bisection Methods.
    *Secant method does not need f to be differentiable

"""


import numpy as np


def secant_method(x0, x1, f, df, error_rate=1e-3, num_steps=10, plot=False, plot_range=[-10,10]):
    if x0 is None or x1 is None or f is None or df is None:
        print('INVALID INPUT.')
        return
    
    history = [[x0,x1]]
    for step in range(num_steps):
        tmp_x = x1 - (x0-x1)*f(x1)/(f(x0)-f(x1))
        x0 = x1
        x1 = tmp_x
        history.append([x0,x1])

        if np.abs(f(x1)) <= error_rate:
            print(f'The method converged in {step+1} steps with error_rate = {error_rate}')
            break

    if plot:
        import matplotlib.pyplot as plt
        
        for secant_x in history:
            larger_x = secant_x[0] if secant_x[0] >= secant_x[1] else secant_x[1]
            smaller_x = secant_x[0] if secant_x[0] < secant_x[1] else secant_x[1]

            a = (f(larger_x)-f(smaller_x))/(larger_x-smaller_x)
            b = f(smaller_x)+a*smaller_x
            y = lambda x : a*x + b
            
            #pts = np.arange(smaller_x, larger_x, 0.01)
            pts = np.arange(plot_range[0], plot_range[1], 0.1)

            plt.plot(pts, y(pts), linestyle='--', alpha=0.3, linewidth=1, color='mediumvioletred')
        pts = np.arange(plot_range[0], plot_range[1]+1, 0.1)
        history = np.array(history)
        plt.plot(pts, f(pts), markersize=0.7, c='b')
        plt.grid()

        plt.xlabel('Value of X')
        plt.ylabel('Value of Y')
        plt.title('SECANT METHOD')
        plt.plot(x1,f(x1), marker='x', c='r')
        plt.show()

    return x1

""" INPUT """
f = lambda x : x**3 - 25
df = lambda x : 3*(x**2)

root = secant_method(
    x0=-10,
    x1=10,
    f=f,
    df=df,
    error_rate=1e-3,
    num_steps=50,
    plot=True,
    plot_range=[-50,50])

print(f'ROOT = {root}')
