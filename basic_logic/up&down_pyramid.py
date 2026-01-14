
def pyramid(n):
    # Upper pyramid
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

    # Lower inverted pyramid
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "* " * (i + 1))

# Example usage
n = int(input("Enter number of rows: "))
pyramid(n)
