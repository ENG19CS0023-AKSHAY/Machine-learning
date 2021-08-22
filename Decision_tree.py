#decission tree
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
X = [[30],[40],[50],[60],[20],[10],[70]]
y = [0,1,1,1,0,0,1]
RandomForestRegModel = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
RandomForestRegModel.fit(X,y)
a=float(input('Enter marks:'))
X_marks=[[a]]
print(RandomForestRegModel.predict(X_marks))
