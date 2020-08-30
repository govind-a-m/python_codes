# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:04:40 2019

@author: GOVIND A M
"""
arr = [2,1,3,1,2]
lena = len(arr)
les = [-1 for _ in range(lena)]

def lesser_than(i):
	if les[i+1]!=-1:
		if arr[i+1]==arr[i]:
			
	else:
		if arr[i+1]<arr[i]:
			result = lesser_than[i+1]
			les[i] = result[0]+result[1]
		elif arr[i+1]==arr[i]:
			les[i] = lesser_than[i+1][1]
			
for i in range(lena):
	if les[i]==-1:
		lesser_than(i)
