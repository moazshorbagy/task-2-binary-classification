import numpy as np
import pandas as pd
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, BatchNormalization

from data import restructure, encode_categorical_variables, feat_count
from performance import evaluate_performance, plot_accuracy, plot_loss
import os

def _create_model():
    model = Sequential()

    model.add(Input(shape=(feat_count,)))
    model.add(BatchNormalization())
    model.add(Dense(units=10, activation='sigmoid'))
    model.add(Dense(units=1, activation='sigmoid'))

    model.compile(
        loss='binary_crossentropy',
        optimizer=RMSprop(learning_rate=0.001),
        metrics=['accuracy'])

    return model

def train(with_plots=True):
    train = pd.read_csv('dataset/training.csv', sep=';')

    # preprocess data
    train = restructure(train)
    train, encoders = encode_categorical_variables(train)
    X_train = train.drop(['classLabel'], axis=1).to_numpy(dtype=np.float32)
    y_train = train['classLabel'].astype(np.float32)

    # build model
    model = _create_model()

    # train model
    history = model.fit(X_train, y_train, epochs=10, batch_size=3, shuffle=True)

    # plot metrics
    if(with_plots):
        plot_accuracy(history)
        plot_loss(history)

    # validate model
    valid = pd.read_csv('dataset/validation.csv', sep=';')
    valid = restructure(valid)
    valid, _ = encode_categorical_variables(valid, encoders)
    X_test = valid.drop(['classLabel'], axis=1).to_numpy(dtype=np.float32)
    y_test = valid['classLabel'].astype(np.float32)

    history = model.evaluate(X_test, y_test)

    # save model
    if not os.path.exists('./models'):
        os.mkdir('models')
    model.save('models/neural_n_model.h5')

    # performance evaluation
    print('\033[1m' + 'Using validation data' + '\033[0m')
    y_pred = np.round(model.predict(X_test))
    evaluate_performance(y_test, y_pred)

    return model
