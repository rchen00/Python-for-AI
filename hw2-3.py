# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:02:16 2021

@author: robert
"""

f = open("number_list.txt","w+")
for i in range (100):
    f.write(" %d\r" % (i+1))  
f.close()


    