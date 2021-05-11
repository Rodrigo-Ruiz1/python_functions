def find_smallest(list_of_numbers):
    smallest_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number < smallest_number:
            smallest_number = number
    return smallest_number
print(find_smallest([-3, -2, 1, 2, 3]))



def find_largest(list_of_numbers):
    largest_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number > largest_number:
            largest_number = number
    return largest_number
# print(find_largest([-3, -2, 1, 2, 3]))
    