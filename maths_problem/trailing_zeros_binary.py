def trailing_zero(n):
    binary=""
    count=0
    while n>0:
        rem=n%2
        binary=str(rem)+binary
        n//=2
    rev_binary=binary[::-1]
    for i in rev_binary:
        if i=='0':
            count+=1
        else:
            break
    return count



print(trailing_zero(10))