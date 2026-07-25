# Project7
# BMI Calculator

A simple tool to calculate your Body Mass Index (BMI) based on your weight and height. It calculates your BMI and tells you which category you fall into (Underweight, Normal, Overweight, or Obese).

## What It Does

- Takes your weight (in kg) and height (in meters)
- Calculates BMI using the formula: weight / (height²)
- Displays your BMI number
- Categorizes your BMI into one of four categories
- Validates input to make sure you enter numbers

## Features

- **Weight input** - Enter your weight in kilograms
- **Height input** - Enter your height in meters
- **BMI calculation** - Uses the standard BMI formula
- **BMI categorization** - Shows which category you fall into
- **Error handling** - Checks if input is valid (not text or empty)
- **Clean output** - Displays both the BMI number and category

## BMI Categories

- **Underweight** - BMI < 18.5
- **Normal weight** - BMI 18.5 to 24.9
- **Overweight** - BMI 25 to 29.9
- **Obese** - BMI ≥ 30

## How to Run

```bash
python bmi_calculator.py
```

Then enter your weight and height.

## Example Usage

```
Enter weight: 65
Enter height: 1.75
BMI: 21.22
Normal weight
```

Another example:
```
Enter weight: 85
Enter height: 1.75
BMI: 27.76
Overweight
```

Invalid input:
```
Enter weight: abc
Enter height: 1.75
Please enter a integer
```

## What I Learned

- **Functions** - Breaking code into separate functions for different tasks
- **Function parameters** - Passing weight and height to calculation function
- **Return values** - Using `return` to send BMI back to main function
- **Multiple functions** - Using one function for calculation and another for categorization
- **If-elif-else chains** - Using multiple conditions to categorize BMI
- **Exception handling** - Try-except to catch ValueError when user enters text
- **F-strings** - Using f"BMI: {BMI}" to format output nicely
- **Formula implementation** - Converting a real-world formula into code

## Code Structure

```python
def bmi_calcu(weight, height):
    # Takes weight and height
    # Calculates BMI using formula
    # Returns the BMI value

def bmi_categ(BMI):
    # Takes BMI value
    # Uses if-elif-else to determine category
    # Prints the category

def main():
    # Gets user input for weight and height
    # Validates input with try-except
    # Calls bmi_calcu function
    # Calls bmi_categ function
    # Displays results
```

## Challenges I Faced

- **Understanding the BMI formula** - Had to look up that height is squared (height²)
- **Multiple functions** - Deciding which job each function should do
- **Error handling** - Making sure invalid input doesn't crash the program
- **Categorization logic** - Getting the if-elif-else conditions in right order
- **Float vs integer** - Learning that weight and height need to be floats, not integers
- **Output formatting** - Deciding how to display BMI nicely

## Things I Could Add Later

- Input validation (check if weight/height is positive number)
- Calculate ideal weight range (based on height)
- Track BMI over time (save to file)
- Multiple unit support (pounds/inches, stones/feet)
- Health tips (give advice based on BMI category)
- Age consideration (BMI calculator is different for children)
- Metric conversions (convert pounds to kg automatically)

## Why This Matters

This project taught me how to:
- Take a real-world formula and code it
- Organize code using functions
- Use if-elif-else for decision-making
- Handle user input safely

It's a practical tool that could actually be useful! Shows that simple code can solve real problems.

Key learnings:
- Functions make code reusable and organized
- Error handling is essential for user applications
- Real-world problems = real programming practice
- Simple logic + good structure = useful tool

Next: Add more features like tracking BMI history! 📊