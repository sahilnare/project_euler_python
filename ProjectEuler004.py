# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 01:52:44 2019

@author: Sahil
"""

def palin(num):
    a = 0
    p = 0
    g = 0
    dup1 = num
    dup2 = num
    c = 0
    
    while dup2>0:
        dup2 = dup2//10
        c += 1
    
    while num>0:
        a = num%10
        g += 1
        p += a*(10**(c-g))
        num = num//10
    
    if p == dup1:
        return True
    else:
        return False


n = 0
maxpal = 0

for i in range(100,1000):
    for j in range(100,1000):
        n = i*j
        if palin(n):
            if n > maxpal:
                maxpal = n

print(maxpal)
        