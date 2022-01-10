import math
a=float(input("enter number a"))
b=float(input("enter number b"))
c=float(input("enter number c"))
x=(b*b)-(4*a*c)
x1=(-b+math.sqrt(x))/(2*a)
x2=(-b-math.sqrt(x))/(2*a)
print("the solution are:",x1,x2)

