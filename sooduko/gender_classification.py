#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:53:47 2017

@author: dhingratul

Gender Classification based on llSourcell as part of a tutorial
Parameter :
    Input : X : [height, weight, shoe_size] pairs for each data point
            Y : Labels corresponding to each data point
    Output :    Predcition : Male/Female
"""
from sklearn import tree


def PredictDT(X, Y, test_vector):
    # Model
    model = tree.DecisionTreeClassifier()
    # Data Fitting
    model = model.fit(X, Y)
    # Prediction
    return model.predict(test_vector)

# Data
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
# Labels
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

print(PredictDT(X, Y, [[190, 70, 43]]))
