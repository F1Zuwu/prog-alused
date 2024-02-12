class Course:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, student, grade):
        self.grades.append((student, grade))

    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        if not self.grades:
            return -1
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)

    def __repr__(self):
        return self.name