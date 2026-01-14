def trailing_zero(n):
    if n == 0:
        return 0

    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2

    return count


print(trailing_zero(5))
