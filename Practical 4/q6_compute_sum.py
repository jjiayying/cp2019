#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_digits(n):
    if n == 0:
        return n
    else:
        return n%10 + sum_digits(n//10)

sum_digits(123)


# In[ ]:




