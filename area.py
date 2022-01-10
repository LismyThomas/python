import math
a=float(input("enter a number:"))
b=float(input("enter a number:"))
c=float(input("enter a number:"))
s=(a+b+c)/2
x=(s*(s-a)*(s-b)*(s-c))
area=math.sqrt(x)
print("area of traingle is:",area)

