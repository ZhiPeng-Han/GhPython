__author__ = "billpower"
__version__ = "2020.01.05"

import rhinoscriptsyntax as rs
import Rhino
from Grasshopper import DataTree
from Grasshopper.Kernel.Data import GH_Path

data = TreeData
print(data)     #检查每个路径下的项值

DA = DataTree[Rhino.Geometry.GeometryBase]()    #定义空的树形数据
print(DA)

Glst = []   #建立空的列表，用于分别放置各个路径下的所有项值，每个路径下的项值被放置于一个列表中
for i in range(data.BranchCount):   #BranchCount路径数，通过循环树形数据下每一个路径下的所有项值
    branchlst = data.Branch(i)  #Branch（）路径下的项，逐一提取树形数据下每一个路径下的所有项值
    lst = []    #建立空列表，提取路径下的各个项值
    for k in range(len(branchlst)):     #在各路径下所有项值循环
        lst.append(branchlst[k])    #把项值加入列表
    Glst.append(lst)     #再总结数据
print(Glst)

branchname = 1
DBPath = GH_Path(branchname)    #将1转换为{1}
DB = DataTree[Rhino.Geometry.GeometryBase](Glst[0],DBPath) #（路径，{1}）提取树形数据
print(DB)

DC = DataTree[Rhino.Geometry.GeometryBase](DB)
print(DC)

OTreeData = Glst
