import re
pat = 'Python!'
text = 'Hello Python!'
a = re.findall(pat,text)    #使用方法以列表形式返回两者匹配项
print(a)
pat = 'python'  #再次定义正则表达式
b = re.findall(pat,text)    #p在text中没有匹配项
print(b)

print('**************')
#字符匹配 - 模式语法
#.匹配任意一个字符
import re
pat = '.ython'
textA = 'Hello Python!'
c = re.findall(pat,textA)   #'.ython'的模式匹配'Python'
textB = 'Hello PGython!'
print(c)
d = re.findall(pat,textB)
textC = 'Hello Pthon!'
print(d)
e = re.findall(pat,textC)
print(e)

import re
pat = r'w?cadesign\.cn,w+\.cadesign\.cn'
text = 'cadesign.cn,www.cadesign.cn'
f = re.findall(pat,text)    #?匹配0或者一个w，所以能匹配，+能匹配1个以上w
print(f)
pat = r'w{2}\.cadesign\.cn' #使用patten{m,n}特殊字符建立正则表达式
g = re.findall(pat,text)    #w{2}匹配两个w
print(g)

pat  = '[Py]*thon!' #[Py]有或者没有，有任意一个，都可以匹配
textA = 'Hello Python!'
textB = 'Hello Pthon!'
textC = 'Hello ython!'
textD = 'Hello thon!'
print(re.findall(pat,textA))
print(re.findall(pat,textB))
print(re.findall(pat,textC))
print(re.findall(pat,textD))

#管道|符号，任意匹配一个或者两者都匹配
pat = 'python|grasshopper'
textA = 'python'
textB = 'grasshopper'
textC = 'python and grasshopper'
print(re.findall(pat,textA))
print(re.findall(pat,textB))
print(re.findall(pat,textC))

print('****************************')
#re模块的方法
import re
pat = '[a-z]'   #匹配a-z的所有小写字母
text = 'python PYTHON'  #建立字符串
print(re.findall(pat,text))

pat = '[a-z]+'  #匹配a-z的所有小写字母，尽可能多的匹配
print(re.findall(pat,text))

print(re.search(pat,text))  #在字符串中寻找
if re.search(pat,text):
    print('Found it!')
print(re.match('p','python'))   #在给定字符串的开头匹配正则表达式
if re.match('p','python'):
    print('Fount it')

text = 'Hello,,,,,,,,,Python'
pat = ','
print(re.split(pat,text))

pat = ',+'  #尽可能多的匹配项
print(re.split(pat,text))

text = 'Hello Python'   #建立字符串
pat = 'Python'
print(re.sub(pat,'Grasshopper',text))   #匹配替换

pat = re.compile('Python')
print(pat.findall(text))   #=re.findall(pat,findall)

print('******************************')
#匹配对象和组
m = re.match(r'www\.(.*)\..{3}','www.python.org')
print(m)
print(m.group(1))   #匹配部分
print(m.start(1))   #调给定组匹配项的开始匹配值
print(m.end(1))    #匹配结束值
print(m.span(1))   #匹配区间


#在于类似于ANSYS这类力学分析软件对接时，由于几何数据不一定可以识别，一般都有txt模式的坐标点对接
#寻找接口
