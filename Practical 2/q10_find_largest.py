#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = 10

while n < 12000 ** (1/3):
  if n**3 < 12000:
    n = n + 1
  else:
    break

print(str(int(n-1)))


# In[ ]:




