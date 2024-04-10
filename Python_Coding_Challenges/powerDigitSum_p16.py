# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 09:37:21 2022

@author: INDHRNA
"""
"""
Power digit sum
 
 
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

"""

from time import time
start = time()
import numpy as np

#%%%

if __name__ == '__main__':
    NUMBER = 2**1000
    ns = str(NUMBER)
    nsl = list(map(int,ns.strip()))
    print(f' sum of digits in a number is : {sum(nsl)}')