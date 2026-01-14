def fact(x):
    if(x==1):
        return 1
    else:
        return (x*fact(x-1))
n=int(input("enter any number:"))
print("the factorial number is ",fact(n))