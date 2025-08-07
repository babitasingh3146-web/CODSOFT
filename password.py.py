import random
import string

print("=== Password Generator ===")

# Ask user for password length
length = int(input("Enter the password length: "))

# Ask user for complexity
print("\nChoose complexity:")
print("1. Only letters (a-z, A-Z)")
print("2. Letters and digits")
print("3. Letters, digits, and symbols")

choice = input("Enter your choice (1/2/3): ")

# Select characters based on complexity
if choice == '1':
    characters = string.ascii_letters  # a-z, A-Z
elif choice == '2':
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
elif choice == '3':
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice! Defaulting to letters only.")
    characters = string.ascii_letters

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

print(f"\nYour generated password is: {password}")
