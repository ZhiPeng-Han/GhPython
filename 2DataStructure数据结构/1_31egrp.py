#coding=utf-8
import rhinoscriptsyntax as rs

#start建立基本结构线
basicpoint = rs.GetPoint("pick one point")  #1.拾取一个点
matrix  = rs.XformTranslation((80,0,0)) #建立用于移动的矩阵
mbpoint = rs.PointTransform(basicpoint,matrix)  #根据建立的矩阵移动点

basicline = rs.AddLine(basicpoint,mbpoint)  #2.建立一条直线

offsetdistance = 10
offsetlineA = rs.OffsetCurve(basicline,[0,0,0],offsetdistance,[0,0,1])  #3.偏移复制直线
offsetlineB = rs.OffsetCurve(basicline,[0,0,0],-offsetdistance,[0,0,1])

#调整结构线，使用提取点移动
extendvalue = 2    #中间直线延长的距离
extendline = rs.ExtendCurveLength(basicline,0,2,extendvalue)    #4.延长中间直线

startpoint = rs.CurveStartPoint(extendline)    #5.拾取两侧端点
endpoint = rs.CurveEndPoint(extendline)
midpoint = rs.CurveMidPoint(extendline)

heightA = 10
heightB = 18
matrixstartend = rs.XformTranslation((0,0,heightA))    #建立端点移动矩阵
matrixmid = rs.XformTranslation((0,0,heightB))      #建立中间点移动矩阵

mstartpoint = rs.PointTransform(startpoint,matrixstartend)  #根据矩阵移动开始点
mendpoint = rs.PointTransform(endpoint,matrixstartend)   #移动结束点
mmidpoint = rs.PointTransform(midpoint,matrixmid)   #移动中心点

#整理变量到列表
cpoints = []
cpoints.extend([mstartpoint,mmidpoint,mendpoint])   #追加移动后的点在一个列表中

centercurve = rs.AddCurve(cpoints)  #6.建立有弧度的曲线
#rs.DeleteObject(basicline)
#基本结构线已建立

#建立等分点与数据组织
divicount = 14 #建立等分点变量
Adivipoints = rs.DivideCurve(offsetlineA,divicount)
Bdivipoints = rs.DivideCurve(offsetlineB,divicount)
cendivipoints = rs.DivideCurve(centercurve,divicount)

#在rhino空间中建立点
rs.AddPoints(Adivipoints)
rs.AddPoints(Bdivipoints)
rs.AddPoints(cendivipoints)

#检查变量
#patternA = list(range(0,len(Adivipoints),2))
patternB = list(range(1,len(Adivipoints)+1,2))
#print(patternA)
print(patternB)

#建立列表
#lineAps = []
#lineBps = []
#lineCps = []

#循环语句，同时分别提取保留点
#for i in patternA:
#    lineAps.append(Adivipoints[i])
#    lineBps.append(Bdivipoints[i])
#    lineCps.append(cendivipoints[i-1])

#用分片方式提取项值，避免循环，增加可读性
la = Adivipoints[::2]
lb = Bdivipoints[::2]
lc = cendivipoints[1::2]

#修整列表使得结构合理完整
lc.insert(0,cendivipoints[0])
lc.append(cendivipoints[-1])

#复制第三条结构线保留等分点，错开插入中心线列表
lcc = lc[:]   
for i in range(len(patternB)):
    lc.insert(patternB[i],la[i])
    lcc.insert(patternB[i],lb[i])

pla = rs.AddPolyline(lc)
plb = rs.AddPolyline(lcc)