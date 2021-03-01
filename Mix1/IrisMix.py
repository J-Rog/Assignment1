import pandas as pd
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

data = pd.read_csv("bezdekIris.data",header=None)
columns = ['Sepel Length','Sepel Width','Petal Length','Petal Width','Flower']

data.columns=columns

#Splits the data between measurements and flower names
measurements = data[['Sepel Length','Sepel Width','Petal Length','Petal Width']]
names = data[['Flower']]

#Converts the flower catagories into numbers
flower_nums = {'Iris-setosa':1,'Iris-versicolor':2,'Iris-virginica':3}
names = names.replace(flower_nums)

#Sepel Lengths
Sepel_Length_Setosa = measurements['Sepel Length'][0:50]
Sepel_Length_Versicolor = measurements['Sepel Length'][50:100]
Sepel_Length_Virginica = measurements['Sepel Length'][100:150]

#Sepel Widths
Sepel_Width_Setosa = measurements['Sepel Width'][0:50]
Sepel_Width_Versicolor = measurements['Sepel Width'][50:100]
Sepel_Width_Virginica = measurements['Sepel Width'][100:150]

#Petal Lengths
Petal_Length_Setosa = measurements['Petal Length'][0:50]
Petal_Length_Versicolor = measurements['Petal Length'][50:100]
Petal_Length_Virginica = measurements['Petal Length'][100:150]

#Petal Widths
Petal_Width_Setosa = measurements['Petal Width'][0:50]
Petal_Width_Versicolor = measurements['Petal Width'][50:100]
Petal_Width_Virginica = measurements['Petal Width'][100:150]

fig, axs = plt.subplots(2,2)

axs[0,0].set_title("Setosa Length")
domainSLS = np.linspace(Sepel_Length_Setosa.min(),Sepel_Length_Setosa.max(),1000)
axs[0,0].plot(domainSLS, norm.pdf(domainSLS ,Sepel_Length_Setosa.mean(),Sepel_Length_Setosa.std()), label = "Setosa")
domainSLVeris = np.linspace(Sepel_Length_Versicolor.min(), Sepel_Length_Versicolor.max(),1000)
axs[0,0].plot(domainSLVeris, norm.pdf(domainSLVeris, Sepel_Length_Versicolor.mean(), Sepel_Length_Versicolor.std()), label = "Versicolor")
domainSLVirgin = np.linspace(Sepel_Length_Virginica.min(), Sepel_Length_Virginica.max(),1000)
axs[0,0].plot(domainSLVirgin, norm.pdf(domainSLVirgin, Sepel_Length_Virginica.mean(), Sepel_Length_Virginica.std()), label = "Virginica")

axs[0,1].set_title("Setosa Width")
domainSWS = np.linspace(Sepel_Width_Setosa.min(),Sepel_Width_Setosa.max(),1000)
axs[0,1].plot(domainSWS, norm.pdf(domainSWS ,Sepel_Width_Setosa.mean(),Sepel_Width_Setosa.std()), label = "Setosa")
domainSWVeris = np.linspace(Sepel_Width_Versicolor.min(), Sepel_Width_Versicolor.max(),1000)
axs[0,1].plot(domainSWVeris, norm.pdf(domainSWVeris, Sepel_Width_Versicolor.mean(), Sepel_Width_Versicolor.std()), label = "Versicolor")
domainSWVirgin = np.linspace(Sepel_Width_Virginica.min(), Sepel_Width_Virginica.max(),1000)
axs[0,1].plot(domainSWVirgin, norm.pdf(domainSWVirgin, Sepel_Width_Virginica.mean(), Sepel_Width_Virginica.std()), label = "Virginica")

axs[1,0].set_title("Petal Length")
domainPLS = np.linspace(Petal_Length_Setosa.min(),Petal_Length_Setosa.max(),1000)
axs[1,0].plot(domainPLS, norm.pdf(domainPLS ,Petal_Length_Setosa.mean(),Petal_Length_Setosa.std()), label = "Setosa")
domainPLVeris = np.linspace(Petal_Length_Versicolor.min(), Petal_Length_Versicolor.max(),1000)
axs[1,0].plot(domainPLVeris, norm.pdf(domainPLVeris, Petal_Length_Versicolor.mean(), Petal_Length_Versicolor.std()), label = "Versicolor")
domainPLVirgin = np.linspace(Petal_Length_Virginica.min(), Petal_Length_Virginica.max(),1000)
axs[1,0].plot(domainPLVirgin, norm.pdf(domainPLVirgin, Petal_Length_Virginica.mean(), Petal_Length_Virginica.std()), label = "Virginica")

axs[1,1].set_title("Setosa Width")
domainPWS = np.linspace(Petal_Width_Setosa.min(),Petal_Width_Setosa.max(),1000)
axs[1,1].plot(domainSWS, norm.pdf(domainPWS ,Petal_Width_Setosa.mean(),Petal_Width_Setosa.std()), label = "Setosa")
domainPWVeris = np.linspace(Petal_Width_Versicolor.min(), Petal_Width_Versicolor.max(),1000)
axs[1,1].plot(domainSWVeris, norm.pdf(domainPWVeris, Petal_Width_Versicolor.mean(), Petal_Width_Versicolor.std()), label = "Versicolor")
domainPWVirgin = np.linspace(Petal_Width_Virginica.min(), Petal_Width_Virginica.max(),1000)
axs[1,1].plot(domainSWVirgin, norm.pdf(domainPWVirgin, Petal_Width_Virginica.mean(), Petal_Width_Virginica.std()), label = "Virginica")

axs[0,0].legend()
axs[0,1].legend()
axs[1,0].legend()
axs[1,1].legend()

plt.show()
