# Grade Calculator
# Lets the user enter scores for a course, then shows the average and letter grade.


def calculate_average(scores):
    """Return the average of a list of scores."""
    # Guard against an empty list: dividing by zero would crash the program.
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


def get_letter_grade(average):
    """Convert a numeric average into a letter grade using a standard 10-point scale."""
    # Checked from highest to lowest so the first matching cutoff wins.
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    scores = []  # Stores every score the user enters

    print("=== Grade Calculator ===")
    print("Enter your scores one at a time. Type 'done' when finished.\n")

    # Keep asking for scores until the user types 'done'.
    # A sentinel word is used because we don't know in advance how many scores there will be.
    while True:
        entry = input("Enter a score (or 'done'): ")

        if entry.lower() == "done":
            break

        # Convert text to a number so it can be used in math.
        # (Assumes valid input for now; error handling can be added later.)
        scores.append(float(entry))

    # Only show results if at least one score was entered.
    if len(scores) == 0:
        print("\nNo scores were entered.")
        return

    average = calculate_average(scores)
    letter = get_letter_grade(average)

    print("\n--- Results ---")
    print(f"Scores entered: {scores}")
    print(f"Number of scores: {len(scores)}")
    print(f"Average: {average:.2f}")
    print(f"Letter grade: {letter}")


# Run main() only when this file is executed directly, not when imported.
if __name__ == "__main__":
    main()