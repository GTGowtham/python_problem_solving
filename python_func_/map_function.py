roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

s = "III"  # example Roman numeral string

# Map each character in the string to its corresponding value in the roman dictionary
mapped_values = [roman[char] for char in s]

print(mapped_values)  # Output: [1, 1, 1]