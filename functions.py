import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import datapull

def black_scholes_call(s, k, tau, t, r, sigma):
    """
    Calculate the price of a European call option using the Black-Scholes model.

    Parameters:
    s (float): Current price of the underlying asset (stock price).
    k (float): Strike price of the option (price at which the option can be exercised).
    tau (float): Time to maturity of the option, expressed in years.
    t (float): Current time in the context of the option's life (usually 0 if at valuation).
    r (float): Risk-free interest rate, expressed as a decimal (e.g., 0.05 for 5%).
    sigma (float): Volatility of the underlying asset, expressed as a decimal.

    Returns:
    float: The price of the call option.
    """