from flask import Flask, request
import git

from src.IO.get_data_from_yahoo import tickers_sp500, data_training, data_prediction
from src.algo.transform_data import lags
from src.algo.model import train_my_model
from src.business_logic.process import compute_data_prediction, compute_data_prediction_gcp


app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome_msg():
    return f'Hi, please use the route: get_predict_stock/ticker \n'


@app.route('/train_model/<my_date>', methods=['GET'])
def train_model(my_date):
    """The date format in the get methods = '%Y-%m-%d'"""
    my_sp = tickers_sp500()
    my_train_dataframe = data_training()
    lag_table = lags(my_train_dataframe, my_sp)
    score = train_my_model(lag_table, my_date)
    text = "Balanced Accuracy Score = " + str(score)
    return text


@app.route('/get_predict_stock/<my_ticker>', methods=['GET'])
def get_predict_value(my_ticker):
    my_data_predict = data_prediction(my_ticker)
    sp500 = str(''.join(my_ticker))
    sp = [sp500]
    lag_table = lags(my_data_predict, sp)

    # locally prediction
    # prediction = compute_data_prediction(lag_table)
    prediction = compute_data_prediction_gcp(lag_table)
    return prediction


@app.route('/getversion/')
def getversion():
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    return f'{sha}\n'


if __name__ == '__main__':
    # Used when running locally only. When deploying to Cloud Run,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host='localhost', port=8080, debug=True)
