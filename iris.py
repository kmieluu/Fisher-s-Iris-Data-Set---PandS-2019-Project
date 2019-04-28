# Agata Chmielowiec, 2019
# Programming and scripting 2019 project

#Modules that will be used in this project are:
#In order to create graphs
import matplotlib.pyplot as plt
#For data analysis 
import pandas as pd
#Numerical Python
import numpy as np 
#data visualization library based on matplotlib
import seaborn as sns
#for scatterplot
from sklearn.datasets import load_iris

#Read data imported to github, folder "Input"
csv = pd.read_csv("Input/iris_csv.csv")

#Show the first 10 lines of data imported(iris_csv.csv)
print(csv.head(10))

#Each flower was measured 50 times.
print(csv.groupby('class').size())

#point location of categories
setosa = csv[0:50]
versicolor = csv[50:100]
virginica = csv[100:150]


print('Iris Setosa Values')
print(setosa.describe()) 
print('Iris Versicolor Values')
print(versicolor.describe())
print('Iris Virginica Values')
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

sns.set(style='darkgrid')
sns.distplot(setosa['sepalwidth'], color='b', kde=False, label='Setosa')
sns.distplot(versicolor['sepalwidth'], color='y', kde=False, label='Versicolor')
sns.distplot(virginica['sepalwidth'], color='g', kde=False, label='Virginica')
plt.legend()
plt.title('Quantity of Sepal Width')
plt.xlabel('Sepal Width (cm)')  
plt.ylabel('Quantity')
plt.show()


sns.set(style='darkgrid')
sns.distplot(setosa['petalwidth'], color='b', kde=False, label='Setosa')
sns.distplot(versicolor['petalwidth'], color='y', kde=False, label='Versicolor')
sns.distplot(virginica['petalwidth'], color='g', kde=False, label='Virginica')
plt.legend()
plt.title('Quantity of Petal Width')
plt.xlabel('Petal Width [cm]')  
plt.ylabel('Quantity')
plt.show()

#ViolinPlot
sns.set(style="white")
sns.violinplot(x='class', y='sepallength', linewidth = 3, palette=['y', 'b', 'r'], data=csv, inner=None)
sns.swarmplot(x='class', y='sepallength', data=csv, color='green', edgecolor='yellow', size=4)
plt.title('Density Plot of Species Sepal Length')
plt.ylabel('Sepal Length (cm)')
plt.show()

sns.set(style="white")
sns.violinplot(x='class', y='petallength', linewidth = 3, palette=['y', 'b', 'r'], data=csv, inner=None)
sns.swarmplot(x='class', y='petallength', data=csv, color='green', edgecolor='yellow', size=4)
plt.title('Density Plot of Species Petal Length')
plt.ylabel('Petal Length (cm)')
plt.show()

sns.set(style="dark")
sns.violinplot(x='class', y='sepalwidth', linewidth = 5, palette=['y', 'b', 'r'], data=csv, inner=None)
sns.swarmplot(x='class', y='sepalwidth', data=csv, color='green', edgecolor='yellow', size=4)
plt.title('Density Plot of Species Sepal Width')
plt.ylabel('Sepal Width (cm)')
plt.show()

sns.set(style="dark")
sns.violinplot(x='class', y='petalwidth', linewidth = 5, palette=['y', 'b', 'r'], data=csv, inner=None)
sns.swarmplot(x='class', y='petalwidth', data=csv, color='green', edgecolor='yellow', size=4)
plt.title('Density Plot of Species Petal Width')
plt.ylabel('Petal Width (cm)')
plt.show()

#PairPlot
sns.set_style("whitegrid")
sns.pairplot(hue='class', markers="<", data = csv, diag_kind = 'kde')
plt.show()

#ScatterPlot

df = sns.load_dataset("Input/iris_csv.csv")



#Re-create the above plot, but this time plot the setosa data points in red, the versicolor data point in green,
# and the virginica data points in blue.
# Setosa, versicolor, and virginica are the three possible values of the species variable. 
# Add a legend to the plot showing which species is in which colour.

#Use the seaborn library to create a scatterplot matrix of all five variables.