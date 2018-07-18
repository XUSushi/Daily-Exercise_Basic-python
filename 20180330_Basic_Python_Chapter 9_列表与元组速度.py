# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:49:18 2018

@author: 许逸文
"""

# In[58]:

#Chapter 9 09 列表与元组的速度比较


# In[62]:

from numpy.random import rand


# In[63]:

values = rand(10000,4)
lst = [list(row) for row in values]
tup = tuple(tuple(row) for row in values)


# In[64]:

get_ipython().magic('timeit for row in lst: list(row)#计算遍历列表的速度')


# In[65]:

get_ipython().magic('timeit for row in tup: tuple(row)#计算遍历元祖的速度')


# In[66]:

#可见在遍历上，元组和列表的速度表现差不多。


# In[68]:


get_ipython().magic('timeit [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]')
#计算生成列表的速度


# In[69]:

get_ipython().magic('timeit (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)')
#计生成元祖的速度


# In[70]:

#显然生成元祖要快


# In[71]:

get_ipython().magic('timeit for row in lst: a = row[0] + 1#计算索引list速度')


# In[72]:

get_ipython().magic('timeit for row in tup: a = row[0] + 1#计算索引tuple速度')


# In[73]:

#元祖快一点


