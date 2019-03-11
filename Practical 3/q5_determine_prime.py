#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status

count = 0
n = 2 

while count!=1000:
    for n in range(1,1001):
        if is_prime(n):
            if count%10==0:
                print()
            print(n,end=" ")
            count+=1
        n+=1


# In[ ]:




