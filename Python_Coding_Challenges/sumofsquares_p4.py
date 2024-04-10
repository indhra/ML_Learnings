# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:26:35 2022

@author: INDHRNA
"""

"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.




"""

from time import time
start = time()
import numpy as np

#%%%

if __name__ == '__main__':
    value = 100 + 1
    sum_sqr = np.sum(np.square(np.arange(0,value)))
    sqr_sum  = np.square(np.sum(np.arange(0,value)))
    
    print(f'difference values is: {sqr_sum-sum_sqr} \n \
          time taken is: {round(time()-start,6)}')
