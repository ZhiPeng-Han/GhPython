#用python对gh的树形数据提取，重组，检查，复制

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

DC = DataTree[Rhino.Geometry.GeometryBase](DB)  #复制
print(DC)

OTreeData = Glst

#############################################################################
#接上文程序print(DC)后
#提取列表中列表的项值
addpoint = Glst[0][1]   #提取Glst列表索引值为0的子列表，继而提取列表索引值为1的项值
print(addpoint)     #检查
#追加项值，默认最后
DC.Add(addpoint)    #使用方法在最后一个路径上追加项（点）
print(DC)   #检查

DC.Add(addpoint,GH_Path(59))    #追加数据，建立新的路径
print(DC)

addpoints = Glst[3]     #提取Glst列表索引值为3的子列表
DC.AddRange(addpoints,GH_Path(9))   #使用此方法追加一个指定路径的列表
print(DC)


#提取与清除树形数据的方法
alldata = DC.AllData()  #将所有树形数据拍平，返回到一个列表下
print(alldata)

branchM = DC.Branch(2)  #提取索引值为2的路径分支
print(branchM)

branchMP = DC.Branch(GH_Path(59))   #指定路径的路径分支
print(branchMP)

DM = DataTree[Rhino.Geometry,GeometryBase](DC)  #复制树形数据
DM = Clear()    #此方法清除数据和结构
print(DM)

DM = DataTree[Rhino.Geometry,GeometryBase](DC)  #复制树形数据
DM = ClearData()    #清除数据保留结构
print(DM)


#增加路径分支、数据拍平和移植项值的方法
DC.EnsurePath(GH_Path(60))  #增加新的路径
print(DC)

DF = DataTree[Rhino.Geometry.GeometryBase](DC)  #复制
DF.Flatten()    #拍平
print(DF)

DF.Graft()  #上升，移植所有路径分支下的项值到各自单独的路径分支下
print(DF)

DF = DataTree[Rhino.Geometry.GeometryBase](DC)  #复制
DF.Graft(GH_Path(9))    #上升{9}下的数据
print(DF)

#其他方法
addpoints = Glst[2][3]
DF.Insert(addpoint,GH_Path(9,0),2)
print(DF)

returnv = DF.ItermExists(GH_Path(9,0),2)    #判断数据是否存在
print(returnv)

returnv = DF.PathExists(GH_Path(9,0),3)
print(returnv)

returnBE = DF.PathExists(GH_Path(9,0))
print(returnBE)

returnP = DF.Path(5)
print(returnP)

DF.RemovePath(GH_Path(9,3))     #移除指定的路径以及其下项值
print(DF)

DF.MergeTree(DC)    #合并两个树形数据
print(DC)

DF.RenumberPaths()  #将所有路径从0开始命名
print(DF)

SMP = TreeData      #将最初的数据复制

SMP.SimplifyPaths()     #简化路径分支，去除0
print(SMP)

#DataTree的基本属性
branchcount = DF.BranchCount    #统计所有路径分支的数量
print(branchcount)

datacount = DF.DataCount    #统计各个路径分支下的所有数据数量
print(datacount)

branches = DF.Branches      #将各个路径下的项值形成列表
print(branches)

pathslst = DF.Paths      #所有路径分支放置于一个列表下
print(pathslst)

dec = DF.TopologyDescription    #树形数据结构
pritn(dec)