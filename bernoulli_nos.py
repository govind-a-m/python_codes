# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:11:15 2019

@author: GOVIND A M
"""
from fractions import Fraction as Fr

def bernoulli2():
    A, m = [], 0
    while True:
        A.append(Fr(1, m+1))
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
        yield A[0] 
        m += 1
 
bn2 = [ix for ix in zip(range(61), bernoulli2())]
bn2 = [(i, b) for i,b in bn2 if b]
print(bn2)