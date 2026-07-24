def bgm_calcu(weight,height):
    BMI = weight / (height * height)
    return BMI
def main():
    try:
        weight = int(input("Enter weight: "))
        height = int(input("Enter height: "))
    except ValueError:
        print("Please enter a integer")
    bgm_calcu(weight,height)
if  __name__ == "__main__":
    main()