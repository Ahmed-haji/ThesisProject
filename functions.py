import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm


def vega(S, K, t, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * t) / (sigma * np.sqrt(t))
    vega = S * norm.pdf(d1) * np.sqrt(t)
    return vega


def inflection_point(S, K, t, r):
    m = S / (K * np.exp(-r * t))
    return np.sqrt(2 * np.abs(np.log(m)) / t)


def implied_volatility(C, s, K, t, r, tol=1e-5, max_iter=100) -> float:
    """
    Calculate the implied volatility of a European call option using the Black-Scholes model.
    Args:
        C:  The market price of the option
        s:
        K:
        t:
        r:
        tol:
        max_iter:

    Returns:

    """
    x0 = inflection_point(s, K, t, r)
    p = black_scholes_call(s, K, t, r, x0)
    v = vega(s, K, t, r, x0)
    while (abs(p - C) / v) > tol and max_iter > 0:
        x0 = x0 - (p - C) / v
        p = black_scholes_call(s, K, t, r, x0)  # theoretical price of the option
        v = vega(s, K, t, r, x0)
        max_iter -= 1
    return x0


def black_scholes_call(s, k, t, r, sigma):
    """
    Calculate the price of a European call option using the Black-Scholes model.

    Parameters:
    s (float): Current price of the underlying asset (stock price).
    k (float): Strike price of the option (price at which the option can be exercised).
    tau (float): Time to maturity of the option, days.
    t (float): Current time in the context of the option's life (usually 0 if at valuation).
    r (float): Risk-free interest rate
    sigma (float): Volatility of the underlying asset, expressed as a decimal.

    Returns:
    float: The price of the call/put
     option.
    """

    d1 = (np.log(s / k) + (r + 0.5 * sigma ** 2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)

    call_price = s * norm.cdf(d1) - k * np.exp(-r * t) * norm.cdf(d2)
    return call_price
