import random
def number_guess(random_number):
    for trial in range(1, 7):
        try:
            user_input = int(input(f"Attempt {trial}/6 - Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if random_number > user_input:
            print("Too low")
        elif random_number < user_input:
            print("Too high")
        else:
            print(f"Found it!! in {trial} trial(s)")
            return

    print("Trials are over! Better luck next time")
def main():
    random_number = random.randint(1, 100)
    number_guess(random_number)
if __name__ == "__main__":
    main()