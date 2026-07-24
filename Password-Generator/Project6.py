import random
import string
try:
    user_length = int(input("Enter the password length: "))
except ValueError:
    print("Invalid Input!")
else:
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(user_length))
    print("Generated Password:", password)