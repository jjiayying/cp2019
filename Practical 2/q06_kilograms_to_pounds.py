#!/usr/bin/env python
# coding: utf-8

# In[3]:


def kilo_to_pounds(limit):
    print("Kilogram","\t","Pounds")
    for i in range(limit):
        print("{0}{2} {1:.1f}".format(i+1,(i+1)*2.2,"\t\t"))
        
kilo_to_pounds(10)


# In[ ]:




