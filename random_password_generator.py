import random
import string

# Creating the password

password = ""

# Enter length of the password

length = int(input("Enter password length:"))

# List of characters for password

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(length):
    password += random.choice(characters)

# Output

print("Your random password is:", password)
