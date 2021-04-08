#!/Users/huynguyen/miniforge3/envs/math/bin/python3

"""

    NAME: HUY NGUYEN
    *IMPLEMENTATION OF BISECTION METHOD
    *If a function f(x) is CONTINUOS on the interval [a,b] with sgn(f(a)) != sgn(f(b)), then we can find an approximate root value of f(x) (find x with f(x) == 0)

    *NOTES: This implementation does not validate if a function f(x) is continuos
    *SOURCE:
    - http://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/07/bisection.html

"""

import numpy as np
import matplotlib.pyplot as plt


def isInvalid(f,interval):  # Sanity check for input interval
    if interval is None or  type(interval) != tuple or len(interval) != 2:
        return True
    a = interval[0]
    b = interval[1]
    if f(a) >= f(b):
        return True
    return False


def plot_function(f, plot_interval):
    if plot_interval[0] >= plot_interval[1]:
        print('INVALID INPUT PLOT_INTERVAL.')
        return

    x = np.arange(plot_interval[0], plot_interval[1]+0.1,0.1)
    plt.figure()
    plt.plot(x, f(x))
    plt.show()


def bisection_find(f, interval, num_steps, error_threshold=0.001, plot=False, plot_interval=(-10,10)):
    if isInvalid(f, interval): 
        print('INVALID INPUT INTERVAL.')
        return

    if plot:
        plot_function(f, plot_interval)

    a = interval[0]
    b = interval[1]

    for step in range(num_steps):
        m = (a+b)/2

        if f(m) == 0:
            print(f'Found exact solution..')
            return m
        elif np.abs(f(m)) <= error_threshold:
            print(f'The method converged in {step+1} STEPS with ERROR_THRESHOLD={error_threshold}.')
            return m
        elif f(m)*f(a) < 0:
            b = m
        else:
            a = m

    return m


# INPUT / One variable function
f = lambda x: x**2 - 4

root = bisection_find(
    f=f,  # One variable function
    interval=(0,10),  # Inclusive bound interval for estimate root
    num_steps=1000,
    error_threshold=1e-07,
    plot=False,  # True will plot the function
    plot_interval=(-10,10))

print(f'ROOT OF THE FUNCTION: {root}')
