from yahoo_fin import stock_info as si
from datetime import datetime, timedelta
from functools import reduce
import pandas as pd


def ticker_stock():
    # Take all Tickers of the S&P500
    sp = si.tickers_sp500()
    return sp


# Price for each Ticker and dates
def ticker_price():
    # get list of S&P 500 ticker
    sp = ticker_stock()
    # pull data for each S&P stock
    price_data = {ticker: si.get_data(ticker) for ticker in sp}
    combined = reduce(lambda x, y: x.append(y), price_data.values())
    return combined


# Lags of close price for each Ticker
def ticker_lags():
    combined = ticker_price()
    sp = ticker_stock()

    # Create DataFrame
    lags = pd.DataFrame(columns=['open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker', 'lag_0', 'lag_1',
                                 'lag_2', 'lag_3', 'lag_4'])
    for ticker in sp:
        mask = (combined['ticker'] == ticker)
        ticker = combined.loc[mask]
        for lag in range(0, 5):
            ticker[f'lag_{lag}'] = ticker['close'].shift(lag)
        lags = lags.append(ticker)
    return lags