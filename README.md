# Grade Calculator

## Project Description
A command-line Python program that lets a user enter course scores and then
calculates the average and the matching letter grade.

## Initial Version
The first version includes:
- `calculate_average()` function that returns the average of a list of scores
- `get_letter_grade()` function that converts an average to a letter (A-F)
- A `while` loop that keeps collecting scores until the user types `done`
- A list that stores all entered scores
- Output showing the scores, the count, the average, and the letter grade
- Handling for the case where no scores are entered

## AI Tool Used
Claude (by Anthropic), used through the Claude chat interface.

## AI Assistance
I asked Claude to help improve the program's handling of invalid input.
Specifically, I asked it to stop the program from crashing when a user types
text instead of a number, and to make sure scores outside a sensible range are
not accepted.

## New or Modified Features
- Added a `get_valid_score()` function that keeps prompting until the user
  enters a valid score or types `done`.
- Added `try/except` error handling so non-numeric input shows a friendly
  message instead of crashing.
- Added a range check so only scores from 0 to 100 are accepted (this also
  rejects values like `nan` and `inf`).
- Updated the main loop to use the new function, and updated the comments to
  explain the new logic.

## Evaluation of AI Output
I accepted Claude's approach of moving input handling into its own function
because it keeps `main()` simple and makes the validation logic easy to follow.
I tested it with letters, negative numbers, numbers over 100, and `nan`, and
each one was rejected correctly while valid scores still worked. I kept the
0-100 limit because it fits a typical grading scale, though a course with
extra credit would need a higher limit.

## How to Run the Program
1. Make sure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run: `python3 main.py`
4. Enter scores when prompted and type `done` to see results.

## Feature Development Comparison

On the `manual-feature` branch, I added the highest and lowest scores to the Grade Calculator’s results. I used Python’s `max()` and `min()` functions on the list of scores entered by the user. ChatGPT gave me a practice example and helped me spot that my first version was using a sample list. I updated both lines to use the actual scores. When I entered 70 and 60, the program correctly showed 70 as the highest score and 60 as the lowest.

On the `ai-feature` branch, I added an `undo` command so users can fix a mistake before finishing. ChatGPT drafted the code, and I added it to `main.py` and reviewed the changes with `git diff`. The command uses `pop()` to remove the most recent score. If the list is empty, the program displays a message and keeps asking for input.

The AI-generated code worked on my first run, and I kept it as written. I felt more confident with the manual approach because I understood what each line did and could see how switching from the sample list to scores made the results reflect what I actually entered.