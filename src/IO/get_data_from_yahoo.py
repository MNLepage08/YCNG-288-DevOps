from yahoo_fin import stock_info as si
from datetime import datetime, timedelta
from functools import reduce


def ticker_stock():
    sp = si.tickers_sp500()
    return sp


def data_training():
    # get list of SP500 ticker
    sp = ticker_stock()
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
