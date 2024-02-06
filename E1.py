date=input("enter a date in dd/mm/yyyy format: ")
dd=[]
mm=[]
yyyy=[]
count=0
for i in date:
    if count<2:
        while i!='/':
            dd.append(i)
            count=count+1
    if count==2:
        while i!='/':
            mm.append(i)
            count=count+1
    if count==4:
        while i!='/':
            yyyy.append(i)
            
res=str(dd)
print(res)           
#new_date=mm + '-' + dd + '-' + yyyy
#print(new_date)