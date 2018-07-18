# -*- coding: utf-8 -*-
"""
Created on Wed Apr 4 18:00:11 2018

@author: 许逸文
"""

# In[111]:

#Chapter 11:集合


# In[112]:

#集合 set 是一种无序的序列
a = set()
type(a)


# In[113]:

a=set([2,4,5])#使用一个列表来初始化一个集合


# In[114]:

a


# In[115]:

b=set([2,4,5,5])


# In[117]:

b#集合会自动去除重复元素


# In[118]:

#创建集合


# In[120]:

a={2,3,3332,4,2}


# In[121]:

a
#集合会自动去除重复元素


# In[124]:

#但是创建空集合的时候只能用set来创建，因为在Python中{}创建的是一个空的字典


# In[123]:

s={}
type(s)


# In[125]:

#合并两个集合，自动去重


# In[126]:

a={3,4,5,'1',2}
b={9,7,4,'2',1}


# In[127]:

a.union(b)#重复的4去掉了


# In[128]:

b.union(a)


# In[129]:

a|b


# In[130]:

#取两个集合的交集，返回两个集合都有的元素的集合


# In[131]:

a.intersection(b)


# In[132]:

b.intersection(a)


# In[133]:

a&b


# In[134]:

#求a 和 b 的差集，返回只在 a 不在 b 的元素组成的集合。


# In[135]:

a.difference(b)


# In[136]:

b.difference(a)


# In[137]:

a-b #等效于a.difference(b)


# In[138]:

b-a #等效于b.difference(a)


# In[139]:

# - b 与 b - a并不一样，a-b返回的是a不在b的元素的集合；b - a 返回的是返回 b 不在 a 的元素组成的集合


# In[140]:

#求对称差，a 和b 的对称差集，返回在 a 或在 b 中，但是不同时在 a 和 b 中的元素组成的集合。


# In[141]:

#也就是并集-交集/ 异或


# In[142]:

a.symmetric_difference(b)


# In[143]:

b.symmetric_difference(a)


# In[144]:

a^b


# In[145]:

a={1,2,3,4}
b={2,3}


# In[146]:

#要判断 b 是不是 a 的子集，可以用 b.issubset(a) 方法，或者更简单的用操作 b <= a ：


# In[147]:

b.issubset(a)


# In[148]:

b<=a


# In[149]:

#也可以用 a.issuperset(b) 或者 a >= b 来判断


# In[150]:

a.issubset(b)


# In[151]:

a>=b


# In[152]:

#方法只能用来测试子集，但是操作符可以用来判断真子集


# In[153]:

a<=a


# In[154]:

a<a#自己不是自己的真子集


# In[155]:

#add 方法向集合添加单个元素


# In[156]:

t={88,99}
t.add(33)


# In[157]:

t


# In[158]:

#如果添加的是已有元素，集合不改变
t.add(33)


# In[159]:

t


# In[160]:

#update 方法向集合添加多个元素


# In[162]:

t.update(3,2,4)
#这样是不行的,update里需要是元素列表


# In[163]:

t.update([3,2,4])


# In[164]:

t


# In[165]:

#remove 方法移除单个元素


# In[166]:

t.remove(3)


# In[167]:

t


# In[168]:

#不能移除一个不存在的元素


# In[169]:

t.remove(11)


# In[170]:

#pop方法弹出元素
#集合没有顺序，不能像列表一样按照位置弹出元素，所以pop 方法删除并返回集合中任意一个元素，如果集合中没有元素会报错。


# In[171]:

t


# In[172]:

t.pop()#返回的是哪个，则删掉了哪个


# In[173]:

t#上面一个返回的值已经删除了


# In[174]:

#如果集合中没有元素会报错。


# In[176]:

s=set()#空集
s.pop()


# In[177]:

#discard 方法
#作用与 remove 一样，但是当元素在集合中不存在的时候不会报错。


# In[178]:

t


# In[179]:

t.discard(2)


# In[180]:

t


# In[181]:

t.discard(1)#没有1这个元素，但不会报错


# In[182]:

t


# In[183]:

#difference_update方法,从a中去除所有属于b的元素


# In[184]:

s={55,88}


# In[185]:

t.difference_update(s)


# In[186]:

t#可以看出在s中有的88，没了


