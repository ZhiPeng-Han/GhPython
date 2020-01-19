#一次可以给多种数据，多个数据同时赋值
x,y,z = 3,7,21

values = 3,7,22

x,y,z = values
print(x,y,z)

d = {'x':3,'y':7}
key,value = d.popitem()
print(key,value)

#一次赋值给多个变量
x=y=9
print(x,y)

x = 6
x += 2
x *= 2