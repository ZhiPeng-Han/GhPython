import rhinoscriptsyntax as rs

point = LocationPoint
file = File
x = []
y = []
z = []
xyz = []
rexyz = []
repoint = []
orpoint = []
f = open(file,'r')  #使用open打开文件，r为只读模式
firstpoint = f.readline()   #使用方法读取行，读到第一个换行符
subdistance = rs.PointSubtract(rs.AddPoint(firstpoint),point)   #读取第一个行点坐标
for line in f.readlines():
    lst = line.split(',')
    x.append(float(lst[0]))
    y.append(float(lst[1]))
    z.append(float(lst[2]))
    xyz.append((float(lst[0]),float(lst[1]),float(lst[2])))
    orpoint.append(rs.AddPoint(float(lst[0]),float(lst[1]),float(lst[2])))
    rexyz.append(((float(lst[0])-subdistance[0]),(float(lst[1])-subdistance[1]),(float(lst[2])))
    repoint.append(rs.AddPoint((float(lst[0])-subdistance[0]),(float(lst[1])-subdistance[1]),(float(lst[2])))
f.close()
rs.function()