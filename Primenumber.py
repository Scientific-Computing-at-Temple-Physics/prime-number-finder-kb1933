# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:53:49 2018

@author: kiana
"""

x1 = raw_input('smallest number to check: ')
x2 = raw_input('largest number to check: ')

x1= eval(x1)
x2= eval(x2)
 


for x in range (x1,x2):
    for y in range (x1,x):
        if x % y == 0:
            break
    else: print x
      
      
    
