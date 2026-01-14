def find_common_characters(msg1, msg2):
    # Remove pass and write your logic here
    msg1 = msg1.replace(" ", "")
    msg2 = msg2.replace(" ", "")
    for i in range(len(msg1)):
        return i

# Provide different values for msg1,msg2 and test your program
msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)