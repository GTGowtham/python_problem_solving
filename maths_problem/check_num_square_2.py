def check_square_2(n):
    count=0
    if n==0:
        return False
    while n>0:
        rem=n%2
        if(rem==1):
            count+=1
        n//=2
    if(count==1):
        return True
    else:
        return False

print(check_square_2(1))