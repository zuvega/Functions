def unique_element(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

print(unique_element([1, 3, 3, 3, 6, 2, 3, 5]))
