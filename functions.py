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


def implied_volatility(row) -> float:
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
    s = row['forward_price']
    k = row['strike_price']
    t = row['tau']
    r = row['risk_free_rate']
    c = row['option_price']
    is_call = row['is_call']

    max_iter = 1000
    tol = 1e-9

    x0 = inflection_point(s, k, t, r)
    p = black_scholes_call(s, k, t, r, x0)
    v = vega(s, k, t, r, x0)
    while (abs(p - c) / v) > tol and max_iter > 0:
        if v < 1e-9:
            break
        x0 = x0 - (p - c) / v
        if is_call:
            p = black_scholes_call(s, k, t, r, x0)
        else:
            p = black_scholes_put(s, k, t, r, x0)

        v = vega(s, k, t, r, x0)
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

def black_scholes_put(s, k, t, r, sigma):
    """
    Calculate the price of a European put option using the Black-Scholes model.

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

    put_price = k * np.exp(-r * t) * norm.cdf(-d2) - s * norm.cdf(-d1)
    return put_price

def average_daily_implied_volatility(data):
    data['date'] = pd.to_datetime(data['date'])

    daily_avg_iv = data.groupby(data['date'].dt.date)['implied_volatility'].mean()
    daily_avg_iv = daily_avg_iv.reset_index()
    daily_avg_iv.columns = ['date', 'average_iv']

    return daily_avg_iv

import matplotlib.pyplot as plt

def plot(daily_average_iv_dict):
    """
    Plot the average implied volatility for multiple stocks on the same graph.

    Parameters:
    daily_average_iv_dict (dict): A dictionary where keys are stock names and values are DataFrames
                                  with 'date' and 'average_iv' columns.
    """
    plt.figure(figsize=(10, 6))  # Set the figure size for better visibility

    for stock_name, data in daily_average_iv_dict.items():
        # Ensure the date column is in the correct datetime format
        data['date'] = pd.to_datetime(data['date'])
        # Plot each stock's data with a unique label
        plt.plot(data['date'], data['average_iv'], label=stock_name)

    plt.xlabel('Date')
    plt.ylabel('Average Implied Volatility')
    plt.title('Average Implied Volatility Over Time')
    plt.legend()  # Add a legend to identify the lines
    plt.grid(True)  # Optionally add a grid for easier reading
    plt.show()

# Example usage:
# Assuming you have dataframes df_aapl, df_msft, df_googl for Apple, Microsoft, and Google,
# and these dataframes have 'date' and 'average_iv' columns:
# stocks_data = {
#     'AAPL': df_aapl,
#     'MSFT': df_msft,
#     'GOOGL': df_googl
# }
# plot(stocks_data)