def add_two_numbers() -> int:
    num_string = input()
    num_list = num_string.split(",")
    num_sum = 0
    for s in num_list:
        num_sum += int(s)
    return num_sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
