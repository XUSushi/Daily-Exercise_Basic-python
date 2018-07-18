
# coding: utf-8
"""
Created on Thu Apr 26 15:12:09 2018

@author: 许逸文
"""

# In[1]:

#Chapter 20_警告


# In[2]:

#出现了一些需要让用户知道的问题，但又不想停止程序，这时候我们可以使用警告


# In[3]:

#导入警告模块


# In[4]:

import warnings


# In[5]:

# warnings 中的 warn 函数：

#warn(msg, WarningType = UserWarning)


# In[17]:

def mo_warning(m):
    if not 1<= m <= 12:
        msg = "month (%d) is not between 1 and 12" % m
        warnings.warn(msg, RuntimeWarning)
mo_warning(13)


# In[8]:

#想要忽略特定类型的警告，可以使用 warnings 的 filterwarnings 函数
#filterwarnings(action, category)


# In[10]:

#将 action 设置为 'ignore' 便可以忽略特定类型的警


# In[13]:

def month_warning(m):
    if not 1<= m <= 12:
        msg = "month (%d) is not between 1 and 12" % m
        warnings.warn(msg, RuntimeWarning)
        warnings.filterwarnings(action = 'ignore', category = RuntimeWarning)
month_warning(45)


# In[ ]:



