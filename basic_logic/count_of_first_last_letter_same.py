def str_check(str1):
    str1=str1.lower()
    separators=[',','.','!','?',' ']
    words=[]
    temp=""
    count=0
    for ch in str1:
        if ch not in separators:
            temp+=ch
        else:
            if temp=="":
                pass
            else:
                words.append(temp)
                temp=""
    if temp!="":
        words.append(temp)

    for word in words:
        n=len(word)-1
        if(word[0]==word[n]):
            count+=1
    return count   
        

str1="Dad,,  civic where moM Monster"
print(str_check(str1))