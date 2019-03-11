#!/usr/bin/env python
# coding: utf-8

# In[2]:


def convert_ms(n):
    seconds=int(n/1000)
    if seconds<60:
        print("0:0:"+str(seconds))
        return
    elif seconds==60:
        print("0:1:0")
        return
    else:
        minutes=int(seconds%60)
        if (seconds/60)<60:
            print("0:"+str(int(seconds/60))+":"+str(minutes))
        elif (seconds/60)==60:
            print("1:0:"+str(minutes))
        else:
            hours=seconds/60
            print(str(int(hours/60))+":"+str(int(hours-(int(hours/60)*60)))+":"+str(minutes))
    

convert_ms(5500)


# In[ ]:




