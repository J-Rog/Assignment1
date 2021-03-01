import pandas as pd
import math
import random
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("bezdekIris.data",header=None)
columns = ['Sepel Length','Sepel Width','Petal Length','Petal Width','Flower']

data.columns=columns
#This shuffles the data for training/testing purposes
data = data.sample(frac=1).reset_index(drop=True)

#Splits the data between inputs (X) and outputs (Y)
measurements = data[['Sepel Length','Sepel Width','Petal Length','Petal Width']]
names = data[['Flower']]
flower_nums = {'Iris-setosa':1,'Iris-versicolor':2,'Iris-virginica':3}

names = names.replace(flower_nums)

print(names.head())

ypoints = measurements['Sepel Length']
ypoints = ypoints.to_numpy()

xpoints = names
xpoints = xpoints.to_numpy()

#plt.hist(ypoints,bins = 20,density=True)
measurements.hist(color='k',alpha=0.5,bins=20)
plt.show()



"""
I'm using a train test split of 90:10, because there are 150 entries
that means 135 training datums and 15 test points. Technically KNN doesn't
need training but these are used to validate that the model can make predictions
"""
train_test_split = 135

x_train = X[0:train_test_split]
x_test = X[train_test_split:].reset_index(drop = True)
y_train = Y[0:train_test_split]
y_test = Y[train_test_split:].reset_index(drop = True)

#Gets every combination of columns in X
ensemble = list(combinations(columns[0:4], 2))

#Convert all elements of ensemble to lists rather than tuples
for i in range(0,len(ensemble)):
    ensemble[i] = list(ensemble[i])
