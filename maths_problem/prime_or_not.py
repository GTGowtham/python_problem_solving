num=int(input("enter the number:"))
flag=0
if num<=1:
    print("this not a prime number")
else:
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
if flag==1:
    print("this is not a prime number")
else:
     print("this is a prime number")