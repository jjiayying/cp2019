#!/usr/bin/env python
# coding: utf-8

# In[9]:


x = int(input("side 1: "))
y = int(input("side 2: "))
z = int(input("side 3: "))

if (x + y < z) or (y + z < x) or (x + z < y):
    print("perimeter = " + str(x+y+z))
else: 
    print("invalid traingle")


# 
