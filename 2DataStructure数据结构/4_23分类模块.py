__author__ = "billpower"
__version__ = "2020.01.15"

import rhinoscriptsyntax as rs

data = dataZ    #z输入带处理数据
cal = Classification    #区间值
da = []
#浮点数化
for j in data:
    da.append(float(j)) #将转化后的值追加到列表中
data = da
for i in cal:
    cal[cal.index(i)] = float(i)
#归纳为a值
for k in range(len(cal)-1):
    a = cal[k]  #获取区间a-b
    b = cal[k+1]
    for q in range(len(data)):
        if a<=data[q]<b:
            data[q] = a     #若z值如果位于a-b分类区间，则用a替换
#两端的数据总结成cal
for w in range(len(data)):
    if data[w]> = cal[-1]:
        data[w] = cal[-1]
    elif data[w] <= cal[0]:
        data[w] = cal[0]
clalist = data
