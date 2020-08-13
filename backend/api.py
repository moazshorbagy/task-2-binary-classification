from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

from data import restructure, scale, impute, encode_categorical_variables
import os

app = Flask(__name__, )

models = ['neural_n', 'knn']
neural_n = knn = columns = scaler = imp_mean = imp_mode = encoders = None

def prepare_models():
    global neural_n, knn, columns, scaler, imp_mean, imp_mode, encoders
    # load_models
    if not os.path.exists('./models/neural_n_model.h5'):
        from neural_n_model import train
        neural_n = train(with_plots = False)
    else:
        from tensorflow.keras.models import load_model
        neural_n = load_model('./models/neural_n_model.h5')

    if not os.path.exists('./models/knn_model.sav'):
        from knn_model import train
        knn = train()
    else:
        with open('./models/knn_model.sav', 'rb') as f:
            knn = pickle.load(f)

    # get preprocessing models from training data
    train = pd.read_csv('dataset/training.csv', sep=';')
    columns = train.columns
    train = restructure(train)
    train, scaler = scale(train)
    train, imp_mean, imp_mode = impute(train)
    _, encoders = encode_categorical_variables(train)

@app.route('/api', methods=["POST"])
def api_post():
    inputs = request.get_json(force=True)
    output = predict(inputs)
    return output

def predict(inputs):
    data = [
        inputs['variable1'], inputs['variable2'], inputs['variable3'], inputs['variable4'],
        inputs['variable5'], inputs['variable6'], inputs['variable7'], inputs['variable8'],
        inputs['variable9'], inputs['variable10'], inputs['variable11'], inputs['variable12'],
        inputs['variable13'], inputs['variable14'], inputs['variable15'], inputs['variable17'],
        inputs['variable18'], inputs['variable19']
    ]
    data = pd.DataFrame([data], columns=columns[:-1])

    # preprocess data
    data = restructure(data)

    if(inputs['model'] == models[1]):
        data, _ = scale(data, scaler)
    data, _, _ = impute(data, imp_mean, imp_mode)
    data, _ = encode_categorical_variables(data, encoders)
    data = data.to_numpy(dtype=np.float32)

    # prediction
    if inputs['model'] == models[0]:
        prediction = np.round(neural_n.predict(data)).astype(np.int16)
        prediction = encoders['classLabel'].inverse_transform(prediction)[0]

    elif inputs['model'] == models[1]:
        prediction = knn.predict(data).astype(np.int16)
        prediction = encoders['classLabel'].inverse_transform(prediction)[0]
    
    return prediction

if __name__ == '__main__':
    prepare_models()
    app.run()
