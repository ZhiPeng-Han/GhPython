import rhinoscriptsyntax as rs
color = color
value = value
selectvalue = value     #再次复制value值
boolean = switch

def classification(color,value,selectvalue):
    color = color   #颜色数据
    value = value   #分类后z坐标数据
    selectvalue = value #复制列表，且使列表同步
    
    symcolor = []
    symvalue = []
    sym = []
    
    #第一次循环比较改变原数据，保留相同数据的第一个值
    for m in value: #外部循环遍历z值
        for n in range(len(selectvalue)):   #内部循环遍历z值
            if selectvalue[n] == m:     #如果值相同则为空值
                selectvalue[n] = None
        sym.append(m)   ##########因为一此循环内部不会同步v和s两组数据，所以可以提取第一个值
    
    #第二次循环，匹配保留值和color值
    for i in range(len(sym)):
        if sym[i] != None:
            symvalue.append(sym[i])
            symcolor.append(color[i])
    return value,selectvalue,sym,symvalue,symcolor

if boolean == True:     #开关决定是否运算
    value,selectvalue,sym,symvalue,symcolor = classification(color,value,selectvalue)





