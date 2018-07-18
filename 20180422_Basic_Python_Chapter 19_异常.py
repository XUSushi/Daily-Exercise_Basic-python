
# coding: utf-8
"""
Created on Sun Apr 22 13:02:18 2018

@author: 许逸文
"""



# In[1]:

#Chapter 19_异常


# In[2]:

#try & except 块


# In[3]:

#下面这个代码，如果输入0或者负数时会出错，因为log10(x)的x不能是负数或0


# In[8]:

import math
import os
while True:
    text = input('> ')
    if text[0] == 'q':
        break
    x = float(text)
    y = math.log10(x)
    print ("log10({0}) = {1}".format(x, y))


# In[9]:

#报错 ValueError: math domain error


# In[10]:

#一旦报错，程序就会停止执行，如果不希望程序停止执行，那么我们可以添加一对 try & except：


# In[14]:

import math

while True:
    try:
        text = input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = math.log10(x)
        print ("log10({0}) = {1}".format(x, y))
    except ValueError:
        print ("the value must be greater than 0")


# In[16]:

#这个时候输入<=0的就会打印except里的内容，程序可以继续执行


# In[17]:

#捕捉不同的异常


# In[18]:

#一个程序可能有好多不同的异常


# In[1]:

#1.捕捉所有异常
#将except 的值改成 Exception 类，来捕获所有的异常。


# In[2]:

import math

while True:
    try:
        text = input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print( "1 / log10({0}) = {1}".format(x, y))
    except Exception:
        print ("invalid value")


# In[3]:

#2. 指定特定值
#我们把 ZeroDivisionError 加入 except 。


# In[8]:

import math

while True:
    try:
        text = input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print( "1 / log10({0}) = {1}".format(x, y))
    except (ValueError, ZeroDivisionError):
        print ("invalid value")


# In[5]:

#3. 另加处理


# In[7]:

import math

while True:
    try:
        text = input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print( "1 / log10({0}) = {1}".format(x, y))
    except ValueError:
        print ("the value must be greater than 0")
    except ZeroDivisionError:
        print ("the value must not be 1")


# In[9]:

#将这两种方式结合起来,用 Exception 来捕捉其他的错误：


# In[15]:


import  math

while True:
        
    try:
        text = input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print ("1 / log10({0}) = {1}".format(x, y))
    except ValueError:
        print ("the value must be greater than 0")
    except ZeroDivisionError:
        print ("the value must not be 1")
    except Exception:
        print ("unexpected error")#这样所有的问题都可以处理到了


# In[16]:

#为了得到异常的具体信息，我们将这个 ValueError 具现化：


# In[1]:

#注意python3 与教材有区别，python 3 与python2在一块有变化，没有message这个属性了
import math

while True:
    try:
        text = input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print ("1 / log10({0}) = {1}".format(x, y))
    except ValueError as exc:
        if str(exc) == "math domain error":
            #python 3 与python2在一块有变化，没有message这个属性了
            print ("the value must be greater than 0")
        else:
            print ("could not convert '%s' to float" % text)
    except ZeroDivisionError:
        print ("the value must not be 1")
    except Exception as exc:
        print ("unexpected error:", exc.message)


# In[24]:

#python2 中exc.message 显示的内容是异常对应的说明
#python 3中直接用str(exc)显示


# In[25]:

#自定义异常


# In[26]:

#异常是标准库中的类，这意味着我们可以自定义异常类


# In[3]:

class CommandError(ValueError):
    pass


# In[28]:

#这里我们定义了一个继承自 ValueError 的异常类，异常类一般接收一个字符串作为输入，并把这个字符串当作异常信息


# In[32]:


valid_commands  = {'start', 'stop', 'pause'}

while True:
    command = input('> ')
    if command.lower() not in valid_commands:
        raise CommandError('Invalid commmand: %s' % command)
        #raise用于抛出异常


# In[ ]:

#我们可以使用 try/except 块来捕捉这个异常


# In[5]:

#这里我自己添加了退出机制，q
valid_commands = {'start', 'stop', 'pause'}

while True:
    command = input('> ')
    if command[0]=='q':
        break
    try:
        
        if command.lower() not in valid_commands:
            raise CommandError('Invalid commmand: %s' % command)
    except CommandError:
        print ('Bad command string: "%s"' % command)


# In[6]:

#关键词 finally。

#不管 try 块有没有异常， finally 块的内容总是会被执行，而且会在抛出异常前执行，因此可以用来作为安全保证，比如确保打开的文件被关闭。


# In[7]:

try:
    print ('try it')
finally:
    print ('finally was called.')


# In[8]:

#在抛出异常前执行
try:
    print (1 / 0)
finally:
    print ('finally was called.')
    


# In[9]:

#再升级一下，看捕获异常的话，执行的先后顺序
try:
    print (1 / 0)
except ZeroDivisionError:
    print ('divide by 0.')
finally:
    print ('finally was called.')


# In[10]:

#如果异常被捕获了，在最后执行


# In[ ]:



