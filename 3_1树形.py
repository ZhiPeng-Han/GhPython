#coding=utf-8
import rhinoscriptsyntax as rs

firstpoint = rs.GetPoint("Selet one point") #在rhinoceros中失区点
rangel = 4  #定义x方向上复制点的数量
multiplev = 12  #定义点间距的倍数
mpoints = []    #定义第一排x方向列表

#循环x方向上复制点数量的参数，形成第一排
for i in range(rangel):
    matrix1 = rs.XformTranslation((i*multiplev,0,0))    #建立x方向上的矩阵
    mpoint1 = rs.PointTransform(firstpoint,matrix1)     #根据变换矩阵移动点
    mpoints.append(mpoint1)     #将移动的点依次放置于事项定义的空列表
    rs.AddPoint(mpoint1)    #在rhino空间中增加每次移动的点

rangeh = 4  #定义Y方向上复制点的次数
dpoints = {}    #定义空的字典，放置所有移动的点，每一横排的点放置于一个单独的列表中，作为值
mpointh = []     #放置所有点的空列表
deletep = []    #放置每一次内部循环即横排点的空列表,用于字典

#循环Y方向上的复制点的次数
for i in range(rangeh): 
    matrixh = rs.XformTranslation((0,i*multiplev,0))    #建立Y方向上的变换矩阵
    for m in range(len(mpoints)):
        pointh = rs.PointTransform(mpoints[m],matrixh)  #按照变换矩阵逐个移动每一个点
        rs.AddPoint(pointh)     #在rhino空间中增加每次移动点
        mpointh.append(pointh)    #将点加入列表
        deletep.append(pointh)
    dpoints[i] = deletep    #加入字典
    deletep = []
print(dpoints)

#提取字典键的值
hifirst = dpoints.get(1)
print(len(hifirst))

#建立矩形
plane = rs.WorldXYPlane()   #定义参考平面，建立矩形
h = 5
w = 5
for i in range(len(mpointh)):
    mplane = rs.MovePlane(plane,mpointh[i])
    rectangle = rs.AddRectangle(mplane,w,h)

