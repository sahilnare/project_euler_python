# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:05:13 2019

@author: Sahil
"""

import math


n = 431465580
for i in range(2,int(math.sqrt(n))):
    while n%i==0:
        if n/i > 1:
            n = n/i
        else:
            break
print(n)