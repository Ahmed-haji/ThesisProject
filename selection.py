"""this script will select the appropriate options using a method derived from VIX near and next term selection
methods """
import numpy as np
import pandas as pd
import DataPull
import functions


def filter_options(df, time_to_maturity=(24, 40) ,moneyness=(0.95, 1.05)):
    df = df[(df['time_to_maturity'] >= time_to_maturity[0])
            & (df['time_to_maturity'] <= time_to_maturity[1])]  # filters options by time to maturity

    atm_prices = df.groupby('date')[
        'forward_price'].median().reset_index()  # calculates the median forward price for each date
    atm_prices = atm_prices.rename(columns={'forward_price': 'atm_price'})

    df = pd.merge(df, atm_prices, on='date', how='left')  # places atm prices on main dataframe

    df['moneyness'] = (df['strike_price'] / df['atm_price'])  # calculates the  moneyness
    df = df[(df['moneyness'] <= moneyness[1]) & (df['moneyness'] >= moneyness[0])]  # filters options by moneyness
    return df
