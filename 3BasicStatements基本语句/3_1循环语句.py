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