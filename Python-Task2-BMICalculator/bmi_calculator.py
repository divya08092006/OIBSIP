try:
    # Get input from user
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    # Validate input
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be greater than 0.")

    else:
        # Calculate BMI
        bmi = weight / (height ** 2)

        # Display BMI
        print("Your BMI is:", round(bmi, 2))

        # Classify BMI
        if bmi < 18.5:
            print("Category: Underweight")

        elif bmi < 25:
            print("Category: Normal")

        elif bmi < 30:
            print("Category: Overweight")

        else:
            print("Category: Obese")

except ValueError:
    print("Error: Please enter numbers only.")