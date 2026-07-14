from typing import List

def read_integers() -> List[int]:
    input_string = input()
    string_list = input_string.split(",")
    integer_list = []
    for s in string_list:
        integer_list.append(int(s))
    return integer_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
