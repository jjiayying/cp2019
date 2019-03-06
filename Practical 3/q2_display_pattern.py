#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("number: "))
for row in range(1, n+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")


# In[ ]:




