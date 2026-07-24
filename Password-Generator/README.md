# Password Generator

A simple tool that creates random, secure passwords. You choose the length, and it generates a password with letters, numbers, and special characters.

## What It Does

- Takes your input for password length
- Generates a random password using:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)
- Prints the generated password

## Features

- **Custom length** - You decide how long the password is
- **Mixed characters** - Uses letters, numbers, and punctuation
- **Random selection** - Each character is randomly chosen
- **Error handling** - Tells you if you enter something that's not a number
- **Simple & fast** - One command, instant password

## How to Run

```bash
python password_generator.py
```

Then enter your desired password length.

## Example Usage

```
Enter the password length: 12
Generated Password: 7kR#mP!xL2qQ
```

Another example:
```
Enter the password length: 8
Generated Password: aB3$xQp@
```

Invalid input:
```
Enter the password length: abc
Invalid Input!
```

## What I Learned

- **String module** - Using string.ascii_letters, string.digits, string.punctuation
- **Random choice** - random.choice() to pick random elements
- **List comprehension** - Creating random characters in a loop with `for _ in range()`
- **String joining** - Using ''.join() to combine list into single string
- **Exception handling** - Try-except to catch ValueError for non-numeric input
- **Else block** - Using else with try-except to run code only if no error

## Code Structure

```python
try:
    user_length = int(input("Enter the password length: "))
except ValueError:
    print("Invalid Input!")
else:
    # Create password with random characters
    password = ''.join(random.choice(...) for _ in range(user_length))
    print("Generated Password:", password)
```

## Character Sets Used

```python
string.ascii_letters      # A-Z and a-z
string.digits            # 0-9
string.punctuation       # !@#$%^&*()_+-=[]{}|;:,.<>?
```

Combines all three to make strong passwords.

## Challenges I Faced

- **String module** - Didn't know it existed at first, had to learn what's available
- **List comprehension** - Understanding the syntax `for _ in range()` took practice
- **Error handling** - Figuring out that non-numbers raise ValueError
- **Random selection** - Understanding how random.choice works on strings

## Things I Could Add Later

- Exclude ambiguous characters (0, O, l, 1) for readability
- Option to exclude special characters if user wants
- Copy to clipboard (automatically copy the password)
- Generate multiple passwords at once
- Password strength checker (show how strong the password is)
- Exclude certain characters (user choice)
- Save passwords to a file

## Why This Project Matters

This is my first project using the string module! It taught me that Python has built-in utilities for almost everything.

Key learnings:
- Libraries are powerful (string module had everything I needed)
- Random + loops = infinite combinations
- Error handling makes apps user-friendly
- Simple code can do powerful things

This could be a real utility app—people actually need password generators!

Next: Add features like password strength indicator. 🔐