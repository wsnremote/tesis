import time


fecha = time.strftime("%d%m%y")
print fecha
for i in range(365) :
  fecha2 = time.strftime("%d%m%y"+i)
  print fecha2 
