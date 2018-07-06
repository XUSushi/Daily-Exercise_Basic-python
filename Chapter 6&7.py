# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:22:58 2018

@author: 许某某
"""
import random

#列表
#元素可以是不同类型的
l = [1, 2.0, 'hello']
print(l)

empty_list = []
q=empty_list.append("hello")
ki=empty_list.append("333")
ki=empty_list.append(333)
print(empty_list)
#可以看到字符串的数字和数字型数字的区别

print(len(empty_list))
#加起来
c=l+empty_list
print(c)#列表中的元素可以重复多次



#随机
b=random.sample(c,random.randint(0,len(c)))
print(b) 
print(c*3)
