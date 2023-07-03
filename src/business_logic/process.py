import pickle
from datetime import datetime
import configparser
import logging
# import joblib


from src.IO.storage_tools import create_bucket, upload_file_to_bucket, get_model_from_bucket


def compute_data_prediction(my_table):
    # Compute table for the prediction
    table = my_table
    table_p = table[[f'lag_{lag}' for lag in range(0, 5)]]

    # Pick-up the model and predict
    pickled_model = pickle.load(open('model_2022_9.pkl', 'rb'))
    prediction = pickled_model.predict(table_p.tail(1))
    return prediction.flatten()[-1]


# # name of your bucket in GCP
# root_bucket = 'devops_bucket_mnl'
# config = configparser.ConfigParser()
# config.read('application.conf')
# create_bucket(root_bucket)


# def get_version():
#    return config['DEFAULT']['version']


# def get_bucket_name():
#    return f'{root_bucket}_{get_version().replace(".", "")}'


# def load_model_in_bucket(my_date):
#     date_object = datetime.strptime(my_date, '%Y-%m-%d').date()
#     version_model = 'model_' + str(date_object.year) + '_' + str(date_object.month) + '.pkl'
#     log = logging.getLogger()
#     log.warning(f'training model for GCP')
#     upload_file_to_bucket(version_model, root_bucket)


# def compute_data_prediction_gcp(my_table):
#     # Compute table for the prediction
#     table = my_table
#     table_p = table[[f'lag_{lag}' for lag in range(0, 5)]]
#
#     model_filename = 'model_2022_9.pkl'
#     model = get_model_from_bucket(model_filename, root_bucket)
#
#     prediction = model.predict(table_p.tail(1))
#     return prediction.flatten()[-1]
