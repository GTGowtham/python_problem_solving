def find_unique(ls):
    ls=sorted(ls)
    count=0
    for i in range(len(ls)-1):
        if ls[i]!=ls[i+1]:
            count+=1
    return count+1

ls=[1,5,2,1,2,3,4,5,7,6,6]
print(find_unique(ls))