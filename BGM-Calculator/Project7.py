def bmi_calcu(weight,height):
    BMI = weight / (height * height)
    return BMI
def bmi_categ(BMI):
    if BMI < 18.5:
        print("Underweight")
    elif BMI < 25:
        print("Normal weight")
    elif BMI < 30:
        print("Overweight")
    else:
        print("Obese")
def main():
    try:
        weight = float(input("Enter weight: "))
        height = float(input("Enter height: "))
    except ValueError:
        print("Please enter a integer")
    BMI = bmi_calcu(weight,height)
    print(f"BMI: {BMI}")
    bmi_categ(BMI)
if  __name__ == "__main__":
    main()