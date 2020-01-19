__author__ = "billpower"
__version__ = "2019.12.25"

import rhinoscriptsyntax as rs

plane = rs.WorldXYPlane()   #获取xy以原点为中心的参考平面
rectangle = rs.AddRectangle(plane,40,40)

dpointsCoordinate = rs.DivideCurve(rectangle,10) #等分10矩形
dpoints = rs.AddPoints(dpointsCoordinate)   #增加等分点
print(dpoints)

format = "point_%s" #格式化字符串的模式
dpointe = []
i = 0
for i in  range(len(dpoints)):
    dpointe.append(format % str(i)) #格式化字符串并逐一追加到列表
print(dpointe)

dpointx = list(range(len(dpoints))) #建立等分点索引
print(dpointx)

#切片索引，建球
selepoints = dpoints[x:y]
spheres = []
print(selepoints)
for i in range(len(selepoints)):  #循环来处理多组数据
    sphere = rs.AddSphere(selepoints[i],3)  #提取[y](圆心，半径)
    cube = rs.AddBox(rs.BoundingBox(sphere))    #（物体，plane）
    spheres.append(cube)
#    id = rs.GetObject(sphere)
#    if id: rs.DeleteObject()

print(spheres)
