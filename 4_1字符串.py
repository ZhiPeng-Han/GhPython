#转换字符串为列表
lst = list("Hello Python!")
print(lst)

#拼接字符串
x = "Hello "
y = "Python!"
z = x+y
print(z)

#嵌入字符串
lst = list(range(0,9,2))
print(lst)

lststr = []
for i in lst:
    lststr.append(str(i))
print(lststr)
sep = "+"
lststrjoin = sep.join(lststr)
print(lststrjoin)

#切分字符串
stri = "Hello Python!"
length = len(stri)  #使用函数len()计算长度
print(length)

#统一为大写或者小写
z = "Hello Python!"
lowerstr = z.lower()    #使用字符串的方法返回小写字母
print(lowerstr)
upperstr = z.upper()    #使用字符串的方法返回大写字母
print(upperstr)

#提取字符串
z = "Hello Python!"
substr = z[6:]  #使用列表分片的方法，提取部分字符串
print(substr)

#移除首尾两侧空白字符
strs = "       Hello Python!"
strs = strs.strip()  #使用列表分片的方法，提取部分字符串
print(strs)

#替换字符串
strr = "Hello Python!"
strrr = strr.replace("Python","Grasshopper")
print(strrr)

#排序字符串
stri = "Hello Python!"
strlst = list(stri)     #将字符串转变为列表
strlst.sort()       #排序，但是先拍大写
print(strlst)

strilower = stri.lower()
strlstlower = list(strilower)
strlstlower.sort()  #再次排序
print(strlstlower)

#查找字符串
stri = "Hello Python!"
d = "Python!"
ds = stri.find(d)
print(ds)