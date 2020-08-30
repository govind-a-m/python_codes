# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:07:23 2019

@author: GOVIND A M
"""
import math
import sys

def permute(na,nb):
  return math.factorial(na+nb)//(math.factorial(na)*math.factorial(nb))

def allowed(na,nb,perms):
  global mxna,mxnb,remove
  if na>nb:
    remove = remove+perms
    return 
  else:
    if na!=0:
      allowed(na-1,nb,perms*na//(nb+na))
    if nb!=0:
      allowed(na,nb-1,perms*nb//(nb+na))

mxna = 25679
mxnb = 51358
total = permute(mxna,mxnb)
remove = 0
allowed(mxna,mxnb,total)