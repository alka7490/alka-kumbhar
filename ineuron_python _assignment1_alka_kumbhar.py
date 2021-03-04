#!/usr/bin/env python
# coding: utf-8

# #Assignment 1
# Example 1

# In[1]:


for i in range(2000, 3001):
        
          if i % 7 ==0 and i % 5 !=0:


                print(i,  end =',')
                
                
                i+=1


# In[16]:


#example 2

#To accept user first name and last name and reverese it with space

first=input("enter your first  name:")

last=input("enter your first  name:")



print(first[::-1] + " " +last[::-1])


# In[25]:


#Example  3

#To find value of sphere 

import numpy as np
#diameter d=12 is given
r=6

volume=4/3*np.pi*r*r*r


print(f'volume of sphere with diameter 12 cm is{volume}=',volume)




# In[ ]:





# In[ ]:




