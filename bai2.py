import math
a=int(input("nhap gia tri cua a"))
b=int(input("nhap gia tri cua b"))
c=int(input("nhap gia tri cua c"))
delta=b*b-4*a*c
if delta<0:
   print("phuong trinh vo nghiem")
elif delta==0:
   x=-b/2*a
   print("phuong trinh co nghiem kep: ",x)
else:
   x1=(-b+math.sqrt(delta))/(2*a)
   x2=(-b-math.sqrt(delta))/(2*a)
   print("phuong trinh co nghiem: ",x1)
   print("phuong trinh co nghiem: ",x2)      
   
