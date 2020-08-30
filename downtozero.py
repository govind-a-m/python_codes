# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 19:41:46 2019

@author: GOVIND A M
"""
from collections import defaultdict
import math

n = 20
d = defaultdict(int)
cnt = 0
d[2] = 2
d[3] = 3
def downtozero(n):
  if n in d:
    print(n,d[n])
    return d[n]
  else:
    mn = pow(n,0.5)
    print(mn)
    if mn==math.floor(mn):
      d[n] = downtozero(mn)+1
      print(n,d[n])
      return d[n]
    else:
      mn = math.floor(mn)
      if mn*(mn+1)==n:
        d[n] =  downtozero(mn+1)+1
        print(n,d[n])
        return d[n]
      elif mn*(mn+1)<n:
        d[n] =  downtozero(mn+1)+n-mn*(mn+1)
        print(n,d[n])
        return d[n]      
      else :
        d[n] = downtozero(mn)+n-mn*mn
        print(n,d[n])
        return d[n]
print(downtozero(29))