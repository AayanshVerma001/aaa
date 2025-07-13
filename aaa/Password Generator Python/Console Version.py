import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short!"

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

while True:
    try:
        length = int(input("Enter desired password length: "))
        print("Generated Password:", generate_password(length))
        if input("Generate another? (y/n): ").lower() != 'y':
            break
    except ValueError:
        print("❌ Please enter a valid number.")