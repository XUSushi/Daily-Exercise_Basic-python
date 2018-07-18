
# coding: utf-8

"""
Created on Tue Apr 17 10:40:01 2018

@author: 许逸文
"""

# In[1]:

#Chapter 16 列表推导式


# In[2]:

#用循环来生成列表
va = [10, 21, 4, 7, 12]
squares = []
for x in va:
    squares.append(x**2)#乘平方
print (squares)


# In[3]:

#用列表推导式更简单

v = [10, 21, 4, 7, 12]
squares = [x**2 for x in v]#简洁、省空间
print (squares)


# In[4]:

#还可以在列表推导式中加入条件进行筛选
v = [10, 21, 4, 7, 12]
squares = [x**2 for x in v if x <= 10]
print (squares)


# In[5]:

#只留下了x<=10的，并乘方


# In[6]:

#使用推导式生成集合和字典


# In[8]:

square_set = {x**2 for x in v if x <= 10}
print(square_set)
square_dict = {x: x**2 for x in v if x <= 10}
print(square_dict)


# In[9]:

type(square_set)


# In[10]:

type(square_dict)


# In[11]:

#计算上面例子中生成的列表中所有元素的和


# In[12]:

sum1 = sum([x**2 for x in v if x <= 10])
print(sum1)
#Python会生成这个列表，然后在将它放到垃圾回收机制中（因为没有变量指向它），这毫无疑问是种浪费。


# In[13]:

#Python使用产生式表达式来解决这个问题：去掉[]结果还是一样，但这里并不会一次性的生成这个列表。


# In[14]:

sum1 = sum(x**2 for x in v if x <= 10)
print(sum1)


# In[15]:

#比较时间


# In[16]:

x = range(1000000)

get_ipython().magic('timeit total = sum([i**2 for i in x])')


# In[17]:

get_ipython().magic('timeit total = sum(i**2 for i in x)')


# In[18]:

#使用产生式表达式更快


# In[19]:




# In[ ]:



