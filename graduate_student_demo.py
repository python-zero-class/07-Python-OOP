class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

class GraduateStudent(Student):
    def __init__(self, name, grades, research_topic):
        super().__init__(name, grades)
        self.research_topic = research_topic
    
    def introduce(self):
        print(f'My name is {self.name} and I research {self.research_topic}.')

if __name__ == "__main__":
    grad_student = GraduateStudent('Alice', [88, 92, 95], 'Quantum Computing')
    grad_student.introduce()