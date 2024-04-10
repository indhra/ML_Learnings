# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:21:16 2022

@author: INDHRNA
"""

"""
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

from time import time
start = time()
import numpy as np
import sympy as sp
import pandas as pd

#%%%
if __name__ == '__main__':
# =============================================================================
#     method 1; using explicit for loop
# =============================================================================
    lis = []
    i = 0
    limit = 1000000
    counter = 10001
    for num in np.arange(limit):
        if sp.isprime(num):
            i +=1
            lis.append(num)
            if i==counter: break
    print(lis[-1])
# =============================================================================
#     method 2; using pandas, no explicit loop, internally cython uses loop
# =============================================================================
    df = pd.Series(np.arange(limit))
    dff = (df[df.apply(lambda x: sp.isprime(x))]).reset_index()
    print(dff.tail())

# =============================================================================
# method 3 ; direct method using sympy
# =============================================================================

    print(f'{counter}^nth prime value is : {sp.prime(counter)}')
    