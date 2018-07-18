
# coding: utf-8

"""
Created on Mon Apr 16 18:40:21 2018

@author: 许逸文
"""

# In[1]:

#Chapter 14 判断语句


# In[2]:

x=0.6


# In[3]:

if x>0.1:
    print("yes!")
    print("x>0.1!")


# In[4]:

#如果 x > 0 为 False ，那么程序将不会执行两条 print 语句。
#python不用{}包起来，用缩进来控制，缩进严格


# In[7]:

a = 11
if a > 10:
    print("Ha!")
    print ("x >10")
    print ("This is still part of the block")
print ("This isn't part of the block, and will always print.")


# In[8]:

x = 2
if x > 10:
    print("Ha!")
    print ("x >10")
    print ("This is still part of the block")
print ("This isn't part of the block, and will always print.")


# In[9]:

#最后一句并不是if语句中的内容，所以不管条件满不满足，它都会被执行


# In[11]:

#elif 的个数没有限制，可以是1个或者多个，也可以没有。
#else 最多只有1个，也可以没有。

x = 300
if x > 100:
    print ("x >100!")
elif x == 100:
    print ("x is 100")
elif x<50:
    print ("x <50 !")
else:
    print("other") 


# In[12]:

#使用 and ， or , not 等关键词结合多个判断条件：


# In[13]:

x = 23
y = -9.7
x > 0 and y < 0


# In[14]:

x>0


# In[15]:

not x>0


# In[16]:

x<0 or x>-23 #or两者符合其一即可


# In[17]:

#判断一个年份是不是闰年


# In[18]:

year = 2018
if year % 400 == 0:
    print ("This is a leap year!")
# 两个条件都满足才执行
elif year % 4 == 0 and year % 100 != 0:
    print ("This is a leap year!")
else:
    print ("This is not a leap year.")


# In[19]:

#值的测试


# In[20]:

#可以直接在if中使用任何表达式作为条件


# In[22]:

'''
大部分表达式的值都会被当作True，但以下表达式值会被当作False：
False
None
0
空字符串，空列表，空字典，空集合
'''


# In[24]:

list1=[2,4,5]
if list1:#如果不为空就会打印项目个数
    print("There are ",len(list1)," elements.")
else:
    print("No element.")


# In[25]:

#看看如果是空列表会怎么样
list1=[]
if list1:
    print("There are ",len(list1)," elements.")
else:#为空则打印下一行
    print("No element.")


# In[26]:

#当然这种用法并不推荐，推荐使用 if len(mylist) > 0: 来判断一个列表是否为空。


