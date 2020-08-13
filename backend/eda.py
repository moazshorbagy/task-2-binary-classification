import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv('dataset/training.csv', sep=';')

plt.figure(figsize=(10, 6))
sns.countplot(x="classLabel", data=train)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x="variable11", data=train)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x="classLabel", hue="variable9", data=train)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x="classLabel", hue="variable10", data=train)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x="classLabel", hue="variable18", data=train)
plt.show()

valid = pd.read_csv('dataset/validation.csv', sep=';')

f, axes = plt.subplots(1, 2, figsize=(12, 6))
f.suptitle('Training (left) vs Validation (right)')

sns.countplot(x="classLabel", hue="variable19", data=train, ax=axes[0])
sns.countplot(x="classLabel", hue="variable19", data=valid, ax=axes[1])
plt.show()

print("p(yes)={}".format(train[train['classLabel'] == "yes."].shape[0] / train.shape[0]))
print("p(no)={}".format(train[train['classLabel'] == "no."].shape[0] / train.shape[0]))
