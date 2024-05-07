"""this script will select the appropriate options using a method derived from VIX near and next term selection
methods """
import numpy as np
import pandas as pd
import DataPull
import functions


def filter_options(df, time_to_maturity=(24, 40)):
    df = df[(df['time_to_maturity'] >= 20) & (
            df['time_to_maturity'] <= 40)]  # filters options with time to maturity between 20 and 40 days

    atm_prices = df.groupby('date')[
        'forward_price'].median().reset_index()  # calculates the median forward price for each date
    atm_prices = atm_prices.rename(columns={'forward_price': 'atm_price'})

    df = pd.merge(df, atm_prices, on='date', how='left')  # places atm prices on main dataframe

    df['moneyness'] = (df['strike_price'] / df['atm_price'])  # calculates the  moneyness
    df = df[(df['moneyness'] <= 1.1) & (df['moneyness'] >= 0.9)]  # filters options with moneyness between 0.9 and 1.1
    return df
