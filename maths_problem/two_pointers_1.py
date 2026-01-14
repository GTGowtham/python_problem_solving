def target_finder(ls,target):
    ls=sorted(ls)
    i=ls[0]
    j=len(ls)-1
    act=0
    while(i<j):
        act=ls[i]+ls[j]
        if act==target:
            return(i,j)
            break
        elif act<target:
            i+=1
        elif act>target:
            j-=1
    return -1
ls=[20,65,30,90,70,21]
target=50
find=target_finder(ls,target)
print(find)