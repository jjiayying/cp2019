#!/usr/bin/env python
# coding: utf-8

# In[1]:


def m_series(i):
    sum_series=0
    for i in range(20):
        sum_series+=(i+1)/(i+2)
        print(i+1,"\t","{:.4f}".format(sum_series))
        
m_series(1)


# In[ ]:




