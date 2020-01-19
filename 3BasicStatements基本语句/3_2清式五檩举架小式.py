#start举架高,step举架差值,count步架数,h步架值,ps檩条半径
start,step,count,h,ps = float(Start),float(Step),int(Count),float(X),float(PS)

#步架值列表
lst = []    #用于放置步架值
lst.insert(0,0)
lst.append(start)

for i in range(count-1):
    start += step
    lst.append(start)
print(lst)

#举高列表
ml = []
for n in lst:
    nm = n*h
    ml.append(nm)
mll = ml.pop()  #移除举高列表最后一个值
mllm = mll+(2*ps-0.032)
ml.append(mllm)
mlo = mllm/h   #计算包含平水高的举高的举架值
print(mllm)

Mu = []
M = []
for q in range(len(ml)):
    Mu.append(ml[q])
    M.append(sum(Mu))
print(M)

MH = lst
MH[0],MH[-1] = [st,mlo]

