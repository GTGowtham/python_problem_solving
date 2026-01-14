'''def reverseString(s):
        # code here
        str1=""
        for i in s:
            str1=i+str1
            
        print(str1)
s="gowtham"
reverseString(s)'''

def reverseString(s):
        reversed_s = ""
        for i in range(len(s)-1, -1, -1):
            reversed_s += s[i]
        print(reversed_s)
        
s="Gowtham"
reverseString(s)
    