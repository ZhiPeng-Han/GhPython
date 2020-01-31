#调入基本的标准库（模块）
import rhinoscriptsyntax as rs
import math
import random

#定义建筑水平方向结构线的函数
def basiclines(basicpoint,lengthunit,angle,offsetvalue,topbplineheight,multiple1,multiple2,multiple3):
#
    #建立初始母线
    bpoint0 = (basicpoint[0],basicpoint[1],basicpoint[2])
    #初始定位点
    bpoits = [] #
    bpoits.append(bpoint0)
    bpoint1 = (bpoint0[0]+multiple1*lengthunit,bpoint0[1],bpoint0[2])
    #根据初始定位点坐标计算第一个折线点的坐标
    bpoints.append(bpoint1)

    hypotenuse = multiple2*lengthunit   #计算第二段折线长度基础值
    bpoint2 = (bpoint1[0],hypotenuse*math.sin(angle),bpoint1[1]+hypotenuse*math.cos(angle))
    #第二个折线点的坐标
    bpoints.append(bpoint2)
    bpoint3 = (bpoint2[0]+multiple3*lengthunit,bpoint2[1],bpoint2[2])
    #
    bpoints.append(bpoint3)
    bpline0 = rs.AddPolyline(bpoints)

    bplines = []    #z方向上确定每一层母线
    bplines.append(bpline0)
    for i in range(1,4):
        dividecurvelength = rs.CopyObject(bpline0,[0,0,5*i])
        bplines.append(dividecurvelength)
    
    offsetbplines = []  #每层母线offset
    for j in bplines:
        offsetbpline=rs.OffsetCurve(j,[0,0,0],offsetvalue)
        offsetbplines.append(offsetbpline)
    
    #屋脊结构线
    topbplinecenter = rs.OffsetCurve(bplines[-1],[0,0,0],offsetvalue/2) #用于屋脊水平方向折线的基础线
    topbpline = rs.CopyObject(topbplinecenter,[0,0,topbplineheight])    #根据新的坐标点复制屋脊水平方向折线的基础线
    rs.DeleteObject(topbplinecenter)
    return bplines,offsetbplines,topbpline  #各层结构母线，水平结构线，屋脊结构线

#定义建筑两侧截面结构线的函数
def basicpoints(bplines,lengthunit):
#
    basicplanepoints = []   #等分点
    for u in range(len(bplines)):
        basicplanepoint = rs.DivideCurveLength(bplines[u],lengthunit,True,True)
        basicplanepoints.append(basicplanepoint)
    
    planeunit = 1
    randomselectionp = []   #随机提取的点
    pupoints = []
    for o in range(len(basicplanepoints)-1):    #循环等分点母列表
        for p in range(len(basicplanepoints[0])):   #循环子列表
            basicplanepointscor = [basicplanepoints[o][p][0],basicplanepoints[o][p][1],basicplanepoints[o][p][2]]
            pupoints.append(basicplanepointscor)    #提取一条线的各个点坐标

            #每组9个点,已有一个原点
            pupoint1 = [basicplanepointscor[0]+planeunit,basicplanepointscor[1],basicplanepointscor[2]]
            pupoints.append(pupoint1)   #第1个点
            rs.Addpoint(pupoint1)

            pupoint2 = [basicplanepointscor[0]+planeunit,basicplanepointscor[1]+planeunit,basicplanepointscor[2]]
            pupoints.append(pupoint2)   #第2个点
            rs.Addpoint(pupoint2)            

            pupoint3 = [basicplanepointscor[0],basicplanepointscor[1]+planeunit,basicplanepointscor[2]]
            pupoints.append(pupoint3)   #第3个点
            rs.Addpoint(pupoint3) 

            pupoint4 = [basicplanepointscor[0]-planeunit,basicplanepointscor[1]+planeunit,basicplanepointscor[2]]
            pupoints.append(pupoint4)   #第4个点
            rs.Addpoint(pupoint4) 

            pupoint5 = [basicplanepointscor[0]-planeunit,basicplanepointscor[1],basicplanepointscor[2]]
            pupoints.append(pupoint5)   #第5个点
            rs.Addpoint(pupoint5)

            pupoint6 = [basicplanepointscor[0]-planeunit,basicplanepointscor[1]-planeunit,basicplanepointscor[2]]
            pupoints.append(pupoint6)   #第6个点
            rs.Addpoint(pupoint6)

            pupoint7 = [basicplanepointscor[0],basicplanepointscor[1]-planeunit,basicplanepointscor[2]]
            pupoints.append(pupoint7)   #第7个点
            rs.Addpoint(pupoint7)     

            pupoint8 = [basicplanepointscor[0]+planeunit,basicplanepointscor[1]-planeunit,basicplanepointscor[2]]
            pupoints.append(pupoint8)   #第8个点
            rs.Addpoint(pupoint8)

            randomselectionp.append(random.choice(pupoints))
            pupoints = []     
    pupoints0 = randomselectionp[:]              

