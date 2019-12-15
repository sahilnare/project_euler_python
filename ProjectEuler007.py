# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:32:08 2019

@author: Sahil
"""

def find_prime(x):
    c = 0
    for i in range(2,int(x/2)+1):
        if x%i == 0:
            c += 1
            break
    return c



l = 0
j = 2
while True:
    k = find_prime(j)
    if k==0:
        l += 1
        if (l==10001):
            print(j)
            break
    j += 1
        


        
