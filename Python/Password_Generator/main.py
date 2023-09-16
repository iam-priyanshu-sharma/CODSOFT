import random
import string

from art import logo

"""
Here, In this project i use string module instead of creating Lists or tuple of uppercase, lowercase, digits and special characters.
"""


def generate_password(length, include_uppercase=True, include_digits=True, include_special_chars=True):
    # Define character sets based on complexity options
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if include_uppercase else ""
    digit_chars = string.digits if include_digits else ""
    special_chars = string.punctuation if include_special_chars else ""

    # Combine character sets based on complexity options
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    if not all_chars:
        print("Error: You must include at least one character set.")
        return

    # Check if the length is valid
    if length < 1:
        print("Error: Password length must be at least 1.")
        return

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


# Get user input for password parameters
print(logo)
length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
include_digits = input("Include digits? (yes/no): ").lower() == "yes"
include_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

# Generate and print the password
password = generate_password(length, include_uppercase, include_digits, include_special_chars)
print("Generated Password:", password)
