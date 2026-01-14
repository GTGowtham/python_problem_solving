def create_largest_number(number_list):
    number_list = [str(num) for num in number_list]
    for i in range(len(number_list)):
        for j in range(i + 1, len(number_list)):
            if number_list[i] + number_list[j] < number_list[j] + number_list[i]:
                temp = number_list[i]
                number_list[i] = number_list[j]
                number_list[j] = temp

    # Step 3: join the result
    return "".join(number_list)


    # remove pass and write your logic here


number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)