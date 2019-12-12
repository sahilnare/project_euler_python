# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 02:19:53 2019

@author: Sahil
"""


def find_gcd(a,b):
    gcd = 1
    for i in range(2,min(a,b)):
        while a%i==0 and b%i==0:
            a = a/i
            b = b/i
            gcd = gcd*i
    return gcd

ans = 1

for k in range(1,11):
    ans = int((ans*k)/(find_gcd(ans,k)))

print(ans)
