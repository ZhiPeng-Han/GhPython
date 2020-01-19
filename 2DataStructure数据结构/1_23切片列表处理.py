# -*- coding: cp936 -*-
__author__ = "billpower"
__version__ = "2019.12.25"

import rhinoscriptsyntax as rs

lst = list(range(10))
print(lst)

lst[5] = 99

lstnone = lst + [None]*6    #需要建立更多数据的索引值时，通过增加none空值
print(lstnone)

lstnone[-6:-2] = list(range(100,106,2)) #分片赋值，可以同时替换多个项值

lstnone[:3] = []    #赋值列表为空，就是删除指定索引值
print(lstnone)

lstnone[1:1] = [0,0,-3,-4]  #指定起始与介素相同时，相当于插入新值
print(lstnone)

del lstnone[-2:]    #del删除指定值
print(lstnone)
