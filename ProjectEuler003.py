# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:05:13 2019

@author: Sahil
"""
'''
def isprime(test):
    for i in range(2,test):
        if test%i==0:
            return False
    return True

pri = 600851475143
copy=int(pri/2)+1
itr=0
for i in range(2,copy+1):
    if pri%i==0:
        if isprime(i):
            print(str(i))
'''
import math


n = 431465580
for i in range(2,int(math.sqrt(n))):
    while n%i==0:
        if n/i > 1:
            n = n/i
        else:
            break
print(n)