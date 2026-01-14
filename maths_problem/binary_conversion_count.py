def bin_conversion(n):
    count=0
    while n>0:
        rem=n%2
        if(rem==1):
            count+=1
        n//=2
    print(count)
bin_conversion(76)