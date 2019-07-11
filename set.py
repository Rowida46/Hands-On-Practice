#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
dir(math)
# to print a list of all craps of what a module math contain


# In[3]:


import numpy as np
dir(np)


# In[4]:


math.__doc__
#to get a documentation of this module


# In[8]:


def nu(*x):
    for i in x:
        return i
x= [1,5,7,8,9]
nu(x)


# In[16]:


def calc(y , x , z):
    return y+z
calc1 = [3 , '+' , 5]
calc(*calc1)


# In[19]:


def calc(y , x , z):
    return y-z
calc2 = [3 , '+' , 5]
calc(calc2[0] , calc2[1] , calc2[2])


# In[21]:


#set
my_set ={1,3}
my_set.add(3)
my_set


# In[27]:


#set
my_set ={1,3}
my_set.add(2)
y = my_set
print(y)
my_set.update({4,5,6})
my_set


# In[28]:


#set
my_set ={1,3}
my_set.add(2)
my_set.update({4,5,6})
my_set.discard(4)
my_set


# In[29]:


#set
my_set ={1,3}
my_set.add(2)
my_set.update({4,5,6})
my_set.remove(4)
my_set


# In[30]:


#set
my_set ={1,3}
my_set.add(2)
my_set.update({4,5,6})
my_set.clear()
my_set


# In[31]:


#union of 2 set
a = {1,2,3,4,5} ; b = {4,5,6,7,8,9}
a | b


# In[32]:


a = {1,2,3,4,5} ; b = {4,5,6,7,8,9}
a.union(b)


# In[33]:


# intersecction of 2 sets
a = {1,2,3,4,5} ; b = {4,5,6,7,8,9}
a & b


# In[36]:


# intersecction of 2 sets
a = {1,2,3,4,5} ; b = {4,5,6,7,8,9}
a.intersection(b)


# In[37]:


#differance of 2 sets
a = {1,2,3,4,5} ; b = {4,5,6,7,8,9}
a-b


# In[38]:


a = {1,2,3,4,5} ; b = {4,5,6,7,8,9}
a ^ b

