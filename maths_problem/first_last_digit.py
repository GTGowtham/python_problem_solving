num=int(input("enter any number:"))
first=num
while first>9:
    first=first//10
print("the first digit number ",first)

last=num%10
print("the last digit number ",last)

print("***************************************************************************************************************************************")

print("another method for find first digit in number")
num=int(input("enter any number:"))
first=num
while first>9:
    div=first%10
    first=int(first/10)
print("the first number is ",first)