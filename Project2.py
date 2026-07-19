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
    print("====Student Information====")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print("Average Marks: ", average_marks)
    print("Total Marks: ", calculate_total(student['marks']))
    print("Grade: ",grade(average_marks))
    for subject, mark in student["marks"].items():
        print(f"{subject}: {mark}")
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