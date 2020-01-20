lst = list(range(29,37,2))
print(lst)

for i in  lst:
    print(i)

for i in range(len(lst)):
    print(i)
    print(lst[i])

d = dict(a=2,b=3,c=6,d=0)
print(d)

for key in d:
    print(key,d[key])

for key,value in d.items():
    print(key,value)


print('****************************')
#while循环
x = 1
while x <= 100:
    print(x)
    x += 10
    if x > 60:break #终止循环

x = 1
while True: #直接开始循环，再确定停止条件
    print(x)
    x += 2
    if x>10:break
