
# coding: utf-8
"""
Created on Tue Apr 17 11:42:21 2018

@author: 许逸文
"""


# In[1]:

#Chapter 17 函数


# In[2]:

#定义函数


# In[3]:

def sum(x, y):
    """Add two numbers"""
    a = x + y
    return a


# In[4]:

#调用函数


# In[6]:

sum(2,44)


# In[7]:

sum("si","we")


# In[8]:

#可以把字符串拼接在一起


# In[9]:

#如果传入的参数数目与实际不符合，也会报错
sum(1,2,3)


# In[10]:

sum(3)


# In[11]:

#传入参数，还可以使用关键词模式，显式地指定参数的值：


# In[16]:

sum(x="pan",y="da")#但要记得这个的关键词必须和定义函数时的参数名一致
#如果这里x改为其他的就不行了


# In[18]:

sum(o="pan",y="da")#报错了


# In[19]:

sum(x=2, y=3)


# In[20]:

#可以混合这两种模式
sum(44,y=32)


# In[22]:

sum(55,y="ya")#但不能不同类型，会报错，没法加在一起啊


# In[23]:

#设定参数默认值
#在函数定义的时候给参数设定默认值


# In[24]:

def my(x, a=3, b=4, c=0):
    return a*x**2 + b*x + c


# In[26]:

my(2)#在调用时，可以省略有默认值的参数


# In[27]:

#可以修改参数的默认值
my(2,3,c=3)#这里混合了两种传值方法，3时传给a的。


# In[28]:

#在使用混合语法时，要注意不能给同一个值赋值多次，否则会报错，


# In[30]:

my(3,3,a=2)#报错了，因为给a传了两次值


# In[31]:

#接收不定参数


# In[32]:

#*args 表示参数数目不定，可以看成一个元组，把第一个参数后面的参数当作元组中的元素
def add(x, *args):
    total = x
    for arg in args:
        total += arg
    return total


# In[33]:

add(1,4,5)


# In[34]:

add(55,6)


# In[35]:

#这样就实现了让函数接收不定数目的参数


# In[36]:

#但是该函数不能使用关键词传参，想达到这个目的，用下面的方法


# In[37]:

def add(x, **kwargs):
    total = x
    for arg, value in kwargs.items():
        print ("adding ", arg)
        total += value
    return total


# In[39]:

add(2,a=1,b=3,v=8)#这样既可以记录关键词还可以记录值


# In[40]:

#这里， **kwargs 表示参数数目不定，相当于一个字典，关键词和值对应于键值对。


# In[41]:

#可以接收任意数目的位置参数和键值对参数：


# In[42]:


def foo(*args, **kwargs):
    print (args, kwargs)

foo(2, 3, x='barrr', ww=10)


# In[43]:

#要按顺序传入参数，先传入位置参数 args ，在传入关键词参数 kwargs 


# In[44]:

#函数返回多个值


# In[45]:

from math import atan2

def to_polar(x, y):
    r = (x**2 + y**2) ** 0.5
    theta = atan2(y, x)
    return r, theta

r, theta = to_polar(3, 4)
print (r, theta)


# In[46]:

#这里Python将返回的两个值变成了元组


# In[47]:

'''
因为这个元组中有两个值，所以可以使用
r, theta = to_polar(3, 4)

给两个值赋值。
'''


# In[51]:

#列表也可以这样批量赋值
x,y,z=[3,5,6]


# In[50]:

print(x,y,z)


# In[52]:

#可以将参数用元组传入：


# In[54]:


def add(x, y):
    """Add two numbers"""
    a = x + y
    return a
    
you = (21, 23)
print(add(*you)) 


# In[55]:

#注意这里的*不能少


# In[56]:

#可以通过字典传入参数来执行函数


# In[58]:

def add(x, y):
    """Add two numbers"""
    a = x + y
    return a

q = {'x': 2, 'y': 3}
print (add(**q))


# In[59]:

#注意这里是**


# In[60]:

#通过 map 的方式利用函数来生成序列：


# In[73]:

def sqr(x): 
    return x ** 2

a = [2,3,4]
w=map(sqr,a)
print (w)
for e in w:
    print(e)


# In[66]:

'''
map(aFun, aSeq)

将函数 aFun 应用到序列 aSeq 上的每一个元素上，返回一个列表，不管这个序列原来是什么类型。
'''


# In[67]:

#根据函数参数的多少，map 可以接受多组序列，将其对应的元素作为参数传入函数


# In[68]:

def add(x, y): 
    return x + y

a = (2,3,4)
b = [10,5,3]
print (map(add,a,b))


# In[70]:

map(add,a)


# In[72]:

for i in map(add,a,b):
    print(i)


# In[ ]:



