# Password Generator

This is a simple password generator I made for a Python project. You tell it how long you want the password to be, and it creates a random one using letters, numbers, and special characters.

## How to Run

Make sure you have Python installed (Python 3 or higher).

Then run:
```
python password_generator.py
```

The program will ask you for the password length, and it'll generate a random password for you.

## How to Use It

1. Run the script
2. When it asks "Enter the password length:", type in a number (like 12 or 16)
3. It generates a random password with that many characters
4. The password gets printed to the screen

That's it!

## Example

```
Enter the password length: 12
Generated Password: aK#7mP2$xLqR
```

```
Enter the password length: 20
Generated Password: 9vF@kL3bY&wQz1mE5jSt
```

## How the Code Works

The script has a few key parts:

**Getting user input** - It asks you to enter the password length and tries to convert it to an integer. If you type something that's not a number, it catches the error and tells you "Invalid Input!"

**Generating the password** - If you enter a valid number, it creates a password by randomly choosing characters from:
- Lowercase letters (a-z)
- Uppercase letters (A-Z)
- Numbers (0-9)
- Special characters like !, @, #, $, %, &, etc.

It picks random characters from all of these until the password reaches the length you specified.

**Displaying the result** - Once it's done, it prints out your new password.

## What You Need

Just Python! The `random` and `string` modules are built into Python, so you don't need to install anything else.

## Things to Know

- You can make passwords as long as you want (though really long ones might take a second)
- The passwords are totally random, so they're usually pretty secure
- Each time you run it, you get a different password
- If you don't enter a number, it'll tell you the input is invalid and won't crash

## Ideas for Improvement

If I decide to improve this later, I could:
- Let you choose what types of characters to include (like only letters, or no special characters)
- Save the password to a file so you don't lose it
- Generate multiple passwords at once
- Add an option to exclude confusing characters like 0/O or 1/l
- Make it copy the password to your clipboard automatically
- Let you exclude certain characters if you want
