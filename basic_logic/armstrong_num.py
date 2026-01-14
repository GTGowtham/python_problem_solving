num=int(input("enter the number:"))
num_str=str(num)
num_len=len(num_str)
total=0
for i in num_str:
    d=int(i)**num_len
    total=total+d
if num==total:
    print("Armstrong number")
else:
    print("not an armstrong")