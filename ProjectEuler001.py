# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:39:34 2019

@author: Sahil
"""

sumo = 0
for i in range(1,1000):
    if (i%3==0) or (i%5==0):
        sumo += i

print(str(sumo))