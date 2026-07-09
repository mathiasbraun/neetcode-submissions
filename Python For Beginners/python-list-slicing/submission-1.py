from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    output_list = []
    for i in range(1, 4):
        output_list.append(my_list[-4+i])
    return output_list


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
