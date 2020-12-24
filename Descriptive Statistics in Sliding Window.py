#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:49:29 2020

@author: minamohammadi
"""


import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = np.array(data)

#deining funciton and setting parameters
def E3function(data, flag, window):
    res = []
    #mean of every range of window value
    for i in range(0, len(dataset) - window):
        arraywindow = dataset[i:i + window]
        mean = np.mean(arraywindow)
        res.append(mean)
   
    if flag == 2:
        for i in range(0, len(dataset) - window):
            #STD for every range of window value
            arraywindow = dataset[i:i + window]
            StandardDeviation = np.std(arraywindow)
            res. append(StandardDeviation)
            
    if flag == 3:
        if len(dataset) == 2:
            #corr for every range of window value
            firstarray = dataset[0]
            secondarray = dataset[1]
            for i in range(0, len(dataset[0]) - window):
                arraywindowone = firstarray[i:i + window]
                arraywindowtwo = secondarray[i:i + window]
                correlation = np.corrcoef(arrayWindowOne, arrayWindowTwo)
                res. append(thecorrelation)
            
            print(res)
            return(res)