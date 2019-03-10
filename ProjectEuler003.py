# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:05:13 2019

@author: Sahil
"""

import math


n = 600851475143
ans = 0
for i in range(2,int(math.sqrt(n))):
    while n%i==0:
        if n/i > 1:
            n = n/i
        elif n/i == 1:
            ans = n
            n = n/i
            print(n)
            break
    if i > n:
        break
print(ans)
