import math
base=int(input("enter any number:"))
power=int(input("enter the exponent:"))
print(pow(base,power))

print("*********************************************************************************************************************************************")
base1=int(input("enter base number:"))
power1=int(input("enter the exponent:"))
cal=1
for i in range(power1):
    cal=cal*base1
print(cal)