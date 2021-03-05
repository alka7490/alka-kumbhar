#!/usr/bin/env python
# coding: utf-8

# In[14]:


# 1. program to print pattern of haf diamond
  




rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
rows = 5


# In[ ]:


# 2. Write a Python program to reverse a word after accepting the input from the user.

def StringReverse(str1):
    str2 = str1[::-1]
    return str2

string = input("Please enter your own String : ")

string2 = StringReverse(string)
print("\nThe Original String = ", string)
print("The Reversed String = ", string2)



# In[ ]:





# In[ ]:




