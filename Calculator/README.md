# Calculator

This was my first real programming project after learning about functions! It's a simple calculator that does basic math.

## What It Does

You run it, pick an operation (add/subtract/multiply/divide), type two numbers, and it gives you the answer. Then you can do another calculation or exit.

## Features

- **Addition** - Add two numbers
- **Subtraction** - Subtract two numbers  
- **Multiplication** - Multiply two numbers
- **Division** - Divide two numbers
- **Loop until exit** - Keep calculating until you want to stop
- **Menu** - Choose what you want to do

## How to Run

```bash
python Project1.py
```

Then just follow the menu!

## What I Learned

- **Functions** - How to create functions and call them
- **If-else statements** - Making decisions in code
- **While loops** - Repeating code until a condition is false
- **User input** - Using `input()` to get data from users
- **String formatting** - Making text look nice
- **Basic validation** - Checking if input is valid before using it

## Example

```
==== Calculator ====
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Choose an operation: 1
Enter first number: 5
Enter second number: 3
Result: 8
```

## Code Structure

The code uses functions for each operation:
- `add(x, y)` - Adds two numbers
- `subtract(x, y)` - Subtracts two numbers
- `multiply(x, y)` - Multiplies two numbers
- `divide(x, y)` - Divides two numbers
- `main()` - Runs the menu and calculator

## Things I Could Add Later

- Square root function
- Exponents (power)
- Memory feature (remember the last answer)
- Modulus and floor division operations

## Challenges I Faced

- Handling division by zero (had to add error checking)
- Making sure the menu loops properly
- Understanding how functions return values

This was fun to build and taught me the basics of how real programs work!