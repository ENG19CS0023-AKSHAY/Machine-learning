#Linear Regression
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
height=[[4],[5],[6],[7],[8],[9],[10]]
weight=[  8, 10 ,12 , 14, 16, 18, 20]
plt.scatter(height,weight,color='blue')
plt.xlabel("height")
plt.ylabel("weight")
reg=linear_model.LinearRegression()
reg.fit(height,weight)
a=float(input('Enter number:'))
X_height=[[a]]
print(reg.predict(X_height))
