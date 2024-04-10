# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:14:14 2022

@author: INDHRNA
"""
"""
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from time import time
start = time()
import numpy as np

#%%%

if __name__ == '__main__':
    NUMBER = 20
    VALUE = 2520
    lis = []
    for num in np.arange(NUMBER):
        lis.append(VALUE%num)