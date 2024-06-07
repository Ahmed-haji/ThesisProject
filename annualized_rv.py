import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import yfinance as yf


def annualized_volatility(returns,window):
    return returns.rolling(window=window).std() * np.sqrt(252)
