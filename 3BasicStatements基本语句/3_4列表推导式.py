lst = []
for i in range(3,37,5):
    if i%2 == 0:    #执行操作条件
        lst.append(i*i)
print(lst)

#用列表推导式，简化程序
lst = [x*x for x in range(3,37,5) if x%2==0]    #进行运算，加入循环，执行条件
print(lst) 
lstU = [(x,y) for x in range(5) for y in range(2)]     #循环嵌套推导式
print(lstU)
d = dict(lstU)
print(d)