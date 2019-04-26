import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 

#Read data from iris_csv.csv
data = pd.read_csv("Input/iris_csv.csv")

#Show the first 10 lines of the dataset
print(data.head(10))

#show how many expositions per class
print(data.groupby('class').size())

#point location of categories
setosa = data[0:50]
versicolor = data[50:100]
virginica = data[100:150]

print('----------------------Iris Setosa Values----------------------')
print(setosa.describe())
print('----------------------Iris Versicolor Values----------------------')
print(versicolor.describe())
print('----------------------Iris Virginica Values----------------------')
print(virginica.describe())

summary = data.describe()
summary = summary.transpose()
print(summary.head())


#Re-create the above plot, but this time plot the setosa data points in red, the versicolor data point in green,
# and the virginica data points in blue.
# Setosa, versicolor, and virginica are the three possible values of the species variable. 
# Add a legend to the plot showing which species is in which colour.

#Use the seaborn library to create a scatterplot matrix of all five variables.