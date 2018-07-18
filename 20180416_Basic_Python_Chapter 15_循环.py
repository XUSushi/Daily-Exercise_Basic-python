# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 19:10:41 2018

@author: 许逸文
"""

# In[27]:

#Chapter 15 循环


# In[28]:

#计算0-100的和

i = 0
num = 0
while i < 100:
    num += i
    i += 1
print (num)


# In[29]:

#空容器会被当成 False ，可以用 while 循环来读取容器中的所有元素：


# In[35]:

#While 循环
hero=set(['Superman','Batman','Iron man'])
while hero:
    #如果不为空，则做下面的内容，也就实现了遍历
    h=hero.pop()
    print("Today ",h," come here!")


# In[32]:

#循环每次从 hero 中弹出一个元素，一直到 hero为空为止。


# In[33]:

hero#可以看出已经空了


# In[36]:

#for 循环


# In[37]:

#用下面语句也可以遍历：


# In[38]:

hero=set(['Superman','Batman','Iron man'])
for h in hero:
    print("Welcome ",h)


# In[39]:

#注意使用 for 循环时，注意尽量不要改变 hero 的值，否则可能会产生意想不到的结果。


# In[40]:

#用for求和


# In[42]:

total = 0
for i in range(100):
    total += i
print (total)


# In[43]:

#在python 2中
#在循环前，它会生成一个长度为 100 的临时列表。
#生成列表的问题在于，会有一定的时间和内存消耗，当数字从 100变得更大时，时间和内存的消耗会更加明显。
#为了解决这个问题，我们可以使用 xrange 来代替 range 函数，其效果与range函数相同，但是 xrange 并不会一次性的产生所有的数据：


# In[44]:

total = 0
for i in xrange(100):
    total += i
print (total)


# In[45]:

#发现报错了，因为python 3中把xrange取消了


# In[46]:

#Continue语句


# In[47]:

#遇到 continue 的时候，程序会返回到循环的最开始重新执行。


# In[48]:

values = [7, 6, 4, 7, 19, 2, 1]
for i in values:
    if i % 2 == 0:
        # 忽略偶数
        continue
    print (i)


# In[49]:

#break语句
#遇到 break 的时候，程序会跳出循环，不管循环条件是不是满足：


# In[50]:

command_list = ['hello', 
                'hey', 
                'I',
                'am', 
                'stop', 
                'start', 
                'Chinese', 
                'stop']
while command_list:
    command = command_list.pop(0)
    if command == 'stop':
        break
    print(command)


# In[51]:

#可以看出在第一个“stop”的位置就停止了，不再打印下面的了


# In[52]:

#else语句


# In[53]:

#与 if 一样， while 和 for 循环后面也可以跟着 else 语句，不过要和break一起连用


# In[54]:

'''
当循环正常结束时，循环条件不满足， else 被执行；
当循环被 break 结束时，循环条件仍然满足， else 不执行。
'''


# In[55]:

#因为有break所以没有执行else
values = [7, 6, 4, 7, 19, 2, 1]
for x in values:
    if x <= 10:
        print ('Found:', x)
        break
else:
    print ('All values greater than 10')


# In[56]:

#当循环正常结束时，循环条件不满足， else 被执行；


# In[57]:

values = [11, 12, 13, 100]
for x in values:
    if x <= 10: #因为循环条件不满足，所以执行了else
        print ('Found:', x)
        break
else:
    print ('All values greater than 10')


# In[ ]:



