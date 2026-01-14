num=int(input("enter the number:"))
digit=num
temp=0
while digit!=0:
    rem=digit%10
    digit=int(digit/10)
    temp=(temp*10)+rem
print(temp)
