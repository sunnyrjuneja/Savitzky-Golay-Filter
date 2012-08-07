import numpy as np

def sgfilter1d(degree, window_size):
  if not isinstance(degree, int) or degree < 0:
    raise ValueError("Degree of polynomial must be positive integers")
  if not isinstance(window_size, int) or window_size % 2 == 0 or window_size < 0 :
    raise ValueError("Window size must be positive odd integer")
  if window_size < degree + 2:
    raise ValueError("Degree to high for half width")
  A = np.mat([[n ** i for i in range(degree + 1)] for n in range(-(window_size - 1)/2, (window_size - 1)/2 + 1)])
  Ainv = np.linalg.pinv(A)
  return Ainv[0]
