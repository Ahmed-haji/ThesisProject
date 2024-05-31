from random import gauss
import os
import pandas as pd
import matplotlib as plt
import numpy as np
from arch import arch_model
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

currentdir = os.getcwd()
pickle_path = os.path.join(currentdir, 'Jupyterlab\data') # path to the data folder

average_iv = pd.read_pickle(os.path.join(pickle_path, 'average_iv_series_with_date_nasdaq100.pkl'))

#fitting gartch model
train, test = average_iv[:-200], average_iv[-200:]#splitting the data
train, test = 100 * train, 100 * test #scaling the data

model = arch_model(train, vol='GARCH', p=2, q=0)
model_fit = model.fit()
print(model_fit.summary())

#rolling forecast
rolling_predictions = []
rolling_window_size = 252
# forecast should start on tests only
for start in range(len(average_iv) - rolling_window_size):
    train, test = average_iv[start:start+rolling_window_size], average_iv[start+rolling_window_size]
    train, test = 100 * train, 100 * test


    model = arch_model(train, vol='GARCH', p=2, q=0)
    model_fit = model.fit(disp='off')
    pred = model_fit.forecast(horizon=1)
    rolling_predictions.append(np.sqrt(pred.variance.values[-1,:][0]))
# converting the list to a pandas series
rolling_predictions = pd.Series(rolling_predictions, index=average_iv.index[rolling_window_size:])
#plotting the rolling forecast

#scaling the data
average_iv = 100 * average_iv



plt.figure(figsize=(10, 6))
plt.plot(average_iv[rolling_window_size:], label='True')
plt.plot(rolling_predictions, color='red', label='Rolling forecast')
plt.title('Rolling forecast')
plt.legend()
plt.show()

# plot last 100 only
plt.figure(figsize=(10, 6))
plt.plot(average_iv[-100:], label='True')
plt.plot(rolling_predictions[-100:], color='red', label='Rolling forecast')
plt.title('Rolling forecast')
plt.legend()