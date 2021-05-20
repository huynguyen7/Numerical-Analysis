import numpy as np
from tqdm import tqdm

"""

    *Name: HUY NGUYEN
    *Trapzoid (calculate area under the curve from given function f and interval [a,b], n split chunks)
    *Trapzoidal rule!

"""


''' PARAMS '''
f = lambda x: np.sin(x)
a = 0
b = np.pi
n = 100


'''
f is input function
[a, b] is interval range.
n is the number of split chunks
'''
def trapzoidal(f, a, b, n):
    area = 0.0
    intervals = np.linspace(a,b,n)
    intervals = list(zip(intervals[:-1], intervals[1:]))
    for (a, b) in tqdm(intervals):
        area += (b-a)*(f(a)+f(b))/2.0
    return area


''' MAIN '''
if __name__ == "__main__":
    area = trapzoidal(f,a,b,n)
    print(f'AREA = {area}')
