import matplotlib.pyplot as plt

#dataset
data = [22,25,27,28,30,32,35,38,40,75]

#create box plot
plt.figure(figsize=(10,6))
plt.boxplot(data,vert=False)
plt.title('Employee Ages - Box Plot')
plt.xlabel('Age')
plt.grid(True, alpha=0.3)
plt.show()

#Outliers appear as dots
#beyond the whiskers!