import Project2
def Student_management():
    student = []
    return student

def main():
    student =Student_management()
    answer = input("Do you want to enter student information? (yes/no): ")
    while answer.lower() == "yes":
        student_info = Project2.Student_info()
        student.append(student_info)
        answer = input("Do you want to enter another student information? (yes/no): ")
        if answer.lower() == "yes":
            continue
        else:
            break
    for student_info in student:
        print("=" * 55)
        Project2.display_student_info(student_info)
if __name__ == "__main__":
    main()