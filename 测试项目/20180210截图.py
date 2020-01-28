import System as s
import Rhino as r
import time

size = s.Drawing.Size(1920,1080)
via = r.RhinoDoc.ActiveDoc.Views.ActiveView
bm = via.CaptureToBitmap(size)

now = time.strftime('%Y%m%d-%H.%M.%S',time.localtime(time.time()))
num = str(now)

print(num)
path = "D:\\users\\po\\" + num + ".png"
if x == True:
    bm.Save(path)


###############

now = time.strftime('%Y-%m-%d',time.localtime(time.time()))
num = str(now)
print(now)