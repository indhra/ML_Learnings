# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:00:51 2022

@author: INDHRNA
"""

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from time import time
start = time()
import numpy as np
import pandas as pd
from numpy import arange, mod
from pandas import Series
#%%%

if __name__ == '__main__':
    
    numb = 1000
    lis = []
    numbers = arange(0,numb)
    
    lis = [(num) for count,num in enumerate(numbers) if (num%3==0) or (num%5==0) ]
        
    sume = np.sum((lis))
    print(sume)

    
    df  = Series(numbers)
    dff = df [(mod(df ,3)==0) | (mod(df ,5)==0)]
    print(dff.sum())

    
    print(f'time taken for execution is : {time()-start}')
