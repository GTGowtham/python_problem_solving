'''def reversearr(arr):
    n=len(arr)
    temp=[0]*n
    #print(temp)
    
    for i in range(n):
        temp[i]=arr[n-i-1]
        
    for i in range(n):
        arr[i]=temp[i]
        
        
    
    
    
    
    
    
arr=[2,89,87,67,54,90]
reversearr(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
-------------------------------------------------------------------------------------------------------------------------------'''
'''def revstr(s1):
    s2=""
    for i in s1:
        s2=i+s2
    print(s2)
        
    
s1=input()
revstr(s1)
--------------------------------------------------------------------------------------------------------------------------------'''
def revstr1(s1):
    s2=""
    for i in range(len(s1)-1,-1,-1):
        s2+=s1[i]
    print(s2)


s1=input()
revstr1(s1)
