# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:26:14 2019

@author: Sahil
"""

def sum_square(i):
    sm = 0
    for a in range(1,i+1):
        sm += a
    return sm**2

def square_sum(j):
    sq = 0
    for b in range(1,j+1):
        sq += b**2
    return sq

smurf = sum_square(100) - square_sum(100)
print(smurf)