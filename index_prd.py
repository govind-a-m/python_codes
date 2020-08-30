# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:36:10 2019

@author: GOVIND A M
"""

arr = [11,11,10,10,10,11,12]
arr.insert(0,0)
lena = len(arr)
right = [0]*lena
left = [0]*lena

for i in range(2,lena):
  j = i-1
  while j>0:
    if arr[j]>arr[i]:
      left[i] = j
      break
    elif arr[j]<arr[i]:
      right[j] = i
      j = left[j]
    else:
      j = left[j]
  