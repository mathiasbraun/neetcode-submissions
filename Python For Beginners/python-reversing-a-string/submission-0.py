def reverse_string(input_string: str) -> str:
    bump = input_string[0]
    return input_string[len(input_string)-1:0:-1] + bump

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
