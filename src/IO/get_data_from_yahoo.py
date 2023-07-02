from yahoo_fin import stock_info as si
from datetime import datetime, timedelta
import pandas as pd


def ticker_stock():
    # Work on colab but not in Flask ??? Pass with tickers_sp500()
    sp = si.tickers_sp500()
    return sp


def tickers_sp500():
    """Downloads list of tickers currently listed in the S&P 500 """
    sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
    sp500["Symbol"] = sp500["Symbol"].str.replace(".", "-")
    sp_tickers = sp500.Symbol.tolist()
    return sp_tickers


def data_training():
    """Compute table with all historical data of SP500 for the training step"""
    sp = tickers_sp500()
    price_data = {ticker: si.get_data(ticker) for ticker in sp}
    combined = pd.concat([pd.DataFrame(value) for value in price_data.values()], axis=0)
    return combined


def data_prediction(my_ticker):
    now = datetime.now()
    start_date = now - timedelta(days=90)
    prediction = si.get_data(my_ticker, start_date)
    prediction = prediction[prediction['close'].notnull()]
    return prediction
