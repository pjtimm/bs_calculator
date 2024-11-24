import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def d1(s,k,r,vol,t):
    return (np.log(s/k) + (r + math.pow(vol,2)/2) * t) / (vol * np.sqrt(t))

def d2(s,k,r,vol,t):
    return d1(s,k,r,vol,t) - vol*np.sqrt(t)

def call_value(s,k,r,vol,t):
    val =  s * norm.cdf(d1(s,k,r,vol,t)) - k * np.exp(-r*t) * norm.cdf(d2(s,k,r,vol,t))
    return round(val,2)

def put_value(s,k,r,vol,t):
    val = k * np.exp(-r*t) * norm.cdf(-d2(s,k,r,vol,t)) - s * norm.cdf(-d1(s,k,r,vol,t))
    return round(val,2)

def delta_call(s, k, r, t, vol):
    d1_val = d1(s, k, r, vol, t)
    return norm.cdf(d1_val)

def delta_put(s, k, r, t, vol):
    d1_val = d1(s, k, r, vol, t)
    return norm.cdf(d1_val) - 1

def gamma(s, k, r, t, vol):
    d1_val = d1(s, k, r, vol, t)
    pdf_d1 = norm.pdf(d1_val)
    return pdf_d1 / (s * vol * np.sqrt(t))

def theta_call(s, k, r, t, vol):
    d1_val = d1(s, k, r, vol, t)
    d2_val = d2(s, k, r, vol, t)
    term1 = -(s * norm.pdf(d1_val) * vol) / (2 * np.sqrt(t))
    term2 = r * k * np.exp(-r * t) * norm.cdf(d2_val)
    return term1 - term2

def theta_put(s, k, r, t, vol):
    d1_val = d1(s, k, r, vol, t)
    d2_val = d2(s, k, r, vol, t)
    term1 = -(s * norm.pdf(d1_val) * vol) / (2 * np.sqrt(t))
    term2 = r * k * np.exp(-r * t) * norm.cdf(-d2_val)
    return term1 + term2

def vega(s, k, r, t, vol):
    d1_val = d1(s, k, r, vol, t)
    return s * norm.pdf(d1_val) * np.sqrt(t)

def rho_call(s, k, r, t, vol):
    d2_val = d2(s, k, r, vol, t)
    return k * t * np.exp(-r * t) * norm.cdf(d2_val)

def rho_put(s, k, r, t, vol):
    d2_val = d2(s, k, r, vol, t)
    return -k * t * np.exp(-r * t) * norm.cdf(-d2_val)

def assetprice_change_plot(start, end,k,r,vol,t):
    pricerange = np.linspace(start,end,100)
    
    call_prices = [call_value(price,k,r,vol,t) for price in pricerange]
    put_prices = [put_value(price,k,r,vol,t) for price in pricerange]
    
    fig, ax = plt.subplots(figsize = (10,6))
    
    ax.plot(pricerange, call_prices, label = "Call Price", color = "blue", linestyle= "-", linewidth=1.5)
    ax.plot(pricerange, put_prices, label = "Put Price", color = "brown", linestyle = "--", linewidth = 1.5)
    
    ax.set_xlabel("Spot Price")
    ax.set_ylabel("Option Price")
    
    ax.set_label("Option Price vs. Spot Price")
    ax.legend()
    ax.grid()
    
    
    return fig, ax
