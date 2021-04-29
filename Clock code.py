#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#program for a clock 
import os    
import time    
second = 0    
minute = 0   
hours = 0 
day_time=[]
while(True):
    day_time.append('%d:%d:%d'%(hours,minute,second))
    time.sleep(1)    
    second+=1    
    if(second == 60):    
        second = 0    
        minute+=1    
    if(minute == 60):    
        minute = 0    
        if(hours<24):
            hours+=1;
        else:
            hours=0;
    os.system('cls')

