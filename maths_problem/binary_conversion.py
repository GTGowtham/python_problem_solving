def binary_conversion(n):
    temp=0
    binary_str=""
    while(n>0):
        rem=n%2
        binary_str = str(rem) + binary_str
        n//=2
    print(binary_str)

binary_conversion(72)