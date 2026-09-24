# Random Password Generator

## Project Description

This project is a Python-based Random Password Generator developed as part of the Oasis Infobyte Internship (OIBSIP).

The program generates random passwords according to the user's selected requirements.

## Features

* Allows the user to enter the desired password length.
* Minimum password length of 8 characters is enforced.
* Supports uppercase letters.
* Supports lowercase letters.
* Supports numbers.
* Supports symbols.
* Requires at least two character types to be selected.
* Validates incorrect password lengths.
* Generates a random password based on the selected criteria.
* Allows the user to generate another password without restarting the program.

## Technologies Used

* Python
* random module
* string module

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python password_generator.py
```

4. Enter the required password length.
5. Select the character types.
6. The program will generate and display the password.
7. Choose whether to generate another password.

## Input Validation

The program checks:

* Password length must be at least 8 characters.
* At least two character types must be selected.
* Invalid length input is rejected.

## Project Structure

```text
Python-Task3-RandomPasswordGenerator/
│
├── password_generator.py
├── README.md
└── screenshots/
```

## Sample Output

```text
===== Random Password Generator =====

Enter password length (minimum 8): 12

Choose character types:
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password: Example@123X
```

## Internship

Oasis Infobyte Internship (OIBSIP)

Task 3 - Random Password Generator
