import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

data = pd.read_csv('ml/dataset.csv')

#dropped columns containing missing values

data.drop(data.columns[[0,-1]], axis=1, inplace=True)
data = data.dropna()
data.replace({"Working abroad or not": {"Yes":1, "No":0}, "Is there telephone number available": {"Yes":1, "No":0}}, inplace=True)
for col in data.columns:
    print(col+":")
    print(data[col].value_counts())