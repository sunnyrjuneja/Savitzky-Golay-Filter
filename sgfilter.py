import numpy as np

def sgfilter1d(degree, window_size):
    if not isinstance(degree, int) or degree < 0:
        raise ValueError("Degree of polynomial must be positive integers")
    if not isinstance(window_size, int) or window_size % 2 == 0 or window_size < 0:
        raise ValueError("Window size must be positive odd integer")
    if window_size < (degree + 1):
        raise ValueError("Degree to high for window size")
    A = np.array([[n ** i for i in xrange(degree + 1)] for n in xrange(-(window_size - 1)/2, (window_size - 1)/2 + 1)])
    Ainv = np.linalg.pinv(A)
    return Ainv[0]

def sgfilter2d(degree, window_size):
    if not isinstance(degree, int) or degree < 0:
        raise ValueError("Degree of polynomial must be positive integers")
    if not isinstance(window_size, int) or window_size % 2 == 0 or window_size < 0 :
        raise ValueError("Window size must be positive odd integer")
    if window_size ** 2 < ((degree + 2) * (degree + 1)) / 2.0:
        raise ValueError("Degree too high for window size")
    exps = [ {"x": k - n, "y": n } for k in xrange(degree + 1) for n in xrange(k + 1)]
    n = np.arange(-(window_size - 1) / 2, (window_size - 1)/2 + 1, dtype = np.float64)
    dx = np.repeat(n, window_size)
    dy = np.tile(n, [window_size, 1]).reshape(window_size ** 2, )
    A = np.empty((window_size ** 2, len(exps)))
    for i, exp in enumerate(exps):
        A[:,i] = (dx ** exp["x"]) * (dy ** exp["y"])
    Ainv = np.linalg.pinv(A)
    return Ainv[0]

print sgfilter2d(3, 5)
