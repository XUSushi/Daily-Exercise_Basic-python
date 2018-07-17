
# coding: utf-8

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


# In[16]:

#Chapter 13 Python 赋值机制


# In[17]:

x=[33,4,5]


# In[18]:

y=x


# In[21]:

x[1]=99
x


# In[22]:

y#改变变量x的值，变量y的值也随着改变


# In[23]:

id(x)


# In[24]:

id(y)


# In[25]:

#两者id值一样，证明变量 y 与变量 x 指向了同一块内存空间


# In[26]:

#使用 is 来判断是不是指向同一个事物


# In[27]:

x is y


# In[28]:

z=[99,9]
y=z


# In[29]:

id(y)#可以看出现在 y 指向另一块内存，与x不一样了


# In[30]:


x is y


# In[31]:

y is z


# In[32]:

#Python会为每个出现的对象进行赋值，哪怕它们的值是一样的
#但为了提高内存利用效率，对于一些简单的对象，如一些数值较小的int对象，Python采用了重用对象内存的办法


# In[33]:

a=9
b=9


# In[34]:

id(a)


# In[35]:

id(b)


# In[36]:

a is b


# In[37]:

#不是那么简单的对象就不一样了
aa=9822.3
bb=9822.3


# In[38]:

id(aa)


# In[39]:

id(bb)


# In[40]:

#id不一样
aa is bb


# In[43]:

#容器类型
x = [88,500, 501, 502]
id(x[0])


# In[44]:

id(x[1])


# In[45]:

id(x[2])


# In[46]:

id(x[3])


# In[47]:

id(x)


# In[48]:

#赋值，id(y)=id(x)


# In[49]:

y=x


# In[50]:

id(y)


# In[51]:

x is y


# In[52]:

#修改 y[1] ，id(y) 并不改变。


# In[53]:

y[1]=99


# In[54]:

id(y)


# In[55]:

#id(x[1]) 和 id(y[1]) 的值改变了


# In[56]:

id(x[1])


# In[57]:

id(y[1])


# In[58]:

#更改 y 的值，id(y) 的值改变


# In[59]:

y=[12,34,56]


# In[60]:

y


# In[61]:

id(y)


# In[62]:

id(x)


# In[ ]:



