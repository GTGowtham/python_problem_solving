def armstrong(n):
    temp=n
    s=0
    count=0
    while n>0:
        rem=n%10
        count+=1
        n//=10
    print(count)
    n=temp
    while n>0:
        rem=n%10
        cal=rem**count
        s+=cal
        n//=10

    if temp==s:
        return ("armstrong_number")
    else:
        return ("not armstrong")

print(armstrong(1634))