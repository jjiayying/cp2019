#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
n = math.sqrt(12000)

while n > 0:
  if n*n > 12000:
    break
  else:
      n = n + 1

print(str(int(n+1)))


# In[ ]:




