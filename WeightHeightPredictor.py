# import libraries to add dataset
import numpy as np
import pandas as pd

# add the CSV dataset 
dataset=pd.read_csv("height-weight.csv")
dataset.head()

# check if dataset is missing values, check column name, and dimension
dataset.isna().any()
dataset.columns
dataset.shape

# find correlation between weight and height 
dataset.corr()

# independent variable in 2 dimension array
height = dataset.Height.values[:, np.newaxis]
height 

# dependent variable in 1 dimension array
weight = dataset.Weight.values
weight

# find min max of variables 
Heightmin=height.min()
Heightmax=height.max() 
Weightmin=weight.min()
Weightmax=weight.max()

# VariableNormal=(Variable-VariableMin)/(VariableMax-VariableMin)
Heightnorm=(height-Heightmin)/(Heightmax-Heightmin)
Heightnorm
Weightnorm=(weight-Weightmin)/(Weightmax-Weightmin)
Weightnorm

# apply Linear Regression Model 
import sklearn.linear_model as lm; lr=lm.LinearRegression(); lr.fit(height,weight)

# find value of weight in correspondence to height value 
knownvalue=int(input("Enter height value:"))
findvalue=lr.predict([[knownvalue]])
print("Weight value is",findvalue, "when the height value is",knownvalue)

# predicted value inserted to dataset
dataset["predicted_value"] = lr.predict(height)
dataset.head()

# calculate model score
from sklearn.metrics import r2_score
accuracy = r2_score(weight, lr.predict(height))
print("The model accurary score is", accurary * 100, "%")
