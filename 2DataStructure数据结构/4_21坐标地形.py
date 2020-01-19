__author__ = "billpower"
__version__ = "2020.01.15"

import rhinoscriptsyntax as rs

point = LocationPoint
file = File
x = []
y = []
z = []
xyz = []
rexyz = []
repoint = []
orpoint = []
f = open(file,'r')  #使用open打开文件，r为只读模式
firstpoint = f.readline()   #使用方法读取行，读到第一个换行符
subdistance = rs.PointSubtract(rs.AddPoint(firstpoint),point)   #读取第一个行点坐标，建立点并与输入的定位点差，获取两点之间坐标的插值
for line in f.readlines():  #对文件内容进行迭代，读取所有行
    lst = line.split(',')
    x.append(float(lst[0]))
    y.append(float(lst[1]))
    z.append(float(lst[2]))
    xyz.append((float(lst[0]),float(lst[1]),float(lst[2])))     #字符串坐标浮点数化，形成坐标值列表
    orpoint.append(rs.AddPoint(float(lst[0]),float(lst[1]),float(lst[2])))  #根据原数据值建立点
    rexyz.append(((float(lst[0])-subdistance[0]),(float(lst[1])-subdistance[1]),(float(lst[2])-subdistance[2])))    #计算新坐标，形成列表
    repoint.append(rs.AddPoint((float(lst[0])-subdistance[0]),(float(lst[1])-subdistance[1]),(float(lst[2])-subdistance[2])))   #根据新坐标增加点
f.close()   #关闭文件