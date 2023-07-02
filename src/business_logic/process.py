import pickle


def compute_data_prediction(my_table):
    # Compute table for the prediction
    table = my_table
    table_p = table[[f'lag_{lag}' for lag in range(0, 5)]]

    # Pick-up the model and predict
    pickled_model = pickle.load(open('model_2022_9.pkl', 'rb'))
    prediction = pickled_model.predict(table_p.tail(1))
    return prediction.flatten()[-1]

