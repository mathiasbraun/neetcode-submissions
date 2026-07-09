from typing import List # this is used to add type hints for List type
# Accept the challenge!

def get_sum(nums: List[int]) -> int:
    # return sum(nums)
    if nums:
        count = 0
        for element in nums:
            count += element
        return count
    else:
        return "The list is empty!"

def get_min(nums: List[int]) -> int:
    # return min(nums)
    if nums:
        minimum = nums[0]
        for element in nums:
            if element < minimum:
                minimum = element
        return minimum
    else:
        return "The list is empty!"

def get_max(nums: List[int]) -> int:
    # return max(nums)
    if nums:
        maximum = nums[0]
        for element in nums:
            if element > maximum:
                maximum = element
        return maximum
    else:
        return "The list is empty!"

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
