import math
#note that quadratic equation is ax^2 + bx + c = 0

a= int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))
c= int(input("Enter the value of c: "))

numerator= (b**2) - 4*a*c
numerator_as_float= float(numerator)

numerator1= math.sqrt(numerator_as_float)

y= -b + numerator1
z= -b - numerator1
x= y / (2*a)
x2= z / (2*a)

print(f"The solution for the equation is {x} and {x2}")
