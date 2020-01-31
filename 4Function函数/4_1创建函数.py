def fib(s,count):   #定义函数，s为最近开始的数，count为项值
    fiblst = [0,1]
    fiblstcount = []
    #s为0或1时的情况，初始值本身不是相加出来
    if s==0 or s==1:
        fiblstcount[:]=fiblst
        if s==0:
            for i in range(count-2):
                fiblstcount.append(fiblstcount[-1]+fiblstcount[-2])
        else:
            for i in range(count-1):
                fiblstcount.append(fiblstcount[-1]+fiblstcount[-2])
            fiblstcount=fiblstcount[1:]            
    #s值大于1时，在斐波那契数列中寻找初始对应值
    else:
        while True:
            fiblst[:]=[fiblst[1],fiblst[0]+fiblst[1]]
            if fiblst[1]-s>=0:break
        fiblstcount[:]=fiblst
        if abs(fiblst[0]-s)>=abs(fiblst[1]-s):
            for i in range(count-1):
                fiblstcount.append(fiblstcount[-1]+fiblstcount[-2])
            fiblstcount.pop(0)
        else:
            for i in range(count-2):
                fiblstcount.append(fiblstcount[-1]+fiblstcount[-2])
    return fiblstcount
            
print(fib(0,6))

#在函数中s，count为形式参数，0，6为实际参数
#形参和实参是内部作用域和外部全局参数传递的接口
#局部作用域下定义的变量不会和外部同名变量相互影响