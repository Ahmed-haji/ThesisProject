# -*- coding: utf-8 -*-
"""lstmModelSpy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ynkvS87u-jOP0oHE_3qj8NdM4DtU_yHV
"""

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import DataLoader, Dataset, random_split

aaplHistIV = pd.read_pickle('/content/aapl_mean_iv_2017_2022.pkl')
googHistIV = pd.read_pickle('/content/goog_mean_iv_2017_2022.pkl')
msftHistIV = pd.read_pickle('/content/msft_mean_iv_2017_2022.pkl')
ndxHistIV = pd.read_pickle('/content/ndx_mean_iv_2017_2022.pkl')
spyHistIV = pd.read_pickle('/content/spc_mean_iv_2017_2022.pkl')

spyHistIV.rename(columns = {'date':'Date'},inplace = True) #renaming date column to Date for consistency
spyHistIV.set_index('Date',inplace = True,drop = True) #setting index to date

#grab spy  from yfinance

spyHistory = yf.download('^GSPC', start='2016-01-01', end='2023-12-31')
#calculate realised vol
window =21 #realisedVol window size
spyHistory['Daily Return'] = spyHistory['Adj Close'].pct_change()
spyHistory['21dRealisedVol'] = spyHistory['Daily Return'].rolling(window=window).std() * np.sqrt(252)
spyHistory.head()
#

plt.plot(spyHistory['21dRealisedVol'])

spyHistIV['average_iv'].head()

spyHistory['Daily Return']['2017':'2021'].head()

spyHistory['21dRealisedVol']['2017':'2021'].head()

historicIVSeries = spyHistIV['average_iv']
dailyReturnSeries= spyHistory['Daily Return']['2017':'2021']
dailyRealisedVolSeries = spyHistory['21dRealisedVol']['2017':'2021']
df_combined = pd.concat([historicIVSeries,dailyReturnSeries,dailyRealisedVolSeries], axis=1)

# Scale the data
scaler = preprocessing.StandardScaler().fit(df_combined)
scaled_data = scaler.transform(df_combined)
car =
