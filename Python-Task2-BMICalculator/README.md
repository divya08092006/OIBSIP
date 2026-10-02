# BMI Calculator

## Project Overview

This project is a beginner-level Python command-line application that calculates a user's Body Mass Index (BMI) based on their weight and height.

The program calculates BMI using the formula:

**BMI = Weight / Height²**

It then classifies the BMI into four standard categories: Underweight, Normal, Overweight, and Obese.

## Features

* Accepts weight in kilograms
* Accepts height in meters
* Calculates BMI
* Displays BMI rounded to 2 decimal places
* Classifies BMI into health categories
* Validates non-numeric input
* Rejects zero and negative values
* Displays helpful error messages

## Technologies Used

* Python
* `input()`
* `float()`
* Basic arithmetic
* `if-elif-else`
* Exception handling

## BMI Categories

| BMI         | Category    |
| ----------- | ----------- |
| Below 18.5  | Underweight |
| 18.5 – 24.9 | Normal      |
| 25 – 29.9   | Overweight  |
| 30 or above | Obese       |

## How to Run

1. Install Python.
2. Open the project folder in VS Code or Command Prompt.
3. Run the following command:

```bash
python bmi_calculator.py
```

4. Enter your weight in kilograms.
5. Enter your height in meters.
6. The program displays your BMI and category.

## Example

```text
Enter your weight in kg: 60
Enter your height in meters: 1.65

Your BMI is: 22.04
Category: Normal
```

## Project Type

Oasis Infobyte Internship — Python Programming

## Task

BMI Calculator