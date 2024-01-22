class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, course, grade):
        self.grades.append((course, grade))

    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)