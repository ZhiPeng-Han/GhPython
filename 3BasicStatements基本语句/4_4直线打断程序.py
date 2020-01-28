__author__ = "billpower"
__version__ = "2020.01.28"

import rhinoscriptsyntax as rs
li = Lines
lst = []    #直线首尾点和交点
pls = []    #根据交点构建的直线
plsp = []   #用于临时放置循环每一步的交点
pl = []     #用于临时放置循环每一步的交点和首尾点

#嵌套循环得出所有直线交点
for i in range(len(li)):
    for p in li:
        point = rs.LineLineIntersection(li[i],p)
        if point and rs.IsPointOnCurve(li[i],point[0]) and rs.IsPointOnCurve(p,point[0]):
        #有交点且同时在两直线上
            lst.append(point[0])
            plsp.append(point[0])
    #取首尾点
    sta = rs.CurveStartPoint(li[i])
    end = rs.CurveEndPoint(li[i])
    #加入临时点列表
    pl = [sta]+plsp+[end]   #单个数据加[]改为列表
    #排序点并且连为折线
    pls.append(rs.AddPolyline(rs.SortPointList(pl)))
    plsp = []
    pl = []

print(lst)
print(PLS)
IntersectionPoints = lst
PLS = pls
