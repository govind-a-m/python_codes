# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:32:36 2019

@author: GOVIND A M
"""
import math

def permute(na,nb):
  return math.factorial(na+nb)/(math.factorial(na)*math.factorial(nb))

mx = 2
s = 'a'
na = 0
nb = 0
index = -1
remove = 0
while True:
  s = s+'a'
  index = index+1
  na+=1
  if na>mx:
    s = s[:index-1]+'b'
    nb = nb+1
    if nb==2*mx:
      idx = index-1
      while s[idx]=='b':
        idx+=-1
      nb = nb-index-idx-1
      index = idx
      s = s[:index]+'b'
      nb = nb+1
  else:
    if na>nb:
      remove = remove+permute(mx-na,2*mx-nb)
      s = s[:index]+'b'
      na = na-1
      nb = nb+1

    
 
    