num=int(input("enter the number:"))
count=0
digit=num
while digit!=0:
    div=digit%10
    digit=(int(digit/10))
    count+=1
print(count)

print("****************************************************************************************************************")
print("another method")
num=int(input("enter the number:"))
count=0
digit=num
while digit!=0:
    digit=digit//10
    count+=1
print(count)