def lcm(a,b):
    res=max(a,b)
    while res<=a*b:
        if res%a==0 and res%b==0:
            break
        res+=1
    return res

print(lcm(12,15))