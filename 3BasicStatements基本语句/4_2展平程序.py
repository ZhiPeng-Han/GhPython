#语言只是交流的工具，表达的含义才是需要传达的内容，一般解决实际问题要进行多次条件判断

__author__ = "billpower"
__version__ = "2020.01.26"

import rhinoscriptsyntax as rs

#分解mesh，获取点坐标列表，用于生成面
meshes = meshes
#meshes = rs.ExplodeMeshes(mesh)  #该函数在新版本中无效
lp = []
#print(Locationpoint)
for i in Locationpoint: #循环遍历点，获取点坐标列表
    lp.append(rs.PointCoordinates(i))
#print(lp)

#核心展平程序
xymeshes = []
for i in range(len(meshes)):
    if i == 0:
        mesh0point = rs.MeshVertices(meshes[i]) #获取第一个单元面的所有顶点
        xymesh0 = rs.OrientObject(meshes[i],mesh0point,lp,1)    
        #将第一个单元面放置在二维平面上，初始参考点为第一个单元面的顶点，目标参考点为输入的点对象（至少三个点，并转化为点坐标列表
        xymeshes.append(xymesh0)    #将第一个展平面加入列表
        #print(xymeshes)
    else:
        vertices2 = rs.MeshVertices(meshes[i])  #获取索引值为i时，单元面所有顶点
        vertices1 = rs.MeshVertices(meshes[i-1])    #i-1时，单元面的所有顶点
        ver = [m for m in vertices1 for n in vertices2 if m==n] #遍历两mesh中的点，提取重合点ab
        #print(vertices2)
        a = ver[0]
        b = ver[1]
        indexa = vertices1.index(a) #提取ab点在i-1单元中的索引值
        indexb = vertices1.index(b)
        d = [m for m in vertices2 if m not in ver][0]
        #使用列表推导式循环遍历索引值为i时单元面的顶点，并且要求提取的条件为不重合的点，如果为四边，因此增加[0]
        refvertice = rs.MeshVertices(xymeshes[i-1]) #获取已经转化为二维单元面i-1的单元顶点
        indexc = [c for c in range(0,3) if c != indexa and c!=indexb]   #获取i-1单元顶点中ab以外c的索引值
        refverticespoint = rs.MirrorObject(rs.AddPoint(refvertice[indexc[0]]),refvertice[indexa],refvertice[indexb])#c'参考a'b',获取cm'点
        mirrorpoint = rs.PointCoordinates(refverticespoint) #获取cm'点坐标
        xymesh = rs.OrientObject(meshes[i],[a,b,d],[refvertice[indexa],refvertice[indexb],mirrorpoint],1)
        #将i单元面转化为二维面，初始参考点为待转化abd，目标为a',b',cm'
        xymeshes.append(xymesh)
    vertices2=[]
    vertices1=[]
    ver = []
print(xymeshes)






