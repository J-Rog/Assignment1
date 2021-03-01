import pandas as pd
import math
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("bezdekIris.data",header=None)
columns = ['Sepel Length','Sepel Width','Petal Length','Petal Width','Flower']

data.columns=columns

#Splits the data between measurements and flower names
measurements = data[['Sepel Length','Sepel Width','Petal Length','Petal Width']]
names = data[['Flower']]

#Converts the flower catagories into numbers
flower_nums = {'Iris-setosa':1,'Iris-versicolor':2,'Iris-virginica':3}
names = names.replace(flower_nums)

#Means and Standard Deviations of each category in each column
#Sepel Lengths
SL_Setosa_Mean = measurements['Sepel Length'][0:50].mean()
SL_Versicolor_Mean = measurements['Sepel Length'][50:100].mean()
SL_Virginica_Mean = measurements['Sepel Length'][100:150].mean()
SL_Setosa_STD = measurements['Sepel Length'][0:50].std()
SL_Versicolor_STD = measurements['Sepel Length'][50:100].std()
SL_Virginica_STD = measurements['Sepel Length'][100:150].std()

#Sepel Widths
SW_Setosa_Mean = measurements['Sepel Width'][0:50].mean()
SW_Veriscolor_Mean = measurements['Sepel Width'][50:100].mean()
SW_Virginica_Mean = measurements['Sepel Width'][100:150].mean()
SW_Setosa_STD = measurements['Sepel Width'][0:50].std()
SW_Veriscolor_STD = measurements['Sepel Width'][50:100].std()
SW_Virginica_STD = measurements['Sepel Width'][100:150].std()

#Petal Lengths
PL_Setosa_Mean =  measurements['Petal Length'][0:50].mean()
PL__Veriscolor_Mean =  measurements['Petal Length'][50:100].mean()
PL_Virginica_Mean =  measurements['Petal Length'][100:150].mean()
PL_Setosa_STD =  measurements['Petal Length'][0:50].std()
PL__Veriscolor_STD =  measurements['Petal Length'][50:100].std()
PL_Virginica_STD =  measurements['Petal Length'][100:150].std()

#Petal Widths
PW_Setosa_Mean =  measurements['Petal Width'][0:50].mean()
PW_Veriscolor_Mean =  measurements['Petal Width'][50:100].mean()
PW_Virginica_Mean =  measurements['Petal Width'][100:150].mean()
PW_Setosa_STD =  measurements['Petal Width'][0:50].std()
PW_Veriscolor_STD =  measurements['Petal Width'][50:100].std()
PW_Virginica_STD =  measurements['Petal Width'][100:150].std()


'''
ypoints = measurements['Sepel Length']
ypoints = ypoints.to_numpy()

xpoints = names
xpoints = xpoints.to_numpy()
'''


measurements.hist(color='k',alpha=0.5,bins=20)
plt.show()

#Gets every combination of columns in X
ensemble = list(combinations(columns[0:4], 2))

#Convert all elements of ensemble to lists rather than tuples
for i in range(0,len(ensemble)):
    ensemble[i] = list(ensemble[i])
