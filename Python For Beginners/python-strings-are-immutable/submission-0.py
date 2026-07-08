def remove_fourth_character(word: str) -> str:
    if len(word) < 4:
        return "Invalid input!"
    elif len(word) == 4:
        return word[:3]
    else:
        first_half = word[:3]
        second_half = word[4:]
        return first_half + second_half


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
