# Using OOP
class Student:
    """Class to represent a student and their grades."""
    def _init_(self, name, scores, average, grades, message):
        self.name = name
        self.scores = scores[:]
        self.average = average
        self.grades = grades[:]
        self.message = message
    
    """Instance methods to handle student data and grades."""
    def start(self):
        print(f"Please, enter the grades for your student {self.name}")
    
    def enter_scores(self):
        num = int(input(f"How many subjects does {self.name} have? "))
        for i in range(num):
            score = int(input(f"Enter score for subject {i + 1}: "))
            self.scores.append(score)
    
    def find(self):
        self.average = sum(self.scores) / len(self.scores)
        for score in self.scores:
            if score >= 90:
                self.grades.append("A")
            elif score >= 80:
                self.grades.append("B")
            elif score >= 70:
                self.grades.append("C")
            elif score >= 60:
                self.grades.append("D")
            else:
                self.grades.append("F")
        self.message = self.get_message()