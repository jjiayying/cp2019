#!/usr/bin/env python
# coding: utf-8

# In[7]:


number_of_students = int(input("number of students: "))

y = []
z = []

for x in range(number_of_students):
    y = input("Name: ")
    z = z.split(input("Score: "))

z.sort()

print(z[-1])   
print(z[-2])


# 
