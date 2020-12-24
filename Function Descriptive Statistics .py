#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:05:52 2020

@author: minamohammadi
"""
#Take in a 1D numpy array of arbitrary length (as a default - you can make it more flexible if you also want it to be able to accommodate a list, but that is not necessary - you will get full credit if it can "just" handle the 1D numpy array as an argument/input).
#Compute the Mean, Median, Standard deviation, Mean Absolute Deviation and n (length) of the input array. You can use pre-existing functions (e.g. from numpy) to do this, write your own, or use functions you wrote previously, like the MAD function for E1. In addition, also compute the standard error of the mean (SEM) as the standard deviation divided by the square root of n (which you just computed). We will explain what the standard error of the mean is and why it matters in the lecture on sampling.
#Returns as an output a 1D numpy array with 6 elements, representing the Mean, Median, Standard Deviation, MAD, n and SEM that you computed in 2), in this order.
#Make sure the function has a clear header (a block of comments at the beginning) outlining what inputs the function assumes, what outputs it produces and when (date is fine) it was written by you (this is a good habit).

import numpy as np
#importing mean, absolute from numpy
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = np.array(data)

writtenBy: "Mina Mohammadi"


def DSfunction(dataarray): #take the array as an input
    mean = np.mean(dataarray)
    median = np.median(dataarray)
    STD = np.std(dataarray)
    n = len(datarray)
    SEM = STD/np.sqrt(n)
    MAD = 0
    for i in range(dataarray):
        MAD += mean(absolute([i] - mean(dataarray)))
    print('mean is' , mean)
    print('median is', median)
    print('STD is' , STD)
    print('n is' , n)
    print('SEM is', SEM)
    print('MAD is', MAD)

DSfunction(A)
