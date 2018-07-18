
# coding: utf-8
"""
Created on Wed Apr 4 18:50:31 2018

@author: 许逸文
"""

# In[97]:

#Chapter 10 字典
a={}#建立空字典


# In[2]:

type(a)


# In[3]:

b={1:'姓名',2:'性别'}
#初始化字典


# In[4]:

b


# In[5]:

#还可以用索引键值的方法向其中添加元素


# In[9]:

a["type"]="dict"


# In[10]:

a["author"]="Xu Yiwen"


# In[11]:

a


# In[12]:

#查看键值
b[1]


# In[13]:

a['one']#没有这个键


# In[14]:

a["type"]


# In[15]:

#字典内的值，是可以修改的，更新键值


# In[16]:

a["type"]='You define it.'


# In[18]:

a
#可以看出修改了
#也可以看出字典中的键的顺序不是按照插入键值的顺序，为字典中的键本身不一定是有序的。


# In[20]:

a[1]#Python中不能用支持用数字索引按顺序查看字典中的值


# In[21]:

#除非数字是键值，比如


# In[22]:

b[1]


# In[23]:

#这样就可以，因为1是键


# In[24]:

#键必须是不可变的类型，出于hash的目的，Python中要求这些键值对的键必须是不可变的


# In[25]:

#字典可以套字典


# In[26]:

d1 = {'m': 4, 'w': 20}
d2 = {'m': 7, 'w': 25}
d3 = {'m': 10, 'w': 80}
d4 = {'m': 3, 'w': 30}


# In[27]:

#把上面这四个字典作为值传入新的字典


# In[28]:

zhengfang={'type1':d1,'type2':d2,'type3':d3,'type4':d4,}


# In[29]:

zhengfang


# In[30]:

#索引时也要注意


# In[31]:

zhengfang['type1']['w']


# In[32]:

#这样就可以索引到了


# In[34]:

zhengfang['type1']


# In[35]:

#键（或者值）的数据类型可以不同：


# In[38]:

fruit={'apple':20,'pineapple':'not good',3:'go home'}


# In[39]:

fruit


# In[40]:

#可以通过 dict() 转化来生成字典：
did=dict([('i',1),('love',2),('you',3)])


# In[41]:

did


# In[42]:

#利用索引直接更新键值对：


# In[43]:

did['too']=4


# In[44]:

did


# In[45]:

did['you']=9


# In[46]:

did


# In[47]:

#浮点数一般不用于做键，但是python3似乎可以了
did[4.5]='haha'


# In[48]:

did


# In[50]:

did[2.2+6.37]='top'


# In[51]:

did


# In[52]:

#有时候，也可以使用元组作为键值


# In[61]:

connections = {}
connections[('New York', 'Seattle')] = 100
connections[('Beijing','Shanghai')]=6700


# In[54]:

connections


# In[62]:

connections[('Shanghai','Beijing')]=600


# In[56]:

connections


# In[57]:

#元组是有序的，因此 'Shanghai', 'Beijing'和 ('Beijing', 'Shanghai') 是两个不同的键：


# In[63]:

print(connections[('Shanghai', 'Beijing')])
print(connections[('Beijing', 'Shanghai')])


# In[64]:

#用索引可以找到一个键对应的值，但是当字典中没有这个键的时候，Python会报错，这时候可以使用字典的 get 方法来处理这种情况


# In[70]:

a={}
a[1]='jj'
a[2]='rrr'


# In[69]:

a[3]#索引不存在的键值会报错


# In[74]:

a.get(3,'new')
#指定默认值参数


# In[78]:

a.get('4')


# In[77]:

a


# In[79]:

#pop 方法可以用来弹出字典中某个键对应的值，同时也可以指定默认参数


# In[81]:

a.pop(1)
#删除并返回字典中键 key 对应的值，如果没有这个键，返回 default 指定的值（默认是 None ）。


# In[82]:

a


# In[84]:

a.pop(4,'not')


# In[86]:

a[4]='kkk'


# In[87]:

a


# In[88]:

#del 函数可以用来删除字典中特定的键值对


# In[89]:

del a[4]


# In[90]:

a


# In[91]:

#update方法更新字典，可以批量


# In[93]:

people={}
people["first"]="Katty"
people["second"]='Hello'


# In[94]:

people


# In[95]:

p={'first':'Cathy','middle':'K'}#用一个字典更新另一个字典
people.update(p)


# In[106]:

people#注意原来的second，还在


# In[99]:

#in查询字典中是否有该键


# In[100]:

'katty' in people


# In[101]:

'Cathy' in people#不能查询值是否在


# In[102]:

'first' in people


# In[103]:

#返回一个由所有键值对元组组成的列表


# In[104]:

people.keys()


# In[107]:

people.values()


# In[109]:


people.items()


# In[110]:

#keys() 返回的值跟 values() 返回的值是一一对应的。


