# Grade Calculator
# Lets the user enter scores for a course, then shows the average and letter grade.
# Stage 2 update: added input validation so invalid entries no longer crash the program.


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


def get_valid_score():
    """Return a valid score, 'undo', or None when the user types 'done'."""
    while True:
        entry = input("Enter a score 0-100 (or 'undo' or 'done'): ").strip()
        command = entry.lower()

        if command == "done":
            return None
        if command == "undo":
            return "undo"

        try:
            score = float(entry)
        except ValueError:
            print("Invalid input. Enter a number, 'undo', or 'done'.")
            continue

        if not 0 <= score <= 100:
            print("Score must be between 0 and 100.")
            continue

        return score


def main():
    scores = []  # Stores every score the user enters

    print("=== Grade Calculator ===")
    print("Enter scores one at a time. Type 'undo' to remove the last score.")
    print("Type 'done' when finished.\n")

    while True:
        score = get_valid_score()

        if score is None:
            break

        if score == "undo":
            if scores:
                removed_score = scores.pop()
                print(f"Removed score: {removed_score:g}")
            else:
                print("There are no scores to undo.")
            continue

        scores.append(score)

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