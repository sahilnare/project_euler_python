# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 01:37:06 2019

@author: Sahil
"""

num1 = 0
num2 = 1
sumo = 0

while((num1 + num2) < 4000000):
    temp = num2
    num2 = num2 + num1
    num1 = temp
    if num2%2 == 0:
        sumo += num2

print(sumo)