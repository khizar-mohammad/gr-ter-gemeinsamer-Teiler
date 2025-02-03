#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ggt_multi(zahlenliste):
  ggt_result = zahlenliste[0]
  for i in range(1,len(zahlenliste)):
    ggt_result = ggt(ggt_result,zahlenliste[i])
  return ggt_result

def ggt(a,b):
  while b!=0:
    x = a
    a = b
    b = x % b
  return a

print(ggt_multi([12,18, 24,60,965472]))

