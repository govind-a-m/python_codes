# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:09:42 2020

@author: MLG1KOR
"""

import socket
import pickle
import time


port = 1235
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',port))
s.listen(5)
print('listening')
c,addr = s.accept()
while True:
  msg = c.recv(4096)
  try:
    print(len(msg))
    data = pickle.loads(msg[:-10])
    print(data['log'][0])
  except:
    print('error')
  time.sleep(0.05)

