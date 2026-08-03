# Using OOP
class Student:
    """Class to represent a student and their grades."""

    def __init__(self, name, scores, average, grade, message):
        self.name = name
        self.scores = scores[:]
        self.average = average
        self.grade = grade
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
            except ValueError:  # Added exception handling for non-integer input
                print("Enter a valid number please")

        for i in range(num):
            while True:
                try:
                    score = float(input(f"Enter score for subject {i + 1}: "))
                    self.scores.append(score)
                    break
                except ValueError:   # Added exception handling for non-numeric input
                    print("We need numbers to produce something meaningful.")
                
    def find(self):
        """Calculate the average and grade for the student."""
        self.average = sum(self.scores) / len(self.scores)
        self.grade = self.get_grade(self.average)
        self.message = self.get_message()

    def get_average_grade(self):
        """Return the letter grade corresponding to the student's average score."""
        if self.average >= 90:
            return "A"
        elif self.average >= 80:
            return "B"
        elif self.average >= 70:
            return "C"
        elif self.average >= 60:
            return "D"
        else:
            return "F"

    def get_message(self):
        """Return a feedback message based on the student's grade."""
        feedback = {
            "A": "Excellent work!",
            "B": "Good job!",
            "C": "You can do better.",
            "D": "Needs improvement.",
            "F": "Failing. Please, seek help.",
        }
        worst_grade = max(self.grades)
        return feedback[worst_grade]

        return feedback[self.grade]

    def display(self):
        """Print the student's grade report."""
        average_grade = self.get_average_grade()
        print(f"\n--- Grade Report for {self.name} ---")
        print(f"Scores  : {self.scores}")
        print(f"Average : {self.average}")
        print(f"Grade   : {self.grade}")
        print(f"Average : {self.average:.2f}  (Grade: {average_grade})")
        print(f"Grades  : {self.grades}")
        print(f"Message : {self.message}")
        print("--------------------")


def main():
    """Collect and display grade reports for one or more students."""
    while True:
        name = input("Enter the student's name: ")
        student = Student(name, [], 0, "", "")
        student.start()
        student.enter_scores()
        student.find()
        student.display()
        again = input("\nAdd another student? (y/n): ").lower()
        if again != "y":
            print("\nAll done. Goodbye!")
            break


if __name__ == "__main__":
    main()
    print("------------------------")


def main():
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


main()