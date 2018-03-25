# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:26:00 2018

@author: 许某某
"""

s="hello, python"
print(s)
p="uiuiui"
print(p*4)

o=len(s)
print(o)

q="H E L L O"
n=q.split() #不指定的话，以空格分隔
print(n)
w="Q!U!E!E!N"
m=w.split('!')
print(m)
b=w.join(p) #与分割相反，s.join(str_sequence)的作用是以s为连接符将字符串序列str_sequence中的元素连接起来，并返回连接后得到的新字符串：

print(b)

e="*"
print(e.join(p))

print(w.replace("!N","haha"))
print(w.lower())

print(p.upper())

'''
s.strip()返回一个将字符串两端的多余空格除去的新字符串。
s.lstrip()返回一个将字符串开头的多余空格除去的新字符串。
s.rstrip()返回一个将字符串结尾的多余空格除去的新字符串。
'''
i=" hu hu hu    "
print(i.strip())
print(i.lstrip())
print(i.rstrip())

#s的值依然不会变化

#Python 用一对三引号来生成多行字符串：
a = """Miracles sometimes occur, 
but one has to work terribly for them. 
(C. Weizmann)"""
print(a)

c = ("hello, world. "
    "hhhhhhhhhh "
    "ooooooooooooooo")
print(c)

d="hello, world. "\
    "hhhhhhhhhh "\
    "ooooooooooooooo"
print(d)
print(hex(255))
print(int('9999'))
print(int('11111111', 2)) #可以指定按照多少进制来进行转换，最后返回十进制表达的整数：
#可以用数字或名字指定传入参数的相对位置：
print('{2} {1} {0}'.format('都', '被', '替换'))
print('{color} {0} {x} {1}'.format(190, 'dddo', x = 1.5, color='blue'))

#索引和分片
#索引
print("-------------------------------")
print(s[8])
#Python还引入了负索引值的用法，即从后向前开始计数，例如，索引 -2 表示倒数第 2 个元素
print(s[-4])
print(s[-6:-3])
print(s[0:4])
print(s[3:-2])
#Python还引入了负索引值的用法，即从后向前开始计数，例如，索引 -2 表示倒数第 2 个元素
print("----------")
print(s[:8])
print(s[:-3])#从字符串第一个开始到倒数第三个字符
print(s[-8:]) #从第-8个字符开始到字符串最后一个
print(s[-2:])
print(s[3:])
#每隔两个取一个值
print(s[::3])
#当step的值为负时，省略lower意味着从结尾开始分片，省略upper意味着一直分片到开头。
print(s[::-1]) #相当于倒着打印
print(s[::-3])

#当给定的upper超出字符串的长度（注意：因为不包含upper，所以可以等于）时，Python并不会报错，不过只会计算到结尾。
print(s[:100])


