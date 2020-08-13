# task-2-binary-classification
This repository provides ML models for binary classification and a web interface to use these models

### Dependencies
Check fulfilling the dependencies written in requirements.txt. You can install them using:

#### `pip3 install -r requirements.txt`

Before running python scripts, the dataset must be downloaded and placed in the correct directory (note: I've added the csv and model files to this repository to make it easier to try the app since they were small). The directory structure should look like this:
```
- backend
-- dataset
--- training.csv
--- validation.csv
```

### Exploratory Data Analysis

I've prepared plots for data visualization to help us understand the relation between some independent variables and the dependent variable. To view the visualizations use the following command:

#### `python3 eda.py`

### Model Training

Two models are available; a neural network model and a kNN model. To train the models use following commands:

#### `python3 train.py -m neural_n`
#### `python3 train.py -m knn`

### Using the Web Interface

To use the web application for prediction, the python backend must be started first using the command:
python api.py

Then to start the application use the following commands:

#### `npm install`
#### `npm start`

This runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.
