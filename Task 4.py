import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define possible characters
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation  # Includes punctuation symbols

    # Combine all possible characters
    all_characters = lowercase + uppercase + digits + symbols

    # Ensure each password has at least one of each type of character
    password = []
    password.append(random.choice(lowercase))
    password.append(random.choice(uppercase))
    password.append(random.choice(digits))
    password.append(random.choice(symbols))

    # Generate the rest of the password using random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password characters to mix the types
    random.shuffle(password)

    # Convert the list to a string
    password_string = ''.join(password)
    return password_string

def main():
    print("Welcome to the Password Generator!")
    print("---------------------------------")
    print("Produce strong passwords for various applications.\n")

    # Get user input for number of passwords and length
    num_passwords = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the length of each password: "))

    # Generate and print passwords
    print("\nGenerating passwords...")
    for _ in range(num_passwords):
        password = generate_password(length)
        print("Generated Password:", password)

    print("\nPassword generation complete!")

if __name__ == "__main__":
    main()
