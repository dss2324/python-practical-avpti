#first program
# #c=int(input("enter temperature in celcius "))
# f=((9/5)*c)+32
# print(f"the temperature in fahrenheit is {f}")

#second program
# x1=int(input("enter first x coordinates"))
# # y1=int(input("enter first y coordinates"))
# x2=int(input("enter second x coordinates"))
# y2=int(input("enter second y coordinates"))

# slpoe=(y2-y1)/(x2-x1)
# print(f"the value of slope is {slpoe}")

#third program
# p=int(input("enter principle amount"))
# t=int(input("enter number of year"))
# r=int(input("enter rate of interest"))
# n=int(input("enter number of times interest is applied per time period"))
# SI=(p*r*t)/100
# print(f"SI= {SI}")
# CI=p*pow((1+(r/(100*n))),n*t)
# print(f"CI= {CI}")

#fourth program
# q=int(input("enter the value in quarter: "))
# d=int(input("enter the value in dimes: "))
# n=int(input("enter the value in nickles: "))
# p=int(input("enter the value in pennies: "))
# dollar=(q*0.25)+(d*0.10)+(n*0.05)+(p*0.01)
# print(f"you have to pay ${dollar}")

#fifth program
# a,b,c=1,2,3
# max= a if(a>b and a>c) else b if(b>a and b>c) else c
# print(f"the maximum number is {max}")
# r=int(input("enter the radius"))
# pi=3.14
# area=4*pi*pow(r,2)
# print(f"area of sphere = {area}")
# volume=(4/3)*pi*pow(r,3)
# print(f"volume of sphere = {volume}")
import math
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# c=int(input("enter c: "))
# delta=pow(b,2)-(4*a*c)
# math.sqrt(delta)
# root1=((-b+delta)/(2*a))
# root2=((-b-delta)/(2*a))
# print(f"value of root1={root1}")
# print(f"value of root2={root2}")
pi=3.14
wh=int(input("enter the height of wall: "))
angle=int(input("enter the angle: "))
rad=(pi/180)*angle
len=wh/math.sin(rad)
print(len)