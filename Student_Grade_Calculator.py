def get_name():
    """Ask the user for the student's first and last name and return the full name."""
    name = input("Enter student name: ")
    return name


def get_scores():
    """Ask the user for the student's scores and return a list of scores (floats)."""
    scores = []
    print("Enter the student's scores. Type 'done' when finished.")
    while True:
        user_input = input("Enter score: ")
        if user_input.lower() == "done":
            break
        try:
            score = float(user_input)
            scores.append(score)
        except ValueError:
            print("Please enter a valid number (e.g. 85 or 78.5) for the score.")
    return scores


def calculate_average(scores):
    """Returns the average of a list of scores"""
    return sum(scores) / len(scores)


def get_letter_grade(score):
    """Return the letter grade for a single numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_grades(scores):
    """Calculate and return a letter grade for each score."""
    grades = []
    for score in scores:
        grades.append(get_letter_grade(score))
    return grades


def get_message(name, scores, grades):
    """Return feedback based on the student's worst grade."""
    feedback = {
        "A": "Excellent work!",
        "B": "Good job!",
        "C": "You can do better.",
        "D": "Needs improvement.",
        "F": "Failing. Please seek help.",
    }
    worst_grade = max(grades)
    return feedback[worst_grade]


def print_report(name, scores, average, grades, message):
    """Print the full grade report."""
    average_grade = get_letter_grade(average)
    print("\n--- Grade Report ---\n")
    print(f"Student : {name}")
    print(f"Scores  : {scores}")
    print(f"Average : {average:.2f}  (Grade: {average_grade})")
    print(f"Grades  : {grades}")
    print(message)
    print("------------------------")


def main():
    """Main function to run the student grade calculator."""
    while True:
        name = get_name()
        scores = get_scores()

        if not scores:
            print(f"No scores entered for {name}. Skipping.\n")
        else:
            average = calculate_average(scores)
            grades = get_grades(scores)
            message = get_message(name, scores, grades)
            print_report(name, scores, average, grades, message)

        again = input("\nAdd another student? (y/n): ").lower()
        if again != "y":
            print("\nAll done. Goodbye!")
            break


main()