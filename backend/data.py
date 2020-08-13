import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

_categorical_feat = ['variable1', 'variable4', 'variable5', 'variable6', 'variable7', 'variable9', 'variable10', 'variable12', 'variable13']
_continuous_feat = ['variable2', 'variable3', 'variable8', 'variable11', 'variable14', 'variable15', 'variable17']

feat_count = len(_categorical_feat + _continuous_feat)

def _fix_numeric(row):
    return np.float64(str(row).replace(',', '.')) # sklearn works with float64.

def _fix_nan(row):
    return np.nan if row == 'nan' or row == '' else row

def restructure(data):
    data = data.drop(['variable18'], axis=1) # correlation = 1 in training data and less than 0 in validation. Might be misleading or corrupted.
    data = data.drop(['variable19'], axis=1) # has more than 50% missing values.

    # restructuring floats by replacing commas with dots and converting data type.
    data['variable2'] = data['variable2'].apply(_fix_numeric)
    data['variable3'] = data['variable3'].apply(_fix_numeric)
    data['variable8'] = data['variable8'].apply(_fix_numeric)

    # a better representation for NaNs.
    for feat in (_categorical_feat + _continuous_feat):
        data[feat] = data[feat].apply(_fix_nan)

    return data

# feature scaling (normal distribution)
def scale(data, scaler=None, imp_mean=None, imp_mode=None):
    if(scaler == None):
        scaler = StandardScaler()
        scaler.fit(data[_continuous_feat])

    data[_continuous_feat] = scaler.transform(data[_continuous_feat])

    return data, scaler

# impute missing values
def impute(data, imp_mean=None, imp_mode=None):
    # missing continuous values (mean imputation)
    if(imp_mean == None):
        imp_mean = SimpleImputer(strategy='mean')
        imp_mean.fit(data[_continuous_feat])

    data[_continuous_feat] = imp_mean.transform(data[_continuous_feat])

    # missing categorical values (mode imputation)
    if(imp_mode == None):
        imp_mode = SimpleImputer(strategy='most_frequent')
        imp_mode.fit(data[_categorical_feat])

    data[_categorical_feat] = imp_mode.transform(data[_categorical_feat])

    return data, imp_mean, imp_mode

def encode_categorical_variables(data, encoders=None):
    data.dropna(inplace=True)
    if(encoders == None):
        encoders = dict()
        for feat in (_categorical_feat + ['classLabel']):
            encoders[feat] = LabelEncoder()
            encoders[feat].fit(data[feat])

    for feat in (_categorical_feat + ['classLabel']):
        if feat in data:
            data[feat] = encoders[feat].transform(data[feat])
    
    return data, encoders
