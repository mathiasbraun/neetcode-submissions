class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        checked = 0

        while students and checked < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                checked = 0
            else:
                stud = students[0]
                students.pop(0)
                students.append(stud)
                checked += 1

        return len(students)