import random
import string


def generate_password(length, character_types):
    characters = ""
    password = []

    if "uppercase" in character_types:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if "lowercase" in character_types:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if "numbers" in character_types:
        characters += string.digits
        password.append(random.choice(string.digits))

    if "symbols" in character_types:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    remaining_length = length - len(password)

    for _ in range(remaining_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)


while True:
    print("\n===== Random Password Generator =====")

    # Password length
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("Password length must be at least 8.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # Character type selection
    character_types = []

    print("\nChoose character types:")

    uppercase = input("Include uppercase letters? (y/n): ").lower()
    if uppercase == "y":
        character_types.append("uppercase")

    lowercase = input("Include lowercase letters? (y/n): ").lower()
    if lowercase == "y":
        character_types.append("lowercase")

    numbers = input("Include numbers? (y/n): ").lower()
    if numbers == "y":
        character_types.append("numbers")

    symbols = input("Include symbols? (y/n): ").lower()
    if symbols == "y":
        character_types.append("symbols")

    # At least 2 types required
    if len(character_types) < 2:
        print("\nError: Please select at least 2 character types.")
        continue

    # Generate password
    password = generate_password(length, character_types)

    print("\nGenerated Password:", password)

    # Generate another password
    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("\nThank you for using Random Password Generator!")
        break