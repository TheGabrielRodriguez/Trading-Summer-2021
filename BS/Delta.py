import numpy as np
from scipy.stats import norm

def delta(flag, s, k, t, r, v):
    d1 = (np.log(s/k)+(r+v*v/2)*t)/(v*np.sqrt(t))
    if flag == "C":
        return norm.cdf(d1)
    else:
        return norm.cdf(-d1)
