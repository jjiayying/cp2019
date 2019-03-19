#!/usr/bin/env python
# coding: utf-8

# In[7]:


def find_num_uppercase(str):
    return sum(1 for c in str if c.isupper())

find_num_uppercase('Good MorninG!')


# In[ ]:




