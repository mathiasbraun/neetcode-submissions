from typing import List

def contains_duplicate(words: List[str]) -> bool:
    # for word in words:
    #    for successor in words[words.index(word)+1:len(words)]:
    #        if successor == word:
    #            return True
    # return False
    my_set = set()
    for word in words:
        if word in my_set:
            return True
        my_set.add(word)
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
