# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:52:07 2019

@author: Sahil
"""


fibo = [0,1]
i = 2
sumo = 0

while((fibo[i-1] + fibo[i-2]) < 4000000):
    fibo.append(fibo[i-1] + fibo[i-2])
    if fibo[i]%2 == 0:
        sumo += fibo[i]
    i+=1


print(sumo)
