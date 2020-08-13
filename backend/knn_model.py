from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import pickle

from data import restructure, scale, impute, encode_categorical_variables
from performance import evaluate_performance
import os

def train():
    train = pd.read_csv('dataset/training.csv', sep=';')
    
    # preprocess data
    train = restructure(train)
    train, scaler = scale(train)
    train, imp_mean, imp_mode = impute(train)
    train, encoders = encode_categorical_variables(train)
    X_train = train.drop(['classLabel'], axis=1).to_numpy(dtype=np.float32)
    y_train = train['classLabel'].astype(np.float32)

    # build model
    model = KNeighborsClassifier()
        
    # train model
    model.fit(X_train, y_train)
    print('\033[1m' + 'Using training data' + '\033[0m')
    print("Accuracy: ", round(model.score(X_train, y_train), 3))

    # validate model
    valid = pd.read_csv('dataset/validation.csv', sep=';')
    valid = restructure(valid)
    valid, _ = scale(valid, scaler)
    valid, _, _ = impute(valid, imp_mean, imp_mode)
    
    valid, _ = encode_categorical_variables(valid, encoders)
    X_test = valid.drop(['classLabel'], axis=1).to_numpy(dtype=np.float32)
    y_test = valid['classLabel'].astype(np.float32)

    # save model
    if not os.path.exists('./models'):
        os.mkdir('models')
    with open('models/knn_model.sav', 'wb') as f:
        pickle.dump(model, f)

    # performance evaluation
    print('\033[1m' + 'Using validation data' + '\033[0m')
    y_pred = model.predict(X_test)
    evaluate_performance(y_test, y_pred)

    return model
