n = int(input("Enter a number: "))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = (rev * 10) + digit   # ✅ same logic as Java
    n = n // 10               # floor division

if temp == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")