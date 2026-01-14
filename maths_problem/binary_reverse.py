def binary_reverse(n):
    str_binary=""
    while n>0:
        rem=n%2
        str_binary=str(rem)+str_binary
        n//=2
    rev=str_binary[::-1]
    return int(rev,2)

print(binary_reverse(76))

# explaination
#
# bit = 10 % 2 = 0
# reversed_num = 0*2 + 0 = 0
# n = 5
#
# bit = 5 % 2 = 1
# reversed_num = 0*2 + 1 = 1
# n = 2
#
# bit = 2 % 2 = 0
# reversed_num = 1*2 + 0 = 2
# n = 1
#
# bit = 1 % 2 = 1
# reversed_num = 2*2 + 1 = 5
# n = 0