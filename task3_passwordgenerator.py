import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

try:
    length = int(input("\t\t\n----:Enter the  length of password:---> "))
    if length <= 0:
        print("Password length must be a positive number.")
    else:
        print("\nGenerating Password.....")
        print("Your Password:", generate_password(length))
        print("\n")
except ValueError:
    print("Please enter a valid number.")
