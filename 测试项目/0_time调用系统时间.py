from datetime import date, time, datetime, timedelta
  
def work():  
  print (x)
  
  
def runTask(func, day=0, hour=0, min=0, second=0):    
  now = datetime.now()
  period = timedelta(days=day, hours=hour, minutes=min, seconds=second)   
  iter_now = datetime.now()  
  iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')   
  print ("start work: %s" % iter_now_time)  
  func()  
  print ("task done.")  
  iter_time = iter_now + period  
  strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')  
  print ("next_iter: %s" % strnext_time)   
  
# runTask(work, min=0.5)  
x = 0
for i in range(0,10,1):
  x = x+1
  runTask(work, day=0, hour=0, min=0,second=5)
