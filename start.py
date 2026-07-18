def get_name():
    """Ask the user for the student's first and last name and return the full name."""
    name = input("Enter student name: ")
    return name


def get_scores():
    """Ask the user for the student's scores and return a list of scores."""
    scores = []
    print("Enter the student's scores. Type 'done' when finished.")
    while True:
        user_input = input("Enter score: ")
        if user_input.lower() == "done":
            break
        try:
            score = int(user_input)
            scores.append(score)
        except ValueError:
            print("Please enter a valid integer for the score.")
    return scores


def calculate_average(scores):
    """Returns the average of a list of scores"""
    return sum(scores) / len(scores)


def get_grades(scores):
    """Calculate and return a letter grade for each score."""
    grades = []
    for score in scores:
        if score >= 90:
            grades.append("A")
        elif score >= 80:
            grades.append("B")
        elif score >= 70:
            grades.append("C")
        elif score >= 60:
            grades.append("D")
        else:
            grades.append("F")
    return grades