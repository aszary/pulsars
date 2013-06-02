from scipy.optimize import leastsq
import numpy as np


def least_sq(x, y, fun, v0, size=200):
    """
    no errors
    """
    x_0 = min(x)
    x_1 = max(x)
    ## Error function
    errfunc = lambda v, x, y: (fun(v, x) - y)
    v, success = leastsq(errfunc, v0, args=(np.array(x), np.array(y)),
                         maxfev=10000)
    #print sum(pow(errfunc(v, np.array(x), np.array(y)), 2.))
    t = '''chi2 = 0.
    for n in range(len(x)):
            residual = (y[n] - fun(v, x[n]))
            chi2 = chi2 + residual*residual
    print chi2
    #'''
    x_new = np.linspace(x_0, x_1, size)
    y_new = fun(v, x_new)
    return x_new, y_new, v


def least_sq1D(x, y, fun, err, v0, size=200):
    """
        err is 1D array (len=1)
    """
    x_0 = min(x)
    x_1 = max(x)
    ## Error function
    errfunc = lambda v, x, y, err: (fun(v, x) - y) / err
    v, success = leastsq(errfunc, v0, args=(np.array(x), np.array(y), np.array(err)), maxfev=10000)
    print sum(pow(errfunc(v, np.array(x), np.array(y), np.array(err)), 2.))
    x_new = np.linspace(x_0, x_1, size)
    y_new = fun(v, x_new)
    return x_new, y_new, v

def least_sq2D(x, y, fun, err, v0, size=200):
    """
        err is 2D array (len=2) - minus error [0], plus error [1]
    """
    x_0 = min(x)
    x_1 = max(x)
    ## Error function
    def errfunc(v, x, y, err):
        diff = fun(v, x) - y
        # err plus or minus?
        for i in xrange(len(diff)):
            if diff[i] < 0:
                diff[i] /= err[0][i]
            else:
                diff[i] /= err[1][i]
        return diff
    errors = np.array([np.array(err[0]), np.array(err[1])])
    v, success = leastsq(errfunc, v0, args=(np.array(x), np.array(y), errors), maxfev=10000)
    print sum(pow(errfunc(v, np.array(x), np.array(y), errors), 2.))
    x_new = np.linspace(x_0, x_1, size)
    y_new = fun(v, x_new)
    return x_new, y_new, v
