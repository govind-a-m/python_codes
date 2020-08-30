# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:06:49 2019

@author: MLG1KOR
"""

arr = [2,1,3,1,2]
lena = len(arr)
gt_arr = [0 for _ in range(lena)]
gt_arr[0] = 0 
total = 0

def get_gt(i):
  global gt_arr
  nfgt = 0
  for j in range(i-1,-1,-1):
    if arr[j]>arr[i]:
      nfgt = nfgt+1
    elif arr[j]==arr[i]:
      gt_arr[i] = gt_arr[j]+nfgt
      return gt_arr[i]
  gt_arr[i] = nfgt
  return gt_arr[i]     
#def get_gt(i):
#  global gt_arr
#  nfgt = 0
#  for j in range(i-1,-1,-1):
#    if arr[j]>arr[i]:
#      if gt_arr[j]==0:
#        nfgt = nfgt+1
#      else:
#        gt_arr[i] = gt_arr[j]+nfgt+1
#        return gt_arr[i]
#    elif arr[j]==arr[i]:
#      gt_arr[i] = gt_arr[j]+nfgt
#      return gt_arr[i]
#  gt_arr[i] = nfgt
#  return gt_arr[i]       

for i in range(1,lena):
  total = total+get_gt(i)
print(total)


