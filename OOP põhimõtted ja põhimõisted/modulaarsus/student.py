class Student:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.grades = {}

    def set_id(self, student_id):
        if self.id is None:
            self.id = student_id
            
    def get_id(self):
        return self.id

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_grades(self):
        return list(self.grades.items())

    def get_average_grade(self):
        if not self.grades:
            return -1
        total = sum(self.grades.values())
        return total / len(self.grades)

    def __repr__(self):
        return self.name