# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 10:27:02 2022

@author: INDHRNA
"""


"""
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

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
    limit = 2000000
    counter = 2000000
    for num in np.arange(limit+1):
        if sp.isprime(num):
            i +=1
            lis.append(num)
            # if i==counter: break
    print(np.sum(lis),' is sum of the primes below ',limit)
# =============================================================================
#     method 2; using pandas, no explicit loop, internally cython uses loop
# =============================================================================
    df = pd.Series(np.arange(limit))
    dff = (df[df.apply(lambda x: sp.isprime(x))]).reset_index()
    print(dff.sum())

# =============================================================================
# method 3 ; direct method using sympy
# =============================================================================

    print(f'sum of the primes below {counter} value is : {sum(sp.primerange(0, counter))}')
    