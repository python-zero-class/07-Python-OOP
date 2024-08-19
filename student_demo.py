class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

if __name__ == "__main__":
    student = Student('John', [90, 85, 92])
    print(f"Average grade: {student.average_grade()}")