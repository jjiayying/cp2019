#!/usr/bin/env python
# coding: utf-8

# In[2]:


def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return m % n
        
gcd(24, 16), gcd(25, 225)


# In[ ]:




