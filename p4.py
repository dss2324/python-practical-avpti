year=int(input("enter the year: "))
if(year%400==0):
    print("the year is leap")
elif(year%100==0): 
    print("the year is not leap")
elif(year%4==0):
    print("the year is leap")
else:
    print("the year is not leap")
# #2
# time=int(input("enter the time you worked: "))
# wages=30000
# if(time==40):
#     print("their is no increment in wages")
# elif(time>40):
#     print("their is increment of 500")
#     wages=wages+500
#     print(f"new wages are {wages}")
# #3
# weight=int(input("enter the weight in kgs: "))
# height=float(input("enter the height in cm: "))
# bmi=weight/(height**2)
# if(bmi<19):
#     print("you are underweight!!")
# elif(bmi>19 and bmi<25):
#     print("you are healthy")
# elif(bmi>25):
#     print("you are overweight!!")

# #4
# marks=int(input("enter your marks"))
# if(marks>=90):
#     print("A")
# elif(marks>=80 and marks<=89):
#     print("B grade")
# elif(marks>=60 and marks<=79):
#     print("C grade")
# elif(marks>=50 and marks<=69):
#     print("D grade")
# else:
#     print("F")
