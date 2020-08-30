# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:27:28 2019

@author: GOVIND A M
"""

def bin_sch(bc,sch):
  start = 0
  end = len(bc)-1
  while True:
    n = end-start+1
    if n%2==0: