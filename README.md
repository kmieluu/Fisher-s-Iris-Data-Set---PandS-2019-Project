# Fisher's Iris data set
## This is repository that contains my solution to the Fisher's Iris Data Set 
## [*To Download Instructions, please click here*](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

## How to download this repository  

1. [Go to GitHub](https://github.com/kmieluu)
2. [Go into Fisher's Iris Data Set - PandS 2019 Project](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project)
3. Click the "Clone or download" button and select Download ZIP

## How to run the code

1. Make sure you have Python installed (via Anaconda for example)
2. Open commander
3. Make sure you are in the right directory
4. Run python code by typing iris.py


The Iris Data Set data set is showing multiple outcomes containing of variations received from combinations of sepals and petals of Irises: Setosa, Versicolor and Virginica.


### Class:
    - Iris Setosa
    - Iris Versicolour
    - Iris Virginica


![KWIATKI](https://user-images.githubusercontent.com/47505151/56806631-625ec480-6824-11e9-9108-665023156900.PNG)

![SepalPetal](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/sepalpetal.png)

The Iris data set is a database that was originally created by R.A.Fisher in 1936 paper called *The use of multiple measurments in taxonomic problems*. It contains 3 types of Iris flowers with their multiple collection of 4 attributes.

### Attribute Information: 
    •	The length of sepals [cm]
    •	The width of sepals [cm]
    •	The length of petals [cm]
    •	The width of petals [cm]

## Data Investigation

Import required modules into Python.

![Modules](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/modules.PNG)

Import Iris data set into python.

Check first 10 rows of the data set:

![Iris Data Set](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/IrisTop10.PNG)

Length and width of all the data.
Petal is smaller then settal and more condensed. Sepal can vary more.

![all data](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/petalsetallengthgraph.png)

Class distribution.
To better understand the data we can check how many examples of data per class there is.
<br>

![Number of Instances](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/NoI.PNG)

Highlight the information about the data using describe funciton in python to see the summary of each attribute.
![Describe Attributes](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/attrdescr.PNG)

Below is information about each of species. 
We can interprete what's below as follows:
Iris Setosa sepal length 
* measured 50 times
* on average the length was about 5cm long (with minimum value 4.3cm and maximum 5.8cm)
* standard deviation of the observation is 35.25%
* Given percentile values (quantile 1, 2 and 3 respectively) of all numeric values in a column (or series)

![Information](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/Informationaboutdata.PNG)



##  Visualisation of Data

Having the data imported to better analyze it and understand the meaning of it we can use various visualisations.

Here we will look at 2 types of plots:
- Univariate plot to better understand each attribute
- Multivariate plot to better understand relationships between attributes.

### Univariate Plots
Gives clearer idea about the distribution of values between attributes.
![Univariate](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/Univariate.PNG)

Please see the histagram view on the same univariate dataset below:
<br>

![UnivariateHist](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/UnivariateHist.PNG)

We can see lenght of petal and sepals but with no diversification between classes (type of iris).

### Multivariate Plots
Please see the relationships between variables in below graph:

![Seaborn](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/seaborn.png)

From above table we can see that:
* In most cases Sepal lengths are shortest for Setosa and longest for Virginica, still there are cases where Virginica and Setosa length could be the same
* Petal length for Setosa is much smaller then Versicolor or Virginica. Virginica would always have longer Petal then even largest Sepal. Small population of Virginica and Versicolor would have the same lenth of petal.


![Seabornwidth](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/seabornwidth.png)

* Sepal width most likely are longest for Setosa and shortest for Versicolor, still there are cases where Versicolor and Setosa width could be the same. Virginica is between. 
* Petal width for Setosa is much smaller then Versicolor or Virginica. Virginica would always have longer Petal then even largest Sepal. Small population of Virginica and Versicolor would have the same width of petal.


ViolinPlot 

Shows the distribution of quantitative data across several levels of one (or more) categorical variables (width and length) such that those distributions can be compared. We use module Seaborn.


![ViolinLength](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/ViolinLength.PNG)

* Smallest discrepancies in lengths presents petal length in Iris setosa. We can assume the length will vary here between 1-2 cm. 
* Highest discrepancies in length we see on sepal length for iris virginica. In scale can be anything between 4-8cm.


![ViolinWidth](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/ViolinWidth.PNG)

* Sepal width looks to be most common category for all classes. 
* Petal width vary less for iris setosa and most for iris virginica

ScatterPlot

![ScatterPlot](https://github.com/kmieluu/Fisher-s-Iris-Data-Set---PandS-2019-Project/blob/master/Images/pairplot.PNG)


## References

- [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Iris)
- [kaggle.com](https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis)
- https://github.com/RitRa/Project2018-iris
- https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
- [Seaborn](https://seaborn.pydata.org/introduction.html)
- [Conda.io](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)
- [How to make scatter plot in python - youtube](https://www.youtube.com/watch?v=TexdD7t0IKU)
- [ViolinPlots](http://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot)
- [Numerical Python](https://www.tutorialspoint.com/numpy)
- https://backtobazics.com/python/pandas-describe-method-dataframe-summary/
- [ScatterPlot](https://scipy-lectures.org/packages/scikit-learn/auto_examples/plot_iris_scatter.html)
- [PairPlot](https://mylearningsinaiml.wordpress.com/2018/11/21/pair-plots/)
