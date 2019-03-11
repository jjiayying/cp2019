#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def print_matrix(n):
    for i in range(n):
        for j in range(n):
            print(random.randint(0,1),end=" ")
        print()

print_matrix(3)


# In[ ]:




