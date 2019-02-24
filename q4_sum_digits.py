#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x = int(input("number : "))
total = 0
while (x > 0):
    dig = x % 10
    total = total + dig
    x = x // 10
print("Total : " + str(total))

