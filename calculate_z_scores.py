import numpy as np
from scipy import stats

#dataset
data = [22,25,27,28,30,32,35,38,40,75]

#calculate Z-scores
z_scores = np.abs(stats.zscore(data))

#threshold (typically 3)
threshold = 3

#find outliers
outliers = []
for i,z in enumerate(z_scores):
    if z > threshold:
        outliers.append(data[i])
        
print(f"Z-scores:", z_scores)
print(f"outliers: {outliers}")