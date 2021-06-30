#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:00:55 2020

@author: robertchen
"""
print("Please enter the follwoing.")
print("what is the loan payment?", end=' ')
loan_payment=input()
print("what is the insurance?",end=' ')
insurance=input()
print("how much is for gas?",end=' ')
gas=input()
print("how much is for tires?",end=' ')
tires=input()
print("how much is for maintenance?",end=' ')
maintenance=input()
monthly=int(loan_payment)+int(insurance)+int(gas)+int(tires)+int(maintenance)
print("monthly total is", monthly)
print("yearly total is", monthly*12)


