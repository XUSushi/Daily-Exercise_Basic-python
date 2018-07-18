# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 14:39:59 2018

@author: 许逸文
"""

"""
第二章 数据类型
第三章 数字
"""
import sys

#整型运算
a=3+3
print(a)

b=a-5 #可以直接把变量减去数字，运算
print(b)

c=4*8
print(c)

c=c/3
print(c)
#在Python 2.7中，整型的运算结果只能返回整型，除法的结果也不例外
#但是3可以

d=10**2 #**表示乘幂
print(d)

f=55%10
print(f) #用%取余数

g=type(f) #查看变量类型
print(g)

#在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
#浮点数
k=1.4
print(type(k)) #查看变量类型

ww=22.3/2.1
print(ww)

ee=ww+3
print(ee) #浮点数与整数进行运算时，返回的仍然是浮点数

q=5.1**2
print(q) #浮点数可以乘方
qq=q%2.1
print(qq) #浮点数可以取余

#复数 Complex Numbers
#Python 使用 j 来表示复数的虚部：
aa=1+2j
print(aa) 
print(aa.real)#查看实部
print(aa.imag)#查看虚部
print(aa.conjugate())#共轭

complex_s=11+4-(4*7/2)**3+23%4
print(complex_s)


#整数除法，返回的是比结果小的最大整数值：
chufa=45.3//7.88
print(chufa)
#也可以除负数
chu=34.4/-3
print(chu)
print("---------------------------")
#简单的数学函数
print(abs(-12.55)) #绝对值
print(round(29.44))#取整
print("---------------------------")
#取最大值
x={1,5,2,9}
xx=max(x)
print(xx)
#取最小值
yy=min(x)
print(yy)
print("---------------------------")
i = sys.maxsize

print(i) #int 的最大值 python3中没有maxint了，只有maxsize
print("---------------------------")
#类型转换
#浮点数转整型，只保留整数部分：
ii=33.444
iii=int(ii)
print(iii)
print("   ")
ff=float(1.2) 
f=1.2
print(ff)
print(f)

#原地计算
f+=3  #f=f+3
print(f)
f*=2 
print(f)
f-=2
print(f)
f-=2.3
print(f) #浮点数会有点误差

#布尔型
qq=True
print(type(qq))

www=4>9
print(www) #打印出的判断后的结果

#Python支持链式比较：
x = 22 
print(1 < x <= 13)
