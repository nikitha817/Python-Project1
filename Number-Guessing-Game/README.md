# Number Guessing Game

This is a number guessing game I made for my Python class. Basically the computer picks a random number between 1 and 100, and you get 6 tries to guess it. After each guess, it tells you if you're too high or too low.

## How to Run

Make sure you have Python installed first.

Then run this command:
```
python number_guess.py
```

That's it! The game will start.

## How to Play

- The computer thinks of a random number (between 1-100)
- You enter your guess
- The game tells you if you're too high or too low
- You get 6 tries total to find the number
- If you guess correctly, it shows how many tries it took
- If you run out of tries, the game ends

## Example Gameplay

```
Attempt 1/6 - Enter your guess: 50
Too low
Attempt 2/6 - Enter your guess: 75
Too high
Attempt 3/6 - Enter your guess: 60
Too high
Attempt 4/6 - Enter your guess: 55
Found it!! in 4 trial(s)
```

## How the Code Works

I have two main functions:

**number_guess()** - This does all the game stuff:
- Runs a loop for 6 attempts
- Gets your input each round
- Checks if you typed an actual number (if you don't, it asks you to try again without using up a try)
- Compares your guess to the secret number
- Tells you if you're too high or too low
- Stops when you either guess it right or run out of tries

**main()** - This is how it all starts:
- Generates the random number
- Calls the game function to begin

## Requirements

Just Python (Python 3 or higher). That's it! The `random` module is already built-in so you don't need to install anything else.

## Future Ideas

Things I might add if I have time:
- Different difficulty levels (easier/harder)
- Keep score if you play multiple times
- Add hints to help you narrow it down
- Show your previous guesses so you don't guess the same number twice
- Add a timer to make it harder
- Maybe a leaderboard or something
