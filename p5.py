# 1
# n=int(input("enter the total number you want: "))
# sum=0
# for i in range (1,n+1):
#      n=int(input("enter the number: "))
#      sum=sum+n
# avg=sum/i
# print(avg)
# 2
# n=int(input("enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,i)

# for i in range(1, 6):
#     for j in range(1, 6):
#          if j <= 5 - i:
#              print(end=" ")
#          else:
#              print("*",end=" ")
#     print()
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")


# n=100
# sum=0
# for i in range(1,n+1):
#     numerator=2*(i-1)+1
#     denomenator=2*(i+1)-1
#     term=numerator/denomenator
#     sum=sum+term
# print(f"the sum of series: {sum}")
n = 1
while n < 10000:
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
        if n == sum:
            print(f"the number {n} is perfect")
    n = n + 1
