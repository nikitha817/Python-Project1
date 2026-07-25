# Project3
# Student Management System

This project let me work with dictionaries and lists to store and manage student data. It was really cool because it does a lot of calculations automatically!

## What It Does

- Add new students with their marks
- Store multiple students in memory
- Calculate total marks for each student
- Calculate average marks
- Automatically assign grades (A, B, C, D, F)
- Display a nicely formatted report for each student

## Features

- **Add students** - Enter student name and marks in different subjects
- **Calculate totals** - Automatically sum all marks
- **Calculate averages** - Get the average mark
- **Auto-grade** - Automatically assign A/B/C/D/F based on average
- **Generate reports** - Display student info in a formatted way
- **Multiple students** - Can add and manage many students

## How to Run

```bash
python Project3.py
```

Follow the menu to add students and view reports!

## What I Learned

- **Dictionaries** - Using key-value pairs to store student info
- **Lists** - Storing multiple student dictionaries in a list
- **Nested data structures** - Dictionaries inside lists
- **Loops** - Going through all students to calculate and display
- **String formatting** - Making output look organized
- **Conditional logic** - Using if-else for grade assignment
- **Automation** - Letting the computer do calculations

## Example

```
======= Add Student =======
Enter student name: Aarav
Enter marks in Math: 85
Enter marks in English: 78
Enter marks in Science: 92

Total Marks: 255
Average Marks: 85
Grade: A

Student added successfully!
```

## Code Structure

```python
students = [
    {
        'name': 'Aarav',
        'marks': {'math': 85, 'english': 78, 'science': 92},
        'total': 255,
        'average': 85,
        'grade': 'A'
    }
]
```

**Main functions:**
- `add_student()` - Add a new student
- `calculate_total()` - Sum all marks
- `calculate_average()` - Get average mark
- `assign_grade()` - Decide A/B/C/D/F
- `display_report()` - Show student info

## Grade Scale

- **A:** Average ≥ 85
- **B:** Average ≥ 75  
- **C:** Average ≥ 65
- **D:** Average ≥ 55
- **F:** Average < 55

## Things I Could Add Later

- Search for a specific student by name
- Update a student's marks
- Delete a student record
- Sort students by grade or name
- Show class statistics (highest score, average class performance)

## Challenges I Faced

- Understanding nested dictionaries (dictionaries inside lists)
- Getting loops to work correctly with nested data
- Formatting the output so it looks organized
- Calculating totals and averages correctly
- Assigning grades based on different conditions

## Why This Matters

This project taught me how real systems store data. Schools use systems like this to manage student records! It shows that with good data structure and functions, you can automate a lot of work.

This was a major step up from the calculator because it handles **real, complex data** instead of just two numbers. 🎓