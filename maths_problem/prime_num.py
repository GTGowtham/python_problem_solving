start=int(input("enter the start number:"))
end=int(input("enter the end number:"))
for i in range(start,end+1):
    if(i==1):
        continue
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
    if(flag==0):
        print(i)
