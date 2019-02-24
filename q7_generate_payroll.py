#!/usr/bin/env python
# coding: utf-8

# In[14]:


name = str(input("name : "))
weekly = float(input("number of hours worked weekly : "))
pay = float(input("hourly pay rate : "))
contribution = float(input("CPF contribution rate(%): "))

gross = weekly * pay
cpf20 = contribution / 100 * 20
net = gross - cpf20

print("Payroll statement for " + name)
print("Number of hours worked in week: " + str(weekly))
print("Hourly pay rate: " + str(pay))
print("Gross pay = " + str(gross))
print("CPF contribution at 20% = " + str(cpf20))
print("Net pay = " + str(net))


# In[ ]:




