# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:44:47 2019

@author: GOVIND A M
"""

def binary_search(strt,end,val,a):
  while True:
    n = end-strt+1
    print(n)
    if n%2==0:
      if a[int((n/2))-1]<val<a[int(n/2)]:
        return n/2
      else:
        if val<a[int(n/2)]:
          strt = strt
          end = int((n/2)-1)
        else:
          strt = int(n/2)
          end = end
    else:
      print((n-1)/2)
      if val<a[int((n-1)/2)]:
        if a[int((n-3)/2)]<val:
          return (n-1)/2
        else:
          end = int((n-3)/2)	
          strt = strt
      else:
        if val<a[int((n+1)/2)]:
          return (n+1)/2
        else:
          strt = int((n+1)/2)
          end = end 

if __name__=="__main__":
  a = [1,1,2,2,3]
  strt = 0
  end = 4
  val = 1.9
  print(binary_search(strt,end,val,a))