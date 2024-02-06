# mylist=[]
# mylist.append('apple')
# mylist.extend("mango")
# print(mylist)
# mylist.remove('m')
# mylist.pop(2)
# print(mylist)
# print(len(mylist))
# print(mylist[1])
# mylist.sort()
# print(mylist)
# mylist.reverse()
# print(mylist)


# n=[]
# x=int(input("enter the range: "))
# count=0
# for i in range(1,x+1):
#      num=int(input("enter the number: "))
#      if(num>0):
#          n.append(num)
#          count=count+1
#      i=i+1
# print(f"the positive number in list are: {n}")


# n=[]
# x=int(input("enter the range: "))
# count=0
# for i in range(1,x+1):
#     num=int(input("enter the number: "))
#     if(num<0):
#         n.append(num)
#         count=count+1
#     i=i+1
# print(f"the negative number in list are: {n}")


# n=[]
# x=int(input("enter the range: "))
# count=0
# for i in range(1,x+1):
#     num=int(input("enter the number: "))
#     if(num==0):
#         n.append(num)
#         count=count+1
#     i=i+1
# print(f"the number of zeroes are : {count}")


# n=[]
# x=int(input("enter the range: "))
# count=0
# for i in range(1,x+1):
#     num=int(input("enter the number: "))
#     if(num%2!=0):
#         n.append(num)
#         count=count+1
#     i=i+1
# print(f"the number of odd number are: {count}")

# n=[]
# x=int(input("enter the range: "))
# count=0
# for i in range(1,x+1):
#     num=int(input("enter the number: "))
#     if(num%2==0):
#         n.append(num)
#         count=count+1
#     i=i+1
# print(f"the number of even number are: {count}")

# n=[]
# x=int(input("enter the range: "))
# sum=0
# for i in range(1,x+1):
#     num=int(input("enter the number: "))
#     n.append(num)
#     i=i+1
# for i in range(len(n)+1):
#     sum=sum+i
#     i=i+1
# avg=sum/len(n)
# print(avg)


# string='0xx912gg67'
# numbers=[]
# for i in range(len(string)):
#     if string[i]>='0' and string[i]<='9':
#        numbers.append(string[i])
# print(numbers)

mylist = [1, 2, 3, 4, 5, 6, 1, 2, 3, 7, 8]
count = 0
for i in range(len(mylist)):
    if ( i != mylist[i]):
        count = count + 1
    if(count!=0):
        mylist.remove(i)
    i=i+1
print(mylist)
