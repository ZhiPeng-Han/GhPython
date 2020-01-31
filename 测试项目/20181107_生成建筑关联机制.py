RecLengthList = [5,6,3,6,7]
RecDistanceList = [4,6,3,5,6]
PolyLengthList = [20,25,50] #从起始位点开始的边界列表

i = 0
j = 0
alrLength = RecLengthList[0] + RecDistanceList[0]
PointList = [0]
next_Length = 0
for i in range(len(RecLengthList)-1):
    I = i + 1
    RemainLength = PolyLengthList[j] - alrLength
    if RemainLength > RecLengthList[I]:
        #PointList.append(RecLengthList[i-1] + RecDistanceList[i-1])
        next_Length = RecDistanceList[i]
        alrLength += RecLengthList[I] + RecDistanceList[I]
    else:
        star_distance = RemainLength + RecDistanceList[i]
        end_distance = 1#用夹角计算方法，计算出end_distance
        for j in range(len(PolyLengthList)-1):
            k = j + 1
            if end_distance + RecLengthList[I] < PolyLengthList[k]:
                #下一边可放下矩形
                #PointList.append(RecLengthList[i-1] + star_distance + end_distance)
                next_Length = star_distance + end_distance
                alrLength = 0
                alrLength = end_distance + RecLengthList[I] + RecDistanceList[I]
                break
            else:
                #下一边不可放下矩形
                next_Length = star_distance + end_distance
                next_Length += PolyLengthList[k]
                #pointlist.append(RecDistanceList[])
    PointList.append(RecLengthList[i] + next_Length)



i = 0
j = 0
alrLength = RecLengthList[0] + RecDistanceList[0]   #建立第一个矩形占用长度
PointList = [0]     #第一个矩形位点
next_Length = 0
for i in range(len(RecLengthList)-1):
    I = i + 1
    RemainLength = PolyLengthList[j] - alrLength    #下一建筑的可用长度
    #print(RemainLength)
    if RemainLength > RecLengthList[I]:
        #PointList.append(RecLengthList[i-1] + RecDistanceList[i-1])
        next_Length = RecDistanceList[i]        #前一建筑的distance
        alrLength += RecLengthList[I] + RecDistanceList[I]  #占用长度增加
    else:
        star_distance = RemainLength + RecDistanceList[i]   #转角前建筑到转交点距离
        d = RecDistanceList[i]
        end = star_distance
        ang = angle[j]
        d_1 = RecdepthList[i]
        d_2 = RecdepthList[I]
        l_1 = RecLengthList[i]
        l_2 = RecLengthList[I]
        end_length = Create_x2(d,end,ang,d_1,d_2,l_1,l_2)   #用夹角计算方法，计算出end_length
        #print(end_length)
        for z in range(len(PolyLengthList)-j):
            k = z + j + 1
            if end_length + RecLengthList[I] < PolyLengthList[k]:
                #下一边可放下矩形
                #PointList.append(RecLengthList[i-1] + star_distance + end_distance)
                next_Length = star_distance + end_length
                alrLength = 0
                alrLength = end_length + RecLengthList[I] + RecDistanceList[I]
                break
            else:
                #下一边不可放下矩形
                next_Length = star_distance + end_length
                next_Length += PolyLengthList[k]
                #pointlist.append(RecDistanceList[])
        j += 1
    PointList.append(RecLengthList[i] + next_Length)
print(PointList)