class School:
    def __init__(self,school_name):
        self.school_name = school_name
        self._roster = {}

    def roster(self):
        return self._roster

    def add_student(self,student_name,student_grade):
        if student_grade not in self._roster:
            self._roster[student_grade] = []
            self._roster[student_grade].append(student_name)
        else:
            self._roster[student_grade].append(student_name)

    def grade(self,school_grade):
        return self._roster[school_grade]

    def sort_roster(self):
        for grade in self._roster:
            self._roster[grade].sort()
        return self._roster
