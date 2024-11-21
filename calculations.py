import math
import numpy as np
import scipy.stats as se


def d1(s,k,r,vol,t):
    return (np.log(s/k) + (r + math.pow(vol,2)/2) * t) / (vol * np.sqrt(t))

def d2(s,k,r,vol,t):
    return d1(s,k,r,vol,t) - vol*np.sqrt(t)

def call_value(s,k,r,vol,t):
    val =  s * se.norm.cdf(d1(s,k,r,vol,t)) - k * np.exp(-r*t) * se.norm.cdf(d2(s,k,r,vol,t))
    return round(val,2)

def put_value(s,k,r,vol,t):
    val = k * np.exp(-r*t) * se.norm.cdf(-d2(s,k,r,vol,t)) - s * se.norm.cdf(-d1(s,k,r,vol,t))
    return round(val,2)

