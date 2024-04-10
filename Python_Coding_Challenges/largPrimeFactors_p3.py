# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 20:50:52 2022

@author: INDHRNA
"""

"""

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

from time import time
start = time()
import sympy as sp


#%%%


if __name__ == '__main__':

    VALUE = 600851475143
    pFactors = sp.primefactors(VALUE)
    
    print(f'largest prime factor of {VALUE} is {pFactors[-1]} \n time taken is {round(time()-start,6)}')
