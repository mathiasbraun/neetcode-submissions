from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best = 0
    name = None
    for student_score in scores:
        student, score = student_score
        if score > best:
            best, name = score, student
    return name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
