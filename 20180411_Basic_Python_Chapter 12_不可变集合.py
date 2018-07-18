
# coding: utf-8
"""
Created on Web Apr 11 19:02:09 2018

@author: 许逸文
"""


# In[1]:

#Chapter 12 不可变集合


# In[2]:

#对应于元组（tuple）与列表（list）的关系，对于集合（set），Python提供了一种叫做不可变集合（frozen set）的数据结构。


# In[4]:

#创建
s=frozenset([1,3,5,'dd',99,0])


# In[5]:

s


# In[6]:

#与集合不同的是，不可变集合一旦创建就不可以改变。
#不可变集合的一个主要应用是用来作为字典的键


# In[7]:


flight_distance = {}


# In[8]:

city_pair = frozenset(['Los Angeles', 'New York'])#用来作为字典的键


# In[9]:

flight_distance[city_pair] = 7999


# In[10]:

flight_distance[frozenset(['China', 'Los Angeles'])] = 9999


# In[11]:

flight_distance


# In[12]:

#由于集合不分顺序，所以不同顺序不会影响查阅结果：


# In[13]:

flight_distance[frozenset(['China', 'Los Angeles'])]


# In[15]:

flight_distance[frozenset([ 'Los Angeles','China'])]


