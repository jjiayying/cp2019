#!/usr/bin/env python
# coding: utf-8

# In[2]:


def miles_to_kilo(mile1,mile2,kilo1,kilo2):
    print("Miles Kilometres Kilometres Miles")
    for i in range(mile1-1,mile2):
        #\t
        size_a=6-len(str(i+1))
        space_a=" "*size_a
        size_b=11-(len(str(int((i+1)*1.609)))+3)-3
        space_b=" "*size_b
        size_c=11-len(str(kilo1))
        space_c=" "*size_c
        print("{0}{2}{1:.3f}".format(i+1,(i+1)*1.609,space_a),
              space_b,
              "{0}{2}{1:.3f}".format(kilo1,(kilo1)*1.609,space_c))
        kilo1+=5

miles_to_kilo(1,10,20,65)


# In[ ]:




