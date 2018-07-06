
# coding: utf-8

# In[57]:

#Chapter 8 元祖

tt  =  (1010, 1111, 1212, 1313, 1414)#元祖由（）生成


# In[5]:

tt


# In[6]:

tt[3]#索引元素


# In[8]:

tt[0:4]#切片


# In[10]:

tt[1]=2222#写后不能修改，这也是与列表的不同之处


# In[11]:

tt[5]=99#也不能再添加新元素了


# In[12]:

a=(333,)#单个元素的元素为了与表达式区别，加，


# In[13]:

a


# In[14]:

a[0]


# In[15]:

type(a)


# In[16]:

aa=(333)#这是表达式


# In[17]:

aa#注意直接打印aa时，表达式显示的是直接的数字；而元祖是（333,）


# In[18]:

type(aa)


# In[19]:

tuple(aa)#强制类型转化，不成功，不能把表达式转化为元祖


# In[20]:

kk=[2,3,4,5]


# In[21]:

kk


# In[22]:

tuple(kk)


# In[23]:

type(kk)#注意上一个语句只是让他那一句的输出是元祖，根本上没有改变kk的类型


# In[24]:

k=tuple(kk)


# In[25]:

k


# In[26]:

type(k)#这里因为把强制转化kk赋给了k，所以k就是元祖


# In[27]:

k.count


# In[28]:

k.count(2)#元组是不可变的，所以只能有一些不可变的方法，count是计算这个元素有几个


# In[29]:

kkk=(2,3,4,5,5,3,2,3,3)#元祖里可以有重复的元素


# In[30]:

kkk


# In[31]:

kkk.count(3)#计算3有几个


# In[32]:

kkk.index(3)#index是索引，找元素的位置，但如果有多个相同元素，则返回第一次出现的位置


# In[33]:

tup1 = ('physics', 'chemistry', 1997, 2000)#可以字符串和数字混着


# In[34]:

tup1


# In[36]:

tup1[1]


# In[37]:

newt=tup1+k#可以把多个元祖加在一起创建新元祖


# In[38]:

print(newt)


# In[39]:

#因为元祖元素写完就不可变了，所以元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组


# In[40]:

del k


# In[41]:

k#因为已经删除成功所以没有了


# In[42]:

len(newt)#计算元素个数


# In[43]:

(newt)*2#复制


# In[44]:

#任意无符号的对象，以逗号隔开，默认为元组


# In[46]:

tup1


# In[47]:

tt


# In[48]:

cmp(tup1,tt)


# In[50]:

t=(33,44,11)


# In[52]:

cmp(t,tt)#Python 3.X 的版本中已经没有 cmp 函数，如果你需要实现比较功能，需要引入 operator 模块，适合任何对象


# In[53]:

import operator


# In[54]:

operator.le(tt,t)#比较tt和t两元祖的长度是否一致


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


# In[ ]:



