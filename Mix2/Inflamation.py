import pandas as pd
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

data = pd.read_csv("diagnosis2.data",header=None)
columns = ['Temperature','Nausea','Lumbar Pain','Urine Pushing','Micturition Pains' , \
            'Burning of Urethra', 'Inflamation of Bladder', 'Inflamation of Renal Pelvis']

data.columns=columns

#Converts the yes/no catagories into numbers
yesNoConversion = {'no':1,'yes':2}
data = data.replace(yesNoConversion)


fig, axs = plt.subplots(4,2)

axs[0,0].set_title("Temperature")
axs[0,0].hist(x = data['Temperature'], bins=20, density=True)

low_fever = data[data['Temperature'] < 39]
high_fever = data[data['Temperature'] >= 39]

lf_x = np.linspace(low_fever['Temperature'].min(), low_fever['Temperature'].max(), 1000)
lf_y = norm.pdf(lf_x, low_fever['Temperature'].mean(), low_fever['Temperature'].std())
axs[0,0].plot(lf_x, lf_y, label='Low Fever')

hf_x = np.linspace(high_fever['Temperature'].min(), high_fever['Temperature'].max(), 1000)
hf_y = norm.pdf(hf_x, high_fever['Temperature'].mean(), high_fever['Temperature'].std())
axs[0,0].plot(hf_x, hf_y, label='High Fever')

axs[0,0].set_xlim(low_fever['Temperature'].min(),high_fever['Temperature'].max())
axs[0,0].legend()



axs[1,0].set_title("Lumbar Pain")
axs[1,0].hist(x = data['Lumbar Pain'], bins = 3 ,density=True)

axs[2,0].set_title("Micturition Pains")
axs[2,0].hist(x = data['Micturition Pains'], bins = 3 ,density=True)

axs[3,0].set_title("Inflamation of Bladder")
axs[3,0].hist(x = data['Inflamation of Bladder'], bins = 3 ,density=True)

axs[0,1].set_title("Nausea")
axs[0,1].hist(x = data['Nausea'], bins = 3 ,density=True)

axs[1,1].set_title("Urine Pushing")
axs[1,1].hist(x = data['Urine Pushing'], bins = 3 ,density=True)

axs[2,1].set_title("Burning of Urethra")
axs[2,1].hist(x = data['Burning of Urethra'], bins = 3 ,density=True)

axs[3,1].set_title("Inflamation of Renal Pelvis")
axs[3,1].hist(x = data['Inflamation of Renal Pelvis'], bins = 3 ,density=True)

plt.show()
