f = open('D:\data.txt','r')  #使用open打开文件，r为只读模式，w写模式，a追加写入模式，b二进制模式，+读写模式
fa=f.read(10)  #
fb=f.readline()
fc=f.readline(10)
fd=f.readlines()
#print(fc)
f.close()

f = open('D:\data.txt','w') #写模式
f.write('Hello Python!')
lst = ['Hello Python!\n','Hello Grasshopper!\n','They are both amazing!']   #定义列表
f.writelines(lst)   #把列表写入文件
f.close()

#迭代读取文件
f = open('D:\data.txt','r') #读模式
lst = []
while True:
    line = f.readline() #逐一读取行
    str = "#"+line  #调整字符串
    lst.append(str) #将调整后的字符串追加到列表中
    if not line:break   #读取完则停止循环
f.close()
#print(lst)

随意移动到读取位置
f = open('D:\data22.txt','w+') #写模式
f.write('Hello Python!')
f.seek(6)
f.write('Grasshopper!')
f.close()

F=open('D:\data22.txt','r') #读模式
fr=F.read(15)
F.close()
print(fr)


