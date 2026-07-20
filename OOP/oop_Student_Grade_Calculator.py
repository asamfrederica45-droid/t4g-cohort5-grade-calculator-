# Using OOP
class Student:
    """Class to represent a student and their grades."""
    def __init__(self, name, scores, average, grades, message):
        self.name = name
        self.scores = scores[:]
        self.average = average
        self.grades = grades[:]
        self.message = message
    
    """Instance methods to handle student data and grades."""
    def start(self):
        """Print a welcome message asking for the student's name."""
        print(f"Please, enter the grades for your student {self.name}")
    
    def enter_scores(self):
        while True:
            try:
               num = int(input(f"How many subjects does {self.name} have? "))
               break
            except ValueError: # Added exception handling for non-integer input
                print("Enter a valid number please")

        for i in range(num):
            while True:
                try:
                    score = int(input(f"Enter score for subject {i + 1}: "))
                    self.scores.append(score)
                    break
                except ValueError: # Added exception handling for non-integer input
                    print("We need numbers to produce something meaningful.")
                
    def find(self):
        """Calculate the average and grades for the student."""
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
    
    def get_message(self):
        """Return a feedback message based on the student's grades."""
        feedback = {
            "A": "Excellent work!",
            "B": "Good job!",
            "C": "You can do better.",
            "D": "Needs improvement.",
            "F": "Failing. Please seek help.",
        }
        worst_grade = max(self.grades)
        return feedback[worst_grade]
    
    def display(self):
        """Print the student's grade report."""
        print(f"\n--- Grade Report for {self.name} ---")
        print(f"Scores  : {self.scores}")
        print(f"Average : {self.average}")
        print(f"Grades  : {self.grades}")
        print(f"Message : {self.message}")
        print("--------------------")
        
"""Display the grade report for the student."""
while True:
    name = input("Enter the student's name: ")  
    student = Student(name, [], 0, [], "")
    student.start()
    student.enter_scores()
    student.find()
    student.message = student.get_message()
    student.display()
    again = input("\nAdd another student? (y/n): ").lower()
    if again != "y":
        print("\nAll done. Goodbye!")
        break