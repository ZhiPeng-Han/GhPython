# -*- coding: cp936 -*-
__author__ = "billpower"
__version__ = "2019.12.25"

import rhinoscriptsyntax as rs

plane = rs.WorldXYPlane()   #��ȡxy��ԭ��Ϊ���ĵĲο�ƽ��
rectangle = rs.AddRectangle(plane,40,40)

dpointsCoordinate = rs.DivideCurve(rectangle,10) #�ȷ�10����
dpoints = rs.AddPoints(dpointsCoordinate)   #���ӵȷֵ�
print(dpoints)

format = "point_%s" #��ʽ���ַ�����ģʽ
dpointe = []
i = 0
for i in  range(len(dpoints)):
    dpointe.append(format % str(i)) #��ʽ���ַ�������һ׷�ӵ��б�
print(dpointe)

dpointx = list(range(len(dpoints))) #�����ȷֵ�����
print(dpointx)

#��Ƭ����������
selepoints = dpoints[x:y]
cubes = []
print(selepoints)
for i in range(len(selepoints)):
    sphere = rs.AddSphere(selepoints[i],3)  #��ȡ[y](Բ�ģ��뾶)
    cube = rs.AddBox(rs.BoundingBox(sphere))    #�����壬plane��
#    id = rs.GetObject(sphere)
#    if id: rs.DeleteObject()
    xform = rs.XformTranslation([i,i*5,i*5])    #x������ƶ�����
    trancube = rs.TransformObject(cube,xform)   #�ƶ�����
    cubes.append(trancube)
print(cubes)
