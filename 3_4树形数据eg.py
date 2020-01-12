__author__ = "billpower"
__version__ = "2018.09.23"

import rhinoscriptsyntax as rs
import Rhino    #调入rhino模块
from Grasshopper import DataTree    #从gh模块中调入Dataree类
from Grasshopper.Kernel.Data import GH_Path

#提取路径
data = TreeData     #将输入的数据赋值给新定义的变量,输入随机点数据
orgdata = []    #建立一个空列表
layerTree = DataTree[Rhino.Geometry.Point3d]()  #建立空的树型数据
for i in range(data.BranchCount):
    branchpath = data.Path(i)   #提取路径值
    branchpath = branchpath[0]
    #print(branchpath)

#寻找相间隔的数据，反转
    if branchpath%2 == 0:   #直接提取树形数据的索引判断，将相间隔的数据反转
        branchlst = data.Branch(i)  #提取path下的项值
        blst = []   #将数据提取为列表，用列表方法编辑数据
        for k in range(len(branchlst)):
            blst.append(branchlst[k])
        blst.reverse()  #反转数据
        orgdata.append(blst)    #重组数据
#剩下的不变
    else:
        branchlst = data.Branch(i)
        blst = []
        for k in branchlst:
            blst.append(k)
        orgdata.append(blst)
#print(orgdata)

#循环遍历列表，建立可用树形数据
for i in range(len(orgdata)):
    path = GH_Path(i)
    v = orgdata[i]  #依次提取子列表赋值给新变量
    layerTree.AddRange(v,path)  #建立路径为path，项值为v的树型数据
print(layerTree)
OTreeData = orgdata
DataTree = layerTree    #输出可用数据