#并行迭代
listA = [0,1,2,3]
listB = ['pointA','pointB','pointC','pointD']
ziplst = zip(listA,listB)   #使用zip函数对列表AB进行 并行迭代
print(ziplst)

d = dict(ziplst)    #结果是包含元组对的列表，使用dict函数建立字典
print(d)


#解包元组对只能在python2中使用
A = []
B = []
for a,b in ziplst:  #解包元组对
    A.append(a) 
    B.append(b)
    print(b)
print(A)

#编号迭代
listC = ['pointA','pointB','pointC','pointD']
d = {}
for index,value in enumerate(listC):    #使用函数编号迭代
    d[index] = value
    print(index,value)
print(d)
