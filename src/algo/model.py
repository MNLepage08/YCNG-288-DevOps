from sklearn.linear_model import LogisticRegression
from datetime import datetime, timedelta
from src.algo.transform_data import lags


def train_baseline_model(my_data, my_sp, my_date):

    # Date of the train model
    date_object = datetime.strptime(my_date, '%Y-%m-%d').date()
    date_object = date_object.replace(day=1)

    # The name of the model based on the date
    version_model = 'baseline_' + str(date_object.year) + '_' + str(date_object.month) + '_v2.pkl'

    txt = "work on that"
    return txt