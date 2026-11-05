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
    """Ask for one score and keep asking until the input is valid.

    Returns the score as a float, or None if the user types 'done'.
    Returning None (instead of a number) lets main() tell the difference
    between "the user finished" and "the user entered a score".
    """
    while True:
        entry = input("Enter a score 0-100 (or 'done'): ").strip()

        if entry.lower() == "done":
            return None

        # float() raises ValueError for text like "abc", so we catch it
        # and re-prompt instead of letting the program crash.
        try:
            score = float(entry)
        except ValueError:
            print("Invalid input. Please enter a number, or 'done' to finish.")
            continue

        # Written as "not 0 <= score <= 100" on purpose: values like "nan"
        # convert to a float successfully, but every comparison with nan is
        # False, so this check also rejects them (and "inf").
        if not 0 <= score <= 100:
            print("Score must be between 0 and 100.")
            continue

        return score


def main():
    scores = []  # Stores every score the user enters

    print("=== Grade Calculator ===")
    print("Enter your scores one at a time. Type 'done' when finished.\n")

    # Keep collecting scores until get_valid_score() signals 'done' with None.
    # A sentinel word is used because we don't know in advance how many scores there will be.
    while True:
        score = get_valid_score()

        if score is None:
            break

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