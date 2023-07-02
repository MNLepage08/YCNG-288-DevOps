import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def tagger(row):
    """Function for the output values"""
    if row['next'] < row['lag_0']:
        return 'Sell'
    else:
        return 'Buy'


def lags(my_data, my_sp):
    """Function to calculate the lags of close price"""
    all_lag = pd.DataFrame()
    combined = my_data

    for ticker in my_sp:
        mask = (combined['ticker'] == ticker)
        ticker = combined.loc[mask]

        for lag in range(0, 5):
            ticker[f'lag_{lag}'] = ticker['close'].shift(lag)
        all_lag = pd.concat([all_lag, ticker], axis=0)

    # Keep only interested columns
    all_lag['date'] = all_lag.index
    all_lag = all_lag.drop(all_lag[['open', 'high', 'low', 'adjclose', 'volume', 'date']], axis=1)
    all_lag = all_lag.dropna()

    # print(all_lag)
    return all_lag
