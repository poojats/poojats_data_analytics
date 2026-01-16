import numpy as np

#dataset
data = [22,25,27,28,30,32,35,38,40,75]

#calculate Q1, Q3
Q1 = np.percentile(data,25,method='nearest')
Q3 = np.percentile(data,75,method='nearest')

#calculate IQR
IQR = Q3 - Q1

#set fences
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

#find outliers
outliers = [x for x in data
            if x<lower or x>upper]

print(f"Q1: {Q1}, Q3: {Q3}")
print(f"IQR: {IQR}")
print(f"Fences: [{lower},{upper}]")
print(f"Outliers: {outliers}")
