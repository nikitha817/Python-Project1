def Student_info():
    student ={
        "name": input("Enter your name: "),
        "age": int(input("Enter your age: ")),
        "subjects" :[
    "Maths",
    "Science",
    "English",
    "History",
    "Geography"
],
        "marks": {}
        }
    for subject in student["subjects"]:
        student["marks"][subject] = int(input(f"Enter your {subject} marks: "))
    return student
def calculate_total(marks):
    total_marks = sum(marks.values())
    return total_marks
def calculate_average(marks):
    average = calculate_total(marks) / len(marks)
    return average
def display_student_info(student):
    average_marks = calculate_average(student["marks"])
    print(f"{'Student Report':^60}")
    print(f"{'=' * 55}\n{'-' * 55}")
    print(f"{student['name']:^60}")
    print("-" * 55)
    print(f"|{'Name':<20}: {student['name']}{"|":^59}")
    print(f"|{'Age':<20}: {student['age']}{"|":^60}")
    print("-" * 55)
    for subject, mark in student["marks"].items():
        print(f"|{subject:<20}: {mark}{"|":^60}")
    print("-" * 55)
    print(f"|{'Average Marks':<20}: {average_marks}{"|":^56}")
    print(f"|{'Total Marks':<20}: {calculate_total(student['marks'])}{"|":^57}")
    print(f"|{'Grade':<20}: {grade(average_marks)}{"|":^61}")

def grade(average):
    if average >= 90:
        return "A"
    elif average >= 85:
        return "B"
    elif average >= 75:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 45:
        return "E"
    elif average < 45:
        return "Fail"
    else:
        return "Invalid Marks"
def main():
    student1 =  Student_info()
    display_student_info(student1)
if __name__ == "__main__":
    main()