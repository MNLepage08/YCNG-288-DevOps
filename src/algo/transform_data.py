import pandas as pd


# Function for the output values
def tagger(row):
    if row['next'] < row['lag_0']:
        return 'Sell'
    else:
        return 'Buy'


# Function to calculate the lags of close price
def lags(my_data, my_sp):
    all_lag = pd.DataFrame()
    combined = my_data

    for ticker in my_sp:
        mask = (combined['ticker'] == ticker)
        ticker = combined.loc[mask]

        for lag in range(0, 5):
            ticker[f'lag_{lag}'] = ticker['close'].shift(lag)
        all_lag = all_lag.append(ticker)

    # Keep only interested columns
    all_lag = all_lag.drop(all_lag[['open', 'high', 'low', 'adjclose', 'volume']], axis=1)
    all_lag['date'] = all_lag.index
    all_lag = all_lag.dropna()

    # Calculate Buy/Sell
    all_lag['next'] = all_lag['close'].shift(-1)
    all_lag['out'] = all_lag.apply(tagger, axis=1)

    # print(all_lag)
    return all_lag
