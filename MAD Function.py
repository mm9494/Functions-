#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 21:42:09 2020

@author: minamohammadi
"""

#Take in a set of numbers (of arbitrary size) and return the mean absolute deviation of this set. 
#Ideally, the function should be able to handle any format that this set is in (e.g. list, numpy array), but minimally we expect it to handle a 1D (column or row vector) numpy array as a default. 
#To make sure that you didn't just randomly download the function and that you understand scope, declare the variable writtenBy and assign your name as a value somewhere, but don't return/output this value.
#Make sure the function has a clear header as to what inputs the function assumes, what outputs it produces and when it was written.


import numpy as np
from numpy import mean, absolute
datalist = [1, 2, 3, 4, 5]
dataarray = np.array(datalist)

writtenBy = "Mina Mohammadi"

#Find mean value of datalist
M = mean(datalist)
print("Sample Mean Value =", mean(datalist))
print("\n")

#Calculate the absolute deviation 
#this is unnecessary
print("datalist-mean","", "deviation")
for i in range(len(datalist)):
    deviation = absolute(datalist[i]-M)
    print(datalist[i], "-", M, round(deviation),2)
   
#Find mean value of datalist
from numpy import mean, absolute
datalist = [1, 2, 3, 4, 5]
dataarray = np.array(datalist)
#Find mean value of the sample
M = mean(datalist)
print("Sample Mean Value =", mean(datalist))
print("\n")
sum = 0

#Calculate mean absolute deviation of datalist
for i in range(len(datalist)):
    deviation = absolute(datalist[i] - M)
    sum = sum + round(deviation,2)
print("Mean Absolute Deviation: " , sum/len(datalist))


#Calculate mean absolute deviation of dataarray
for i in range(len(dataarray)):
    deviation = absolute(dataarray[i] - M)
    sum = sum + round(deviation, 2)
print("Absolute Mean Deviation:" , sum/len(dataarray))


#MadFunction
datalist = [1, 2, 3, 4, 5]
dataarray = np.array(datalist)

def MadFunction(array):
    mysum = 0
    for i in range(array):
        findn = np.size(dataarray)
        mean = np.mean(dataarray)
        deviation = (i - mean)
        absolute = mysum + absolute(deviation)
        mad = Absolute/findn
        print ("mad solution:" , mad)

MadFunction(datalist)

        
        
        





