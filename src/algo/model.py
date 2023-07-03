from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from datetime import datetime
import pickle
from src.algo.transform_data import tagger
from src.business_logic.process import load_model_in_bucket


def compute_train_test(my_data):
    # Calculate Buy/Sell for the prediction
    all_lags = my_data
    all_lags['next'] = all_lags['close'].shift(-1)
    all_lags['out'] = all_lags.apply(tagger, axis=1)

    # Compute Train & Test
    train = all_lags.loc[(all_lags.index < '2022-06-01')]
    test = all_lags.loc[(all_lags.index >= '2022-06-01') & (all_lags.index <= '2022-09-01')]

    train_x = train[[f'lag_{lag}' for lag in range(0, 5)]]
    train_y = train['out']
    test_x = test[[f'lag_{lag}' for lag in range(0, 5)]]
    test_y = test['out']
    return train_x, train_y, test_x, test_y


def train_my_model(my_data, my_date):

    train_x, train_y, test_x, test_y = compute_train_test(my_data)

    # Build the baseline model
    model_lr = LogisticRegression()
    model_lr.fit(train_x, train_y)

    # Compute the predictions & scoring
    predictions = model_lr.predict(test_x)
    score = balanced_accuracy_score(test_y, predictions)
    score = str(score)

    # Date of train model
    date_object = datetime.strptime(my_date, '%Y-%m-%d').date()
    date_object = date_object.replace(day=1)

    # The name of the model based on the date enter in get method
    version_model = 'model_' + str(date_object.year) + '_' + str(date_object.month) + '.pkl'

    # Load the file locally
    filename = version_model
    pickle.dump(model_lr, open(filename, 'wb'))

    # Load the file in GCP
    load_model_in_bucket(my_date)

    return score
