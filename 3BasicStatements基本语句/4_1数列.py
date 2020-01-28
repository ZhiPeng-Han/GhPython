import math
start = int(Start)
end = int(End)
step = int(Step)
series = []

series.append(start)    #将初始值加入列表
#for i in range(int(math.floor((end-start)/step))):
while True:
    start += step
    if start>=end:break
    series.append(start)

print(series)

#已有列表lst，索引范围切片
if start >= end:
    end = start+1
a = lst[start:end:step]
