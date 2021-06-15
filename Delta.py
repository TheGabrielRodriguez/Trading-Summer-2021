import numpy as np
from scipy.stats import norm

def d1():
    t = int(input("What is the time to expiration (% of year)?"))
    s = int(input("Underlying Price?"))
    x = int(input("Strike Price?"))
    r = int(input("risk free rate?"))
    v = int(input("implied volatility?"))
    return (np.log(s/x)+(r+v*v/2)*t)/(v*np.sqrt(t))
def d2():
    d_one = d1()
    v = int(input("implied volatility?"))
    t = int(input("What is the time to expiration (% of year)?"))
    return d_one - (v*np.sqrt(t))
def call_delta():
    q = int(input("What is the compounded dividend yield? (%p.a.)"))
    t = int(input("What is the time to expiration (% of year)?"))
    d_one = d1()
    return np.exp(-q*t) * (norm.cdf(d_one))
def put_delta():
    q = int(input("What is the compounded dividend yield? (%p.a.)"))
    t = int(input("What is the time to expiration (% of year)?"))
    d_one = d1()
    return np.exp(-q * t) * (norm.cdf(d_one) - 1)
def gamma():
    q = int(input("What is the compounded dividend yield? (%p.a.)"))
    t = int(input("What is the time to expiration (% of year)?"))
    s = int(input("Underlying Price?"))
    v = int(input("implied volatility?"))
    d_one = d1()
    return (np.exp(-q * t) / (s*v*np.sqrt(t))) *(1/np.sqrt(np.pi)) * (np.exp((-d_one **2)/2))








