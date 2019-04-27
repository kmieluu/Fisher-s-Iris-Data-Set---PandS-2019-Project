import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 
import seaborn as sns

#Read data from iris_csv.csv
csv = pd.read_csv("Input/iris_csv.csv")

#Show the first 10 lines of the dataset
print(csv.head(10))

#show how many expositions per class
print(csv.groupby('class').size())

#point location of categories
setosa = csv[0:50]
versicolor = csv[50:100]
virginica = csv[100:150]

print('----------------------Iris Setosa Values----------------------')
print(setosa.describe())
print('----------------------Iris Versicolor Values----------------------')
print(versicolor.describe())
print('----------------------Iris Virginica Values----------------------')
print(virginica.describe())

summary = csv.describe()
summary = summary.transpose()
print(summary.head())


#Univariate box and whisker plots
csv.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

csv.hist()
plt.show()



csv.plot.scatter(x="sepallength", y="sepalwidth")
plt.show()


csv.plot.scatter(x="petallength", y="petalwidth")
plt.show()

#Multivariate scatter plot matrix

sns.set(style='darkgrid')
sns.distplot(setosa['sepallength'], color='b', kde=False, label='Setosa')
sns.distplot(versicolor['sepallength'], color='y', kde=False, label='Versicolor')
sns.distplot(virginica['sepallength'], color='g', kde=False, label='Virginica')
plt.legend()
plt.title('Quantity of Sepal Lengths')
plt.xlabel('Sepal Length (cm)')  
plt.ylabel('Quantity')
plt.show()


sns.set(style='darkgrid')
sns.distplot(setosa['petallength'], color='b', kde=False, label='Setosa')
sns.distplot(versicolor['petallength'], color='y', kde=False, label='Versicolor')
sns.distplot(virginica['petallength'], color='g', kde=False, label='Virginica')
plt.legend()
plt.title('Quantity of Petal Lengths')
plt.xlabel('Petal Length [cm]')  
plt.ylabel('Quantity')
plt.show()

![Seaborn](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/seaborn.png)



#Re-create the above plot, but this time plot the setosa data points in red, the versicolor data point in green,
# and the virginica data points in blue.
# Setosa, versicolor, and virginica are the three possible values of the species variable. 
# Add a legend to the plot showing which species is in which colour.

#Use the seaborn library to create a scatterplot matrix of all five variables.