
# coding: utf-8
"""
Created on Sat Apr 21 12:22:11 2018

@author: 许逸文
"""


# In[1]:

#Chapter 18 模块和包


# In[2]:

#模块 Python会将所有 .py 结尾的文件认定为Python代码文件


# In[3]:

get_ipython().run_cell_magic('writefile', 'ex1.py', '\nPI = 3.1416\n\ndef sum(lst):\n    tot = lst[0]\n    for value in lst[1:]:\n        tot = tot + value\n    return tot\n    \nw = [0, 1, 2, 3]\nprint (sum(w), PI)')


# In[4]:

#在自己的本地可以找到了


# In[7]:

#执行这个文件

get_ipython().magic('run ex1.py')


# In[8]:

#这个脚本可以当作一个模块，可以使用import关键词加载并执行它
#要在ex1.py文件路径下
import ex1


# In[9]:

ex1


# In[10]:

#使用下面这个方式，‘文件名.内容’来查看或修改变量
print (ex1.PI)


# In[11]:

ex1.PI = 3.141592653


# In[12]:

ex1.PI#改变了


# In[13]:

#调用模块里面的函数
ex1.sum([2, 3, 4])


# In[14]:

#在python2中
#为了提高效率，Python只会载入模块一次，已经载入的模块再次载入时，Python并不会真正执行载入操作，哪怕模块的内容已经改变。


# In[15]:

#需要重新导入模块时，可以使用reload强制重新载入它


# In[17]:

#但是python 3 就不一样了，取消了reload.直接再次import就会重新加载了
import ex1


# In[19]:

ex1.PI#可以看见已经修改了


# In[20]:

#删除之前生成的文件


# In[23]:

import os
os.remove('ex1.py') #去文件目录下看已经没有了，但是还是可以像下面这样调用？很奇怪


# In[24]:

ex1.PI


# In[25]:

#__name__ 属性


# In[26]:

#想将一个 .py 文件既当作脚本，又能当作模块用，这个时候可以使用 __name__ 这个属性。

#只有当文件被当作脚本执行的时候， __name__的值才会是 '__main__'，所以我们可以：


# In[42]:

get_ipython().run_cell_magic('writefile', 'ex2.py', '\nPI = 3.1416\n\ndef sum(lst):\n    """ Sum the values in a list\n    """\n    tot = 0\n    for value in lst:\n        tot = tot + value+6\n    return tot\n\ndef add(x, y):\n    " Add two values."\n    a = x + y\n    return a\n\ndef test():\n    w = [0,1,2,3]\n    assert(sum(w) == 6)\n    print (\'Very Good! test passed.\')\n    \nif __name__ == \'__main__\':\n    test()')


# In[28]:

#运行


# In[43]:

get_ipython().magic('run ex2.py')


# In[32]:

#当作模块导入， test() 不会执行


# In[39]:

import ex2


# In[40]:

#使用其中的变量
ex2.PI


# In[44]:

#使用别名：
import ex2 as e2
e2.PI


# In[47]:

#其他导入方法
#可以从模块中导入变量：


# In[48]:

from ex2 import add, PI


# In[49]:

#直接使用


# In[50]:

add(3,4)


# In[51]:

#使用 * 导入所有变量


# In[53]:

from ex2 import *
add(22.3, 4.5)


# In[54]:

#但这种导入方法不是很提倡，因为如果你不确定导入的都有哪些，可能覆盖一些已有的函数。


# In[55]:

#删除文件


# In[56]:

import os
os.remove('ex2.py')


# In[ ]:



