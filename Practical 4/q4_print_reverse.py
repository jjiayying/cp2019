#!/usr/bin/env python
# coding: utf-8

# In[3]:


def reverse_int(n):
        sign = -1 if n < 0 else 1
        n *= sign

        while n:
            if n % 10 == 0:
                n /= 10
            else:
                break
        
        n = str(n)
        lst = list(n)
        lst.reverse()
        n = "".join(lst)
        n = int(n)
        return sign*n
    
print(reverse_int(234))
print(reverse_int(-234))


# In[ ]:




