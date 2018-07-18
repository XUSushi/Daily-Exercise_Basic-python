
# coding: utf-8
"""
Created on Sat Apr 28 19:52:29 2018

@author: 许逸文
"""


# In[1]:

#Chapter 21_文件读写


# In[5]:

#写入测试文件：


# In[7]:

get_ipython().run_cell_magic('writefile', 'test.txt', 'this is a test file.\nhello world!\npython is good!\ntoday is a good day.')


# In[16]:

#使用 open 函数或者 file 函数来读文件，使用文件名的字符串作为输入参数：


# In[17]:

f = open('test.txt')


# In[18]:

f = file('test.txt')


# In[19]:

#python 3 中file()的取消了


# In[20]:

#可以使用 read 方法来读入文件中的所有内容：


# In[22]:

text = f.read()
print (text)


# In[23]:

#可以按照行读入内容，readlines 方法返回一个列表，每个元素代表文件中每一行的内容：


# In[26]:


f =  open('test.txt' )
lines = f.readlines()
print (lines)


# In[27]:

#一定不要忘记关文件！！！不然要出大事情的！


# In[28]:

f.close()


# In[29]:

#可以写个循环，读每行内容


# In[31]:

f = open('test.txt')
for line in f:
    print (line)
f.close()


# In[32]:

#删除刚才创建的文件：


# In[33]:

import os
os.remove('test.txt')


# In[34]:

#写文件


# In[35]:

#使用 open 函数的写入模式来写文件


# In[36]:

#使用 w 模式时，如果文件不存在会被创建


# In[37]:

f = open('myfile.txt', 'w')
f.write('hello world!')
f.close()


# In[38]:

#查看是否真的写入了
open('myfile.txt').read()


# In[39]:

f.close()


# In[40]:

#如果文件已经存在， w 模式会覆盖之前写的所有内容


# In[43]:

f = open('myfile.txt' , 'w')
f.write('覆盖 hello world!')
f.close()
print (open('myfile.txt').read())


# In[45]:

#追加模式 a 
#追加模式不会覆盖之前已经写入的内容，而是在之后继续写入：


# In[46]:

f = open('myfile.txt', 'a')
f.write('... and more')
f.close()
print (open('myfile.txt').read())


# In[47]:

#写入结束之后一定要将文件关闭，否则可能出现内容没有完全写入文件中的情况。


# In[48]:

#读写模式 w+


# In[50]:

f = open('myfile.txt', 'w+')
f.write('hello world!')
f.seek(6) 
# f.seek(6) 移动到文件的第6个字符处，然后 f.read() 读出剩下的内容。
print (f.read())
f.close()


# In[51]:

#w+具有可读可写权限，而w只有可写权限。


# In[52]:

#删去刚才的文件


# In[53]:

import os
os.remove('myfile.txt')


# In[54]:

#二进制文件
#二进制读写模式 b


# In[55]:

import os
f = open('binary.bin', 'wb')
f.write(os.urandom(16))
f.close()

f = open('binary.bin', 'rb')
print (repr(f.read()))

f.close()


# In[56]:

import os
os.remove('binary.bin')


# In[57]:

#删除文件


# In[58]:

#换行符
'''
不同操作系统的换行符可能不同：

\r
\n
\r\n
使用 U 选项，可以将这三个统一看成 \n 换行符。
'''


# In[59]:

#关闭文件可以保证内容已经被写入文件，而不关闭可能会出现意想不到的结果：


# In[61]:

f = open('newfile.txt','w')
f.write('hello world')
g = open('newfile.txt', 'r')
print (repr(g.read()))


# In[62]:

#在关闭前，这个内容没有写入磁盘，所以读不出来


# In[63]:

#使用循环写入的内容也并不完整：


# In[66]:

f = open('newfile.txt','w')
for i in range(1000):
    f.write('hello world: ' + str(i) + '\n')

g = open('newfile.txt', 'r')
print (g.read())
f.close()
g.close()


# In[67]:

#只打印到hello world: 917，因为没有在写完关闭，就不完整


# In[69]:

#修改版
f = open('newfile.txt','w')
for i in range(1000):
    f.write('你好哟: ' + str(i) + '\n')
f.close()
#及时关闭文件
g = open('newfile.txt', 'r')
print (g.read())

g.close()


# In[70]:

#这样及时关闭文件，就可以写全了


# In[71]:

#删除文件
import os
os.remove('newfile.txt')


# In[73]:

#在读写时考虑到异常处理


# In[78]:

f = open('new.txt','w')
for i in range(3000):
    x = 1.0 / (i - 1000)
    f.write('hello world: ' + str(i) + '\n')


# In[75]:

#看看存了多少


# In[79]:

g = open('new.txt', 'r')
print (g.read())
f.close()
g.close()


# In[85]:

#出现异常的时候，磁盘的写入并没有完成，为此我们可以使用 try/except/finally 块来关闭文件
#finally 确保关闭文件，所有的写入已经完成。
f = open('newfile.txt','w')
try:
    for i in range(3000):
        x = 1.0 / (i - 1000)
        f.write('hello world: ' + str(i) + '\n')
except Exception:
    print ("出错了呜呜呜！")
finally:
    f.close()


# In[87]:

#读文件看看
g = open('newfile.txt', 'r')
print (g.read())
g.close()


# In[88]:

#Python还提供了更安全的方法 with 方法


# In[89]:

#with 块的内容结束后，Python会自动调用它的close 方法，确保读写的安全：


# In[90]:

with open('newfile.txt','w') as f:
    for i in range(3000):
        x = 1.0 / (i - 1000)
        f.write('hello world: ' + str(i) + '\n')


# In[91]:

#与 try/exception/finally 效果相同，但更简单。


# In[93]:

g = open('newfile.txt', 'r')
print (g.read())
g.close()


# In[94]:

#写文件时候一定要记得关闭文件


# In[95]:

#把文件删掉
import os
os.remove('newfile.txt')


# In[ ]:



