def butterfly(n):
    # Top Half
    for i in range(1, n ):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)
    
    # Bottom Half
    for i in range(n, 0, -1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)

butterfly(5)
