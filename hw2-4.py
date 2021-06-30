# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:38:42 2021

@author: robert
"""

def main():

    f = open("number_list.txt", "r")
# content=f.read()
# print(content)

    fl = f.readlines()
    for x in (fl):
        print(x)
           
if __name__=="__main__":
    main()