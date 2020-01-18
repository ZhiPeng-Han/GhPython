x=int(input('please input a int:'))
if x<0: 
  retrun -1
low=0
high=x
ans=(low+high)/2.0
sign=ans
while ans**2 !=x:
  if ans**2>x:
    high=ans
  else:
    low=ans
  ans=(low+high)/2.0
  if (ans**2)-x<0.01 and (ans**2)-x>-0.01:
    break
print(ans)
