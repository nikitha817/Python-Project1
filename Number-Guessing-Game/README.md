# Project5
# Number Guessing Game

A fun command-line game where the computer picks a random number and you try to guess it. You get 6 attempts to figure it out.

## What It Does

- Computer picks a random number between 1 and 100
- You get 6 tries to guess it
- After each guess, you get a hint ("too high" or "too low")
- If you guess correctly, you win
- If you run out of tries, game over

## Features

- **Random number generation** - Uses Python's random module
- **User input validation** - Checks if you entered a number (not text)
- **Attempt counter** - Tracks which attempt you're on (1-6)
- **Hints** - Tells you if your guess is too high or too low
- **Trial tracking** - Shows how many attempts it took to win
- **Error handling** - Doesn't crash if you enter bad input

## How to Run

```bash
python number_guess.py
```

Then guess the number!

## Example Game

```
Attempt 1/6 - Enter your guess: 50
Too high
Attempt 2/6 - Enter your guess: 25
Too low
Attempt 3/6 - Enter your guess: 37
Too low
Attempt 4/6 - Enter your guess: 43
Too high
Attempt 5/6 - Enter your guess: 40
Found it!! in 5 trial(s)
```

## What I Learned

- **Random module** - Generating random numbers with randint()
- **Loops** - Using for loop with range() to create attempts
- **Exception handling** - Try-except to catch invalid input (ValueError)
- **Conditionals** - Using if-elif-else for game logic
- **Functions** - Breaking game into functions (number_guess and main)
- **User feedback** - Giving helpful hints to guide the player

## Code Structure

```python
def number_guess(random_number):
    # Loop through attempts 1-6
    # Get user input
    # Validate input with try-except
    # Compare guess with random number
    # Give feedback

def main():
    # Generate random number
    # Call number_guess function
```

## Challenges I Faced

- **Error handling** - Learning what ValueError means and how to catch it
- **Loop control** - Making sure the loop exits when you win
- **User experience** - Realizing hints are better than just saying "wrong"
- **Attempt tracking** - Keeping count and showing it to the user

## Things I Could Add Later

- Difficulty levels (easy = 1-50, hard = 1-1000)
- Replay option (play multiple games without restarting)
- Score tracking (who won in fewest attempts)
- Time limit (guess within 30 seconds)
- Hints remaining counter (limited hints instead of unlimited tries)

## Why This Project Matters

This is my first real interactive game! It shows how loops, conditionals, and user input work together to create an actual game. Games are just logic + feedback.

This was fun and taught me:
- Exceptions are your friend (not scary)
- Good user feedback makes games better
- Simple logic = complex behavior

Next step: Add features like difficulty levels! 🎮