class Solution:
    def countStudentsIterate(self, students: List[int], sandwiches: List[int]) -> int:
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

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud_0 = students.count(0)
        stud_1 = len(students) - students.count(0)

        for sandwich in sandwiches:
            if sandwich == 0:
                if stud_0 == 0:
                    break
                    # break if no one wants sandwich 0
                stud_0 -= 1
            else:
                if stud_1 == 0:
                    break
                    # break if no one wants sandwich 1
                stud_1 -= 1

        return stud_0 + stud_1
