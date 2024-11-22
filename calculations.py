import math
import numpy as np
import scipy.stats as se
import matplotlib.pyplot as plt


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

def assetprice_change_plot(start, end,k,r,vol,t):
    pricerange = np.linspace(start,end,100)
    
    call_prices = [call_value(price,k,r,vol,t) for price in pricerange]
    put_prices = [put_value(price,k,r,vol,t) for price in pricerange]
    
    fig, ax = plt.subplots(figsize = (10,6))
    
    ax.plot(pricerange, call_prices, label = "Call Price", color = "blue", linestyle= "-", linewidth=1.5)
    ax.plot(pricerange, put_prices, label = "Put Price", color = "brown", linestyle = "--", linewidth = 1.5)
    
    ax.set_xlabel("Asset Price")
    ax.set_ylabel("Option Price")
    
    ax.set_label("Option Price vs. Asset Price")
    ax.legend()
    ax.grid()
    
    
    return fig, ax
