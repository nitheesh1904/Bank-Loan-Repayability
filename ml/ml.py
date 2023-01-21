import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data = pd.read_csv('ml/dataset.csv')

#dropped columns containing missing values

data.drop(data.columns[[0,-1]], axis=1, inplace=True)
data = data.dropna()
data.replace(
    {"Working abroad or not": {"Yes":1, "No":0},

    "Is there telephone number available": {"Yes":1, "No":0},

    "Loan History":{
        "existing loans paid back duly till now":0, 
        "critical account/other loans existing (not at this bank)":1, 
        "delay in paying off loans in the past":2, 
        "all loans at this bank paid back duly":3,
        "no loans taken/all loans paid back duly":4
    },
    
    "Purpose of taking loan":{
        "Purchase of radio/television":0,
        "New Car Purchase":1,
        "Purchase of furniture/equipment":2,
        "Old Car Repair":3,
        "Loan for business establishment":4,
        "Education Loan":5,
        "Other repairs":6,
        "Purchase of domestic appliances":7,
        "Loan for retraining":8
    },

    "Guarantor or Debtor":{
        "none":0,
        "gaurantor":1,
        "co-applicant":2
    },

    "Number of years of employment":{
        "unemployed":0,
        "less than a year":1,
        "between 1 and 4 years":2,
        "greater than 4 years":3
    },

    "Marital Status":{
        "male and single":0,
        "female and divorced/seperated/married":1,
        "male and married/widowed":2,
        "male and divorced/seperated":3
    },

    "amount in current account":{
        "no current account":0,
        "less than 0":1,
        "between 0 and 200":2,
        "greater than 200":3
    },

    "amount in savings account":{
        "no savings account":0,
        "less than 100":1,
        "between 100 and 500":2,
        "between 500 and 1000":3,
        "greater than 1000":4
    },

    "Other loans plans taken":{
        "none":0,
        "bank":1,
        "stores":2
    },

    "Owned property":{
        "No property":0,
        "car or other property":1,
        "building society savings agreement/life insurance":2,
        "Real Estate":3
    },

    "Type of job performed":{
        "unemployed/ unskilled - non-resident":0,
        "skilled employee / official":1,
        "management/ self-employed/highly qualified employee/ officer":2,
        "unskilled - resident":3
    },

    "Type of Housing":{
        "for free":0,
        "own":1,
        "rent":2
    },

    "Loan Defaulted or not":{
        1:0,
        2:1
    }
    }, inplace=True)

result = data["Loan Defaulted or not"]
input = data.drop(columns=["Loan Defaulted or not"], axis=1)

input_train, input_test,result_train,result_test = train_test_split(input,result,test_size=0.2,stratify=result,random_state=2)

# for col in input.columns:
#     print(col+":")
#     print(input[col].value_counts())
#     print()

# print(input.shape, input_train.shape, input_test.shape)

# sns.countplot(x="amount in savings account", hue="Loan Defaulted or not", data=data)
# plt.show()

classifier = svm.SVC(kernel='linear')
classifier.fit(input_train,result_train)
