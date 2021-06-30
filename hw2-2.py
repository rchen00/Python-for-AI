# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:56:21 2021

@author: robert
"""

f = open("my_name.txt", "r+")
content= f.read()
print(content)
f.close()
