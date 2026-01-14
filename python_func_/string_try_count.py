s1="everything is possible"
s2="nothing is impossible so try again"
c='o'
co=0
s3=s1+s2
for ch in s3:
    if ch==c:
        co+=1
print(f" the character {c}, appears ,{co},times")