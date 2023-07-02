from yahoo_fin import stock_info as si
from datetime import datetime, timedelta
from functools import reduce
import pandas as pd


def ticker_stock():
    # Work on colab but not in Flask ???
    # Pass with tickers_sp500()
    sp = si.tickers_sp500()
    return sp


def tickers_sp500():
    """Downloads list of tickers currently listed in the S&P 500 """
    # get list of all S&P 500 stocks
    sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
    sp500["Symbol"] = sp500["Symbol"].str.replace(".", "-")
    sp_tickers = sp500.Symbol.tolist()
    return sp_tickers


def data_training():
    # get list of SP500 ticker
    sp = tickers_sp500()
    # pull data for each SP500 stock
    price_data = {ticker: si.get_data(ticker) for ticker in sp}
    combined = reduce(lambda x, y: x.append(y), price_data.values())
    return combined


def data_prediction(my_ticker):
    now = datetime.now()
    start_date = now - timedelta(days=90)
    prediction = si.get_data(my_ticker, start_date)
    prediction = prediction[prediction['close'].notnull()]
    return prediction
