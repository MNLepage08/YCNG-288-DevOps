from flask import Flask
import git
from src.IO.get_data_from_yahoo import ticker_stock, ticker_price, ticker_lags


app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome_msg():
    return f'Hi, please use the route: get_predict_stock/ticker \n'


@app.route('/get_predict_stock/<my_ticker>', methods=['GET'])
def get_predict_value(my_ticker):
    data = ticker_lags()
    return data


@app.route('/getversion/')
def getversion():
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    return f'{sha}\n'


if __name__ == '__main__':
    # Used when running locally only. When deploying to Cloud Run,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host='localhost', port=8080, debug=True)
