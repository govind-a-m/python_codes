# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:19:12 2019

@author: GOVIND A M
"""

n = 8
k = 2

if n%(2*k)== 0:
  sign = k
  result = ''
  cnt = 0
  for i in range(1,n+1):
    result = result+str(i+sign)+' '
    cnt = cnt+1
    if cnt==k:
      sign = -sign
      cnt = 0
  print(result)
else:
  print(-1)