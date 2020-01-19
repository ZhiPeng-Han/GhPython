#用%s转化说明符
formatstr = "Hello,%s and %s!"  #通用%建立格式化字符串模式
values = ("Python","Grasshopper")   #常使用元组放置希望格式化的值
newstr = formatstr % values     #使用格式化值来格式化字符串模式
print(newstr)

formatstr = "Pi with three decimals:%.3f,and enter a value with percent sign:%.2f %%."
from math import pi
newstr = formatstr % (pi,3.14159)     #使用格式化值来格式化字符串
print(newstr)

formatstr = "%10f,%10.2f,%.2f,%.5s,%.*s,$%d,%x,%f"  #各类转换说明符实例
newstr = formatstr % (pi,pi,pi,"Hello Python!",5,"Hello Python",52,52,pi)
print(newstr)

formatstr = "%010.2f,%-10.2f,%+5d,%+5d"
newstr = formatstr % (pi,pi,10,-10)
print(newstr)

from string import Template
s = Template('$x,glorious $x!')     #定义模板字符串，$为格式化操作符
print(s.substitute(x="Python"))     #定义值，并使用sub方法格式化模板字符串

s = Template('$x and $y are both amazing!')
d = dict([('x','Python'),('y','Grasshopper')])
print(d)
print(s.substitute(d))