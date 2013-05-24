from scipy.optimize import leastsq
import numpy as np

def least_sq(x, y, fun, v0, size=200):
    x_0 = min(x)
    x_1 = max(x)
    ## Error function
    err = lambda v, x, y: (fun(v,x) - y)
    v , success = leastsq(err, v0, args=(np.array(x), np.array(y)),
                          maxfev=10000)
    x_new = np.linspace(x_0, x_1, size)
    y_new = fun(v, x_new)
    return x_new, y_new, v
