def gcd(a,b):
    temp=1
    for i in range(1,min(a, b) + 1):
        if a%i==0 and b%i==0:
            temp=i
    return temp

print(gcd(64,26))