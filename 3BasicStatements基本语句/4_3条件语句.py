'''
x == y
x<y
x>y
x<=y
x>=y
x!=y

x is y  #x和y为同一对象
x is not y  #为不同对象

x in y  #x是y容器（比如列表）的成员
x not in y  #x不是y容器的成员
'''

#######################
x = y = [3,6,9] #链式赋值，xy为同一对象，即一个发生改变时另一个页发生变化
z = [3,6,9]
print(x==y)
print(x is y)
print(x==z)
print(x is z)
print(x is not y)

print(3 in x)

del x[2]
print(x,y)


