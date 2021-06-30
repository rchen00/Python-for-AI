# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 19:56:13 2021

@author: robert
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(10))
    
    
    