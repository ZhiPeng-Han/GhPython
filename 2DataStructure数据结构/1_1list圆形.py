#coding=utf-8
import rhinoscriptsyntax as rs

plane = rs.WorldXYPlane()   #建立XY工作平面
mplane = rs.MovePlane(plane,[6,6.5,0])  #移动平面
rectangle = rs.AddCircle(mplane,5)   #建立圆形
dpointsc = rs.DivideCurve(rectangle,20)     #等分矩形
dpoints = rs.AddPoints(dpointsc)      #增加等分点
for i in range(len(dpoints)):
    rs.AddText(str(i),dpoints[i],1)   #添加字
print(dpoints)

#sphere = rs.AddSphere(dpoints[3],1)
#cube = rs.AddBox(rs.BoundingBox(sphere))

sdpoints = dpoints[:]     #切片提取点
for i in range(len(sdpoints)):
    sphere = rs.AddSphere(sdpoints[i],0.5)
    cube = rs.AddBox(rs.BoundingBox(sphere))
    rs.DeleteObject(sphere)     #删除不再使用的球体
    xform =rs.XformTranslation([i,i*1.3,i*1.3]) #分步骤执行比gh同步更灵活
    trancube = rs.TransformObject(cube,xform)