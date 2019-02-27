#!/usr/bin/env python
# coding: utf-8

# In[3]:


year = int(input("enter year here: "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("leap")
else:
    print ("not leap")


# In[ ]:




