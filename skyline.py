# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:09:47 2019

@author: GOVIND A M
"""
#arr = [8979,4570,6436,5083,7780,3269,5400,7579,2324,2116]
#arr = [5,4,3,2,1,2,3,4,5]
arr = [11,11,10,10,10]
lena = len(arr)
nfgt_arr = [1]*lena
ptr = [0]*lena
endup = [0]*(lena+1)
ptr[-1] =  lena
for i in range(lena-2,-1,-1):
  j = i+1
  while j<lena:
    if arr[j]>arr[i]:
      nfgt_arr[i] = nfgt_arr[i]+nfgt_arr[j]
      ptr[i] = ptr[j]
      j = ptr[j]
    elif arr[j]<arr[i]:
      ptr[i] = j
      endup[j]+=1
      k = ptr[j]
      while k<lena:
        endup[k]+=1
        k = ptr[k]
      break
    else:
      nfgt_arr[i] = nfgt_arr[i]+nfgt_arr[j]
      ptr[i] = ptr[j]
      endup[j]+=1
      k = ptr[j]
      while k<lena:
        endup[k]+=1
        k = ptr[k]
      break
mx = arr[0]*(nfgt_arr[0]+endup[0])
for i in range(1,lena):
  prd = arr[i]*(nfgt_arr[i]+endup[i]) 
  if prd>mx:
    mx = prd 
print(mx)