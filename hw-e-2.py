#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 12:24:52 2020

@author: robertchen
"""

print("how many Class A seats are sold?")
a=input()
print("how many Class B seats are sold?")
b=input()
print("how many Class C seats are sold?")
c=input()
print((a), "Class A seats,", (b), "Class B seats, and", (c), "Class C seats are sold")
income=int(a)*20+int(b)*15+int(c)*10
print("Total income generated from ticket sales is", (income))