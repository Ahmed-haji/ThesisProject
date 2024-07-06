# Functions for evaluating the performance of the model
import numpy as np
import pandas as pd
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.model_selection import TimeSeriesSplit
from sklearn import preprocessing


def evaluate_regression_metrics(y_true, y_pred):
    mse = metrics.mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = metrics.mean_absolute_error(y_true, y_pred)
    r2 = metrics.r2_score(y_true, y_pred)

    print(f'MSE: {mse}')
    print(f'RMSE: {rmse}')
    print(f'MAE: {mae}')
    print(f'R2: {r2}')


    return None

def plot(y_true, y_pred):
    plt.plot(y_true, label='True')
    plt.plot(y_pred, label='Predicted')
    plt.legend()
    plt.show()


def create_sequences(data, seq_length):
    xs, ys = [], []
    for i in range(len(data) - seq_length - 3):
        x = data[i:(i + seq_length)]
        y = data[(i + seq_length), 0]  # Next 3-day IV
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


def preprocess_data(data, history_name, seq_length=60, splits=5, window=21):
    data = data.rename(columns={'date': 'Date'})  # renaming date column to Date for consistency Fix later
    data = data.set_index('Date')  # setting index to date

    # grab historical data from yfinance
    historical_data = yf.download(history_name, start='2016-01-01', end='2023-12-31', progress=False)
    historical_data['dailyReturn'] = np.log(historical_data['Adj Close'] / historical_data['Adj Close'].shift(1))
    historical_data['21dRealisedVol'] = historical_data['dailyReturn'].rolling(window=window).std() * np.sqrt(252)

    historic_iv_series = data['average_iv']
    historic_volume_series = historical_data['Volume'].rolling(21).mean()['2017':'2021']
    daily_return_series = historical_data['dailyReturn']['2017':'2021']
    daily_realised_vol_series = historical_data['21dRealisedVol']['2017':'2021']
    df_combined = pd.concat([historic_iv_series, daily_return_series, daily_realised_vol_series, historic_volume_series], axis=1)

    # Scale the data
    scaler = preprocessing.StandardScaler().fit(df_combined)
    scaled_data = scaler.transform(df_combined)

    X, y = create_sequences(scaled_data, seq_length)
    tscv = TimeSeriesSplit(n_splits=splits)

    for train_index, test_index in tscv.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]


    return X_train, X_test, y_train, y_test
